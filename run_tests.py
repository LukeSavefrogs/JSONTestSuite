#!/usr/bin/env python3

import html
import io
import os
import os.path
import subprocess
import sys
import json

from os import listdir
from time import strftime

from JSONTestSuite import constants
from JSONTestSuite.programs import programs

def run_tests(restrict_to_path=None, restrict_to_program=None) -> None:
    """ Run all tests.
    
    Args:
        restrict_to_path (str): Restrict to a single file.
        restrict_to_program (str): Restrict to a single program.
    """
    FNULL = open(os.devnull, "w")
    log_file = open(constants.LOG_FILE_PATH, "w")

    prog_names = list(programs.keys())
    prog_names.sort()

    if isinstance(restrict_to_program, io.TextIOBase):
        restrict_to_program = json.load(restrict_to_program)

    if restrict_to_program:
        prog_names = filter(lambda x: x in restrict_to_program, prog_names)

    # Run tests for each program defined in the programs dict
    for prog_name in prog_names:
        program_config = programs[prog_name]

        url = str(program_config.get("url", ""))
        commands = program_config.get("commands", None)
        setup = program_config.get("setup", None)

        # Skip if no commands are defined
        if commands is None:
            print(f"-- skip {prog_name} (no commands)")
            continue

        # Run setup commands (if defined)
        if setup != None:
            print("--", " ".join(setup))
            try:
                subprocess.call(setup)
            except Exception as e:
                print("-- skip", e)
                continue

        # Search for JSON files in the test cases directory and run the program against each one
        for root, _, files in os.walk(constants.TEST_CASES_DIR_PATH):
            json_files = (f for f in files if f.endswith(".json"))
            for filename in json_files:
                # TODO: Analyze how this works
                if restrict_to_path:
                    restrict_to_filename = os.path.basename(restrict_to_path)
                    if filename != restrict_to_filename:
                        continue

                file_path = os.path.join(root, filename)

                use_stdin = "use_stdin" in program_config and program_config["use_stdin"]
                if use_stdin:
                    my_stdin = open(file_path, "rb")
                    process_args = commands
                else:
                    my_stdin = FNULL
                    process_args = commands + [file_path]

                print("--", " ".join(process_args))

                try:
                    status = subprocess.call(
                        process_args,
                        stdin=my_stdin,
                        stdout=FNULL,
                        stderr=subprocess.STDOUT,
                        timeout=5,
                    )
                    # print("-->", status)
                except subprocess.TimeoutExpired:
                    print("timeout expired")
                    status_log_entry = "%s\tTIMEOUT\t%s" % (prog_name, filename)
                    log_file.write("%s\n" % status_log_entry)
                    print("RESULT:", result)
                    continue
                except FileNotFoundError as e:
                    print("-- skip non-existing", e.filename)
                    break
                except OSError as e:
                    if e.errno == constants.INVALID_BINARY_FORMAT or e.errno == constants.BAD_CPU_TYPE:
                        print("-- skip invalid-binary", commands[0])
                        break
                    raise e

                if use_stdin:
                    my_stdin.close()

                result = None
                if status == 0:
                    result = "PASS"
                elif status == 1:
                    result == "FAIL"
                else:
                    result = "CRASH"

                status_log_entry = None
                if result == "CRASH":
                    status_log_entry = "%s\tCRASH\t%s" % (prog_name, filename)
                elif filename.startswith("y_") and result != "PASS":
                    status_log_entry = "%s\tSHOULD_HAVE_PASSED\t%s" % (prog_name, filename)
                elif filename.startswith("n_") and result == "PASS":
                    status_log_entry = "%s\tSHOULD_HAVE_FAILED\t%s" % (prog_name, filename)
                elif filename.startswith("i_") and result == "PASS":
                    status_log_entry = "%s\tIMPLEMENTATION_PASS\t%s" % (prog_name, filename)
                elif filename.startswith("i_") and result != "PASS":
                    status_log_entry = "%s\tIMPLEMENTATION_FAIL\t%s" % (prog_name, filename)

                if status_log_entry != None:
                    print(status_log_entry)
                    log_file.write("%s\n" % status_log_entry)

    FNULL.close()
    log_file.close()


def f_underline_non_printable_bytes(input_bytes: bytes) -> str:
    """ Return an HTML string where non-printable bytes are underlined.
    
    Args:
        input_bytes (bytes): Input bytes.
        
    Returns:
        html_string(str): The resulting HTML string.
    """
    html_string = ""

    has_non_printable_characters = False

    for b in input_bytes:
        is_not_printable = b < 0x20 or b > 0x7E

        has_non_printable_characters |= is_not_printable

        if is_not_printable:
            html_string += f"<U>{html.escape('%02X' % b)}</U>"
        else:
            html_string += html.escape("%c" % b)

    if has_non_printable_characters:
        try:
            html_string += html.escape(" <=> %s" % input_bytes.decode("utf-8", errors="ignore"))
        except:
            pass

    if len(input_bytes) > 36:
        return html.escape("%s(...)" % html_string[:36])

    return html_string


def f_status_for_lib_for_file(json_dir, results_dir):
    txt_filenames = [f for f in listdir(results_dir) if f.endswith(".txt")]

    # comment to ignore some tests
    statuses = [
        "SHOULD_HAVE_FAILED",
        "SHOULD_HAVE_PASSED",
        "CRASH",
        "IMPLEMENTATION_FAIL",
        "IMPLEMENTATION_PASS",
        "TIMEOUT",
    ]

    d = {}
    libs = []

    for filename in txt_filenames:
        path = os.path.join(results_dir, filename)

        with open(path) as f:
            for l in f:
                comps = l.split("\t")
                if len(comps) != 3:
                    print("***", comps)
                    continue

                if comps[1] not in statuses:
                    print("-- unhandled status:", comps[1])

                (lib, status, json_filename) = (comps[0], comps[1], comps[2].rstrip())

                if lib not in libs:
                    libs.append(lib)

                json_path = os.path.join(constants.TEST_CASES_DIR_PATH, json_filename)

                if json_path not in d:
                    d[json_path] = {}

                d[json_path][lib] = status

    return d, libs


def f_status_for_path_for_lib(json_dir, results_dir):
    txt_filenames = [f for f in listdir(results_dir) if f.endswith(".txt")]

    # comment to ignore some tests
    statuses = [
        "SHOULD_HAVE_FAILED",
        "SHOULD_HAVE_PASSED",
        "CRASH",
        "IMPLEMENTATION_FAIL",
        "IMPLEMENTATION_PASS",
        "TIMEOUT",
    ]

    d = {}  # d['lib']['file'] = status

    for filename in txt_filenames:
        path = os.path.join(results_dir, filename)

        with open(path) as f:
            for l in f:
                comps = l.split("\t")
                if len(comps) != 3:
                    continue

                if comps[1] not in statuses:
                    # print "-- unhandled status:", comps[1]
                    continue

                (lib, status, json_filename) = (comps[0], comps[1], comps[2].rstrip())

                if lib not in d:
                    d[lib] = {}

                json_path = os.path.join(constants.TEST_CASES_DIR_PATH, json_filename)

                d[lib][json_path] = status

    return d


def f_tests_with_same_results(libs, status_for_lib_for_file):
    tests_with_same_results = (
        {}
    )  # { {lib1:status, lib2:status, lib3:status} : { filenames } }

    files = list(status_for_lib_for_file.keys())
    files.sort()

    for f in files:
        prefix = os.path.basename(f)[:1]
        lib_status_for_file = []
        for l in libs:
            if l in status_for_lib_for_file[f]:
                status = status_for_lib_for_file[f][l]
                lib_status = "%s_%s" % (status, l)
                lib_status_for_file.append(lib_status)
        results = " || ".join(lib_status_for_file)
        if results not in tests_with_same_results:
            tests_with_same_results[results] = set()
        tests_with_same_results[results].add(f)

    r = []
    for k, v in tests_with_same_results.items():
        r.append((k, v))
    r.sort()

    return r


def generate_report(report_path, keep_only_first_result_in_set=False):
    (status_for_lib_for_file, libs) = f_status_for_lib_for_file(
        constants.TEST_CASES_DIR_PATH, constants.LOGS_DIR_PATH
    )

    status_for_path_for_lib = f_status_for_path_for_lib(
        constants.TEST_CASES_DIR_PATH, constants.LOGS_DIR_PATH
    )

    tests_with_same_results = f_tests_with_same_results(libs, status_for_lib_for_file)

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("""
            <!DOCTYPE html>
            <HTML>
                <HEAD>
                    <TITLE>JSON Parsing Tests</TITLE>
                    <LINK rel="stylesheet" type="text/css" href="style.css">
                    <META charset="UTF-8">
                </HEAD>
                <BODY>
        """)

        prog_names = list(programs.keys())
        prog_names.sort()

        libs = list(status_for_path_for_lib.keys())
        libs.sort()

        title = "JSON Parsing Tests"
        if keep_only_first_result_in_set:
            title += ", Pruned"
        else:
            title += ", Full"
        f.write("<H1>%s</H1>\n" % title)
        f.write(
            '<P>Appendix to: seriot.ch <A HREF="http://www.seriot.ch/parsing_json.php">Parsing JSON is a Minefield</A> http://www.seriot.ch/parsing_json.php</P>\n'
        )
        f.write("<PRE>%s</PRE>\n" % strftime("%Y-%m-%d %H:%M:%S"))

        f.write("""
            <H4>Contents</H4>
            <OL>
                <LI><A HREF="#color_scheme">Color Scheme</A></LI>
                <LI><A HREF="#all_results">Full Results</A></LI>
                <LI>
                    <A HREF="#results_by_parser">Results by Parser</A>
                    <UL>
        """)
        for i, prog in enumerate(prog_names):
            f.write('    <LI><A HREF="#%d">%s</A>\n' % (i, prog))
        f.write("""
                    </UL>
                </LI>
            </OL>
        """)

        f.write("""
            <A NAME="color_scheme"></A>
            <H4>1. Color scheme:</H4>
            <TABLE>
                <TR><TD class="EXPECTED_RESULT">expected result</TD></TR>
                <TR><TD class="SHOULD_HAVE_PASSED">parsing should have succeeded but failed</TD></TR>
                <TR><TD class="SHOULD_HAVE_FAILED">parsing should have failed but succeeded</TD></TR>
                <TR><TD class="IMPLEMENTATION_PASS">result undefined, parsing succeeded</TD></TR>
                <TR><TD class="IMPLEMENTATION_FAIL">result undefined, parsing failed</TD></TR>
                <TR><TD class="CRASH">parser crashed</TD></TR>
                <TR><TD class="TIMEOUT">timeout</TD></TR>
            </TABLE>
        """)

        ###

        f.write('<A NAME="all_results"></A>\n')
        f.write("<H4>2. Full Results</H4>\n")
        f.write("<TABLE>\n")

        f.write("    <TR>\n")
        f.write("        <TH></TH>\n")
        for lib in libs:
            f.write('        <TH class="vertical"><DIV>%s</DIV></TH>\n' % lib)
        f.write("        <TH></TH>\n")
        f.write("    </TR>\n")

        for k, file_set in tests_with_same_results:
            ordered_file_set = list(file_set)
            ordered_file_set.sort()

            if keep_only_first_result_in_set:
                ordered_file_set = [ordered_file_set[0]]

            for path in [path for path in ordered_file_set if os.path.exists(path)]:
                f.write("    <TR>\n")
                f.write("        <TD>%s</TD>" % os.path.basename(path))

                status_for_lib = status_for_lib_for_file[path]
                bytes = open(path, "rb").read()

                for lib in libs:
                    if lib in status_for_lib:
                        status = status_for_lib[lib]
                        f.write('        <TD class="%s">%s</TD>' % (status, ""))
                    else:
                        f.write('        <TD class="EXPECTED_RESULT"></TD>')
                f.write("        <TD>%s</TD>" % f_underline_non_printable_bytes(bytes))
                f.write("    </TR>")

        f.write("</TABLE>\n")

        ###

        f.write('<A NAME="results_by_parser"></A>\n')
        f.write("<H4>3. Results by Parser</H4>")
        for i, prog in enumerate(prog_names):
            url = programs[prog]["url"]
            f.write('<A NAME="%d"></A>' % i)
            if len(url) > 0:
                f.write('<H4><A HREF="%s">%s</A></H4>\n' % (url, prog))
            else:
                f.write("<H4>%s</H4>\n" % prog)

            ###

            if prog not in status_for_path_for_lib:
                continue
            status_for_path = status_for_path_for_lib[prog]

            paths = list(status_for_path.keys())
            paths.sort()

            f.write("<TABLE>\n")

            f.write("    <TR>\n")
            f.write("        <TH></TH>\n")
            f.write('        <TH class="space"><DIV></DIV></TH>\n')
            f.write("        <TH></TH>\n")
            f.write("    </TR>\n")

            for path in paths:
                f.write("    <TR>\n")
                f.write("        <TD>%s</TD>" % os.path.basename(path))

                status_for_lib = status_for_lib_for_file[path]
                if os.path.exists(path):
                    bytes = open(path, "rb").read()
                else:
                    bytes = [ord(x) for x in "(MISSING FILE)"]

                if prog in status_for_lib:
                    status = status_for_lib[prog]
                    f.write('        <TD class="%s">%s</TD>' % (status, ""))
                else:
                    f.write("        <TD></TD>")
                f.write("        <TD>%s</TD>" % f_underline_non_printable_bytes(bytes))
                f.write("    </TR>")

            f.write("</TABLE>\n")

        ###

        f.write("""
            </BODY>
            </HTML>
        """)
    if os.path.exists("/usr/bin/open"):
        os.system('/usr/bin/open "%s"' % report_path)


###

if __name__ == "__main__":
    restrict_to_path = None
    """
    if len(sys.argv) == 2:
        restrict_to_path = os.path.join(BASE_DIR, sys.argv[1])
        if not os.path.exists(restrict_to_path):
            print("-- file does not exist:", restrict_to_path)
            sys.exit(-1)
    """

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("restrict_to_path", nargs="?", type=str, default=None)
    parser.add_argument(
        "--filter",
        dest="restrict_to_program",
        type=argparse.FileType("r"),
        default=None,
    )

    args = parser.parse_args()

    # args.restrict_to_program = ["C ConcreteServer"]

    run_tests(args.restrict_to_path, args.restrict_to_program)

    generate_report(
        os.path.join(constants.BASE_DIR, "results/parsing.html"),
        keep_only_first_result_in_set=False,
    )
    generate_report(
        os.path.join(constants.BASE_DIR, "results/parsing_pruned.html"),
        keep_only_first_result_in_set=True,
    )

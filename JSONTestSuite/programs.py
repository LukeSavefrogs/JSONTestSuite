""" List of programs supported by the test suite. """

import os
from . import constants


programs = {
    "Bash JSON.sh 2016-08-12": {
        "url": "https://github.com/dominictarr/JSON.sh",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_Bash_JSON/JSON.sh")],
        "use_stdin": True,
    },
    "R rjson": {
        "url": "",
        "commands": [
            "/usr/local/bin/RScript",
            os.path.join(constants.PARSERS_DIR, "test_rjson.r"),
        ],
    },
    "R jsonlite": {
        "url": "",
        "commands": [
            "/usr/local/bin/RScript",
            os.path.join(constants.PARSERS_DIR, "test_jsonlite.r"),
        ],
    },
    "Obj-C JSONKit": {
        "url": "",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_JSONKit/bin/test-JSONKit")],
    },
    "Obj-C Apple NSJSONSerialization": {
        "url": "",
        "commands": [
            os.path.join(
                constants.PARSERS_DIR, "test_ObjCNSJSONSerializer/bin/test_ObjCNSJSONSerializer"
            )
        ],
    },
    "Obj-C TouchJSON": {
        "url": "https://github.com/TouchCode/TouchJSON",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_TouchJSON/bin/test_TouchJSON")],
    },
    "Obj-C SBJSON 4.0.3": {
        "url": "https://github.com/stig/json-framework",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_SBJSON_4_0_3/bin/test_sbjson")],
    },
    "Obj-C SBJSON 4.0.4": {
        "url": "https://github.com/stig/json-framework",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_SBJSON_4_0_4/bin/test_sbjson")],
    },
    "Obj-C SBJson 5.0.0": {
        "url": "https://github.com/stig/json-framework",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_SBJson_5_0_0/bin/test_sbjson")],
    },
    "Go 1.7.1": {
        "url": "",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_go/test_json")],
    },
    "Zig 0.8.0-dev.1354+081698156": {
        "url": "",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_zig/test_json")],
    },
    "Free Pascal fcl-json": {
        "url": "",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_fpc/test_json")],
    },
    "Xidel Internet Tools": {
        "url": "http://www.videlibri.de/xidel.html",
        "commands": ["/usr/bin/env", "xidel", "--input-format=json-strict", "-e=."],
    },
    "Lua JSON 20160916.19": {
        "url": "http://regex.info/blog/lua/json",
        "commands": [
            "/usr/local/bin/lua",
            os.path.join(constants.PARSERS_DIR, "test_Lua_JSON/test_JSON.lua"),
        ],
    },
    "Lua dkjson": {
        "url": "http://dkolf.de/src/dkjson-lua.fsl/home",
        "commands": [
            "/usr/local/bin/lua",
            os.path.join(constants.PARSERS_DIR, "test_dkjson.lua"),
        ],
    },
    "Ruby": {
        "url": "",
        "commands": ["/usr/bin/env", "ruby", os.path.join(constants.PARSERS_DIR, "test_json.rb")],
    },
    "Ruby regex": {
        "url": "",
        "commands": [
            "/usr/bin/env",
            "ruby",
            os.path.join(constants.PARSERS_DIR, "test_json_re.rb"),
        ],
    },
    "Ruby Yajl": {
        "url": "https://github.com/brianmario/yajl-ruby",
        "commands": ["/usr/bin/env", "ruby", os.path.join(constants.PARSERS_DIR, "test_yajl.rb")],
    },
    "Ruby Oj (strict mode)": {
        "url": "https://github.com/ohler55/oj",
        "commands": [
            "/usr/bin/env",
            "ruby",
            os.path.join(constants.PARSERS_DIR, "test_oj_strict.rb"),
        ],
    },
    "Ruby Oj (compat mode)": {
        "url": "https://github.com/ohler55/oj",
        "commands": [
            "/usr/bin/env",
            "ruby",
            os.path.join(constants.PARSERS_DIR, "test_oj_compat.rb"),
        ],
    },
    "Crystal": {
        "url": "https://github.com/crystal-lang/crystal",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_json_cr")],
    },
    "JavaScript": {
        "url": "",
        "commands": ["/usr/local/bin/node", os.path.join(constants.PARSERS_DIR, "test_json.js")],
    },
    "Python 2.7.10": {
        "url": "",
        "commands": ["/usr/bin/python", os.path.join(constants.PARSERS_DIR, "test_json.py")],
    },
    "Python 3.5.2": {
        "url": "",
        "commands": [
            "/usr/bin/env",
            "python3.5",
            os.path.join(constants.PARSERS_DIR, "test_json.py"),
        ],
    },
    "Python cjson 1.10": {  # pip install cjson
        "url": "https://pypi.python.org/pypi/python-cjson",
        "commands": ["/usr/bin/python", os.path.join(constants.PARSERS_DIR, "test_cjson.py")],
    },
    "Python ujson 1.35": {  # pip install ujson
        "url": "https://pypi.python.org/pypi/ujson",
        "commands": ["/usr/bin/python", os.path.join(constants.PARSERS_DIR, "test_ujson.py")],
    },
    "Python simplejson 3.10": {  # pip install simplejson
        "url": "https://pypi.python.org/pypi/simplejson",
        "commands": [
            "/usr/bin/python",
            os.path.join(constants.PARSERS_DIR, "test_simplejson.py"),
        ],
    },
    "Python demjson 2.2.4": {  # pip install demjson
        "url": "https://pypi.python.org/pypi/demjson",
        "commands": ["/usr/bin/python", os.path.join(constants.PARSERS_DIR, "test_demjson.py")],
    },
    "Python demjson 2.2.4 (py3)": {  # pip install demjson
        "url": "https://pypi.python.org/pypi/demjson",
        "commands": [
            "/usr/bin/env",
            "python3.5",
            os.path.join(constants.PARSERS_DIR, "test_demjson.py"),
        ],
    },
    "Python demjson 2.2.4 (jsonlint)": {  # pip install demjson
        "url": "https://pypi.python.org/pypi/demjson",
        "commands": [
            "/usr/bin/env",
            "jsonlint",
            "--quiet",
            "--strict",
            "--allow=non-portable,duplicate-keys,zero-byte",
        ],
    },
    "Perl Cpanel::JSON::XS": {
        "url": "https://metacpan.org/pod/Cpanel::JSON::XS",
        "commands": [
            "/usr/bin/perl",
            os.path.join(constants.PARSERS_DIR, "test_cpanel_json_xs.pl"),
        ],
    },
    "Perl JSON::Parse": {
        "url": "https://metacpan.org/pod/JSON::Parse",
        "commands": ["/usr/bin/perl", os.path.join(constants.PARSERS_DIR, "test_json_parse.pl")],
    },
    "Perl JSON::PP": {  # part of default install in perl >= v5.14
        "url": "https://metacpan.org/pod/JSON::PP",
        "commands": ["/usr/bin/perl", os.path.join(constants.PARSERS_DIR, "test_json_pp.pl")],
    },
    "Perl JSON::SL": {
        "url": "https://metacpan.org/pod/JSON::SL",
        "commands": ["/usr/bin/perl", os.path.join(constants.PARSERS_DIR, "test_json_sl.pl")],
    },
    "Perl JSON::Tiny": {
        "url": "https://metacpan.org/pod/JSON::Tiny",
        "commands": ["/usr/bin/perl", os.path.join(constants.PARSERS_DIR, "test_json_tiny.pl")],
    },
    "Perl JSON::XS": {
        "url": "https://metacpan.org/pod/JSON::XS",
        "commands": ["/usr/bin/perl", os.path.join(constants.PARSERS_DIR, "test_json_xs.pl")],
    },
    "Perl MarpaX::ESLIF::ECMA404": {
        "url": "http://metacpan.org/pod/MarpaX::ESLIF::ECMA404",
        "commands": [
            "/usr/bin/perl",
            os.path.join(constants.PARSERS_DIR, "test_marpax_eslif_ecma404.pl"),
        ],
    },
    "Perl Mojo::JSON": {
        "url": "http://metacpan.org/pod/Mojo::JSON",
        "commands": ["/usr/bin/perl", os.path.join(constants.PARSERS_DIR, "test_mojo_json.pl")],
    },
    "Perl Pegex::JSON": {
        "url": "http://metacpan.org/pod/Pegex::JSON",
        "commands": ["/usr/bin/perl", os.path.join(constants.PARSERS_DIR, "test_pegex_json.pl")],
    },
    "PHP 5.5.36": {
        "url": "",
        "commands": ["/usr/bin/php", os.path.join(constants.PARSERS_DIR, "test_json.php")],
    },
    "Swift Freddy 2.1.0": {
        "url": "",
        "commands": [
            os.path.join(constants.PARSERS_DIR, "test_Freddy_2_1_0/bin/test_Freddy_2_1_0")
        ],
    },
    "Swift Freddy 20160830": {
        "url": "",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_Freddy_20160830/bin/test_Freddy")],
    },
    "Swift Freddy 20161018": {
        "url": "",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_Freddy_20161018/bin/test_Freddy")],
    },
    "Swift Freddy 20170118": {
        "url": "",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_Freddy_20170118/bin/test_Freddy")],
    },
    "Swift PMJSON 1.1.0": {
        "url": "https://github.com/postmates/PMJSON",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_PMJSON_1_1_0/bin/test_PMJSON")],
    },
    "Swift PMJSON 1.2.0": {
        "url": "https://github.com/postmates/PMJSON",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_PMJSON_1_2_0/bin/test_PMJSON")],
    },
    "Swift PMJSON 1.2.1": {
        "url": "https://github.com/postmates/PMJSON",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_PMJSON_1_2_1/bin/test_PMJSON")],
    },
    "Swift STJSON": {
        "url": "",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_STJSON/bin/STJSON")],
    },
    "Swift Apple JSONSerialization": {
        "url": "",
        "commands": [
            os.path.join(
                constants.PARSERS_DIR,
                "test-AppleJSONSerialization/bin/test-AppleJSONSerialization",
            )
        ],
    },
    "C pdjson 20170325": {
        "url": "https://github.com/skeeto/pdjson",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_pdjson/bin/test_pdjson")],
    },
    "C jsmn": {
        "url": "https://github.com/zserge/jsmn",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_jsmn/bin/test_jsmn")],
    },
    "C jansson": {
        "url": "",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_jansson/bin/test_jansson")],
    },
    "C JSON Checker": {
        "url": "http://www.json.org/JSON_checker/",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_jsonChecker/bin/jsonChecker")],
    },
    "C JSON Checker 2": {
        "url": "",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_jsonChecker2/bin/jsonChecker2")],
    },
    "C JSON Checker 20161111": {
        "url": "https://github.com/douglascrockford/JSON-c",
        "commands": [
            os.path.join(
                constants.PARSERS_DIR, "test_jsonChecker20161111/bin/jsonChecker20161111"
            )
        ],
    },
    "C++ sajson 20170724": {
        "url": "https://github.com/chadaustin/sajson",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_sajson_20170724/bin/test_sajson")],
    },
    "C ccan": {
        "url": "",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_ccan_json/bin/test_ccan")],
    },
    "C cJSON 20160806": {
        "url": "https://github.com/DaveGamble/cJSON",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_cJSON_20160806/bin/test_cJSON")],
    },
    "C cJSON 1.7.3": {
        "url": "https://github.com/DaveGamble/cJSON",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_cJSON_1_7_3/bin/test_cJSON")],
    },
    "C JSON-C": {
        "url": "https://github.com/json-c/json-c",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_json-c/bin/test_json-c")],
    },
    "C JSON Parser by udp": {
        "url": "https://github.com/udp/json-parser",
        "commands": [
            os.path.join(constants.PARSERS_DIR, "test_json-parser/bin/test_json-parser")
        ],
    },
    "C++ nlohmann JSON 20190718": {
        "url": "https://github.com/nlohmann/json/",
        "commands": [
            os.path.join(
                constants.PARSERS_DIR, "test_nlohmann_json_20190718/bin/test_nlohmann_json"
            )
        ],
    },
    "C++ RapidJSON 20170724": {
        "url": "https://github.com/miloyip/rapidjson",
        "commands": [
            os.path.join(constants.PARSERS_DIR, "test_rapidjson_20170724/bin/test_rapidjson")
        ],
    },
    "Rust json-rust": {
        "url": "https://github.com/maciejhirsz/json-rust",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_json-rust/target/debug/tj")],
    },
    "Rust rustc_serialize::json": {
        "url": "https://doc.rust-lang.org/rustc-serialize/rustc_serialize/json/index.html",
        "commands": [
            os.path.join(constants.PARSERS_DIR, "test_json-rustc_serialize/rj/target/debug/rj")
        ],
    },
    "Rust serde_json": {
        "url": "https://github.com/serde-rs/json",
        "commands": [
            os.path.join(constants.PARSERS_DIR, "test_json-rust-serde_json/rj/target/debug/rj")
        ],
    },
    "Java json-simple 1.1.1": {
        "url": "",
        "commands": [
            "/usr/bin/java",
            "-jar",
            os.path.join(
                constants.PARSERS_DIR, "test_java_simple_json_1_1_1/TestJSONParsing.jar"
            ),
        ],
    },
    "Java org.json 2016-08-15": {
        "url": "https://github.com/stleary/JSON-java",
        "commands": [
            "/usr/bin/java",
            "-jar",
            os.path.join(constants.PARSERS_DIR, "test_java_org_json_2016_08/TestJSONParsing.jar"),
        ],
    },
    "Java gson 2.7": {
        "url": "",
        "commands": [
            "/usr/bin/java",
            "-jar",
            os.path.join(constants.PARSERS_DIR, "test_java_gson_2_7/TestJSONParsing.jar"),
        ],
    },
    "Java BFO v1": {
        "url": "https://github.com/faceless2/json",
        "commands": [
            "/usr/bin/java",
            "-jar",
            os.path.join(constants.PARSERS_DIR, "test_java_bfo/TestJSONParsing.jar"),
        ],
    },
    "Java com.leastfixedpoint.json 1.0": {
        "url": "",
        "commands": [
            "/usr/bin/java",
            "-jar",
            os.path.join(
                constants.PARSERS_DIR,
                "test_java_com_leastfixedpoint_json_1_0/TestJSONParsing.jar",
            ),
        ],
    },
    "Java Jackson 2.8.4": {
        "url": "",
        "commands": [
            "/usr/bin/java",
            "-jar",
            os.path.join(constants.PARSERS_DIR, "test_java_jackson_2_8_4/TestJSONParsing.jar"),
        ],
    },
    "Scala Dijon 0.3.0": {
        "url": "",
        "commands": [
            "/usr/bin/java",
            "-jar",
            os.path.join(
                constants.PARSERS_DIR,
                "test_scala_dijon_0.3.0/target/scala-2.13/TestJSONParsing.jar",
            ),
        ],
    },
    "Java Mergebase Java2Json 2019.09.09": {
        "url": "https://github.com/mergebase/Java2Json",
        "commands": [
            "/usr/bin/java",
            "-jar",
            os.path.join(
                constants.PARSERS_DIR, "test_java_mergebase_json_2019_09_09/TestJSONParsing.jar"
            ),
        ],
    },
    "Java nanojson 1.0": {
        "url": "",
        "commands": [
            "/usr/bin/java",
            "-jar",
            os.path.join(constants.PARSERS_DIR, "test_java_nanojson_1_0/TestJSONParsing.jar"),
        ],
    },
    "Java nanojson 1.1": {
        "url": "",
        "commands": [
            "/usr/bin/java",
            "-jar",
            os.path.join(constants.PARSERS_DIR, "test_java_nanojson_1_1/TestJSONParsing.jar"),
        ],
    },
    "Java Actson 1.2.0": {
        "url": "https://github.com/michel-kraemer/actson",
        "commands": [
            "/usr/bin/java",
            "-jar",
            os.path.join(constants.PARSERS_DIR, "test_java_actson_1_2_0/TestJSONParsing.jar"),
        ],
    },
    "Haskell Aeson 0.11.2.1": {
        "url": "https://github.com/bos/aeson",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_haskell-aeson/testaeson")],
    },
    "OCaml Yojson": {
        "url": "https://github.com/mjambon/yojson",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_ocaml-yojson/testyojson")],
    },
    "OCaml Orsetto": {
        "url": "https://bitbucket.org/jhw/orsetto",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_ocaml_orsetto/test_orsetto_json")],
    },
    "Qt JSON": {"url": "", "commands": [os.path.join(constants.PARSERS_DIR, "test_qt/test_qt")]},
    "C ConcreteServer": {
        "url": " https://github.com/RaphaelPrevost/ConcreteServer",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_ConcreteServer/json_checker")],
    },
    "Squeak JSON-tonyg": {
        "url": "http://www.squeaksource.com/JSON.html",
        "commands": [
            os.path.join(
                constants.PARSERS_DIR, "test_Squeak_JSON_tonyg/Squeak.app/Contents/MacOS/Squeak"
            ),
            "-headless",  # <--optional
            os.path.join(
                constants.PARSERS_DIR, "test_Squeak_JSON_tonyg/Squeak5.1-16549-32bit.image"
            ),
            "test_JSON.st",
        ],
    },
    ".NET Newtonsoft.Json 12.0.3": {
        "url": "http://www.newtonsoft.com/json",
        "setup": [
            "dotnet",
            "build",
            "--configuration",
            "Release",
            os.path.join(constants.PARSERS_DIR, "test_dotnet_newtonsoft/app.csproj"),
        ],
        "commands": [
            "dotnet",
            os.path.join(
                constants.PARSERS_DIR, "test_dotnet_newtonsoft/bin/Release/net5.0/app.dll"
            ),
        ],
    },
    ".NET System.Text.Json 5.0.0": {
        "url": "https://docs.microsoft.com/en-us/dotnet/api/system.text.json",
        "setup": [
            "dotnet",
            "build",
            "--configuration",
            "Release",
            os.path.join(constants.PARSERS_DIR, "test_dotnet_system_text_json/app.csproj"),
        ],
        "commands": [
            "dotnet",
            os.path.join(
                constants.PARSERS_DIR, "test_dotnet_system_text_json/bin/Release/net5.0/app.dll"
            ),
        ],
    },
    "Elixir Json": {
        "url": "https://github.com/cblage/elixir-json",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_elixir_json/test_elixir_json")],
    },
    "Elixir ExJSON": {
        "url": "https://github.com/guedes/exjson",
        "commands": [
            os.path.join(constants.PARSERS_DIR, "test_elixir_exjson/test_elixir_exjson")
        ],
    },
    "Elixir Poison": {
        "url": "https://github.com/devinus/poison",
        "commands": [
            os.path.join(constants.PARSERS_DIR, "test_elixir_poison/test_elixir_poison")
        ],
    },
    "Elixir Jason": {
        "url": "https://github.com/michalmuskala/jason",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_elixir_jason/test_elixir_jason")],
    },
    "Nim": {
        "url": "http://nim-lang.org",
        "commands": [os.path.join(constants.PARSERS_DIR, "test_nim/test_json")],
    },
    "Swift JSON 20170522": {
        "url": "https://github.com/owensd/json-swift",
        "commands": [
            os.path.join(constants.PARSERS_DIR, "test_json_swift_20170522/bin/json_swift")
        ],
    },
    "C++ nlohmann JSON 20190718": {
        "url": "https://github.com/nlohmann/json",
        "commands": [
            os.path.join(
                constants.PARSERS_DIR, "test_nlohmann_json_20190718/bin/test_nlohmann_json"
            )
        ],
    },
}


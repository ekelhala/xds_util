import os, time, sys, json

firmware_versions = {}
path = ""

try:
    with open("config.json") as config:
        file_contents = config.read()
        try:
            config_obj = json.loads(file_contents)
            firmware_versions = config_obj["firmwareBinaries"]
            path = config_obj["xdsfuPath"]
        except json.JSONDecodeError:
            print("ERROR: Invalid JSON")
        else:
            command = sys.argv[1]
            if command in firmware_versions:
                os.system("{dir}xdsdfu -m".format(dir=path))
                time.sleep(1)
                os.system("{dir}xdsdfu -f {firmware_file} -r".format(dir=path, firmware_file=firmware_versions[command]))
            else:
                print("Invalid argument, possible values are: {keys}".format(keys=" ".join(firmware_versions.keys())))
except FileNotFoundError:
    print("ERROR: Missing config.json")
import subprocess
import json

def run_command(command):
    try:
        output = subprocess.check_output(command, shell=True)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

def dump_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    command = "ping -c4 google.com"
    output = run_command(command)
    dump_to_json({"output": output.split('\n')}, "output.json")


if __name__ == "__main__":
    main()
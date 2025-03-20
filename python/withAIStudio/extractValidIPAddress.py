import re
import os

def extract_ipv4_from_files(directory):
    """
    Extracts valid IPv4 addresses from all files in a given directory and its subdirectories.

    Args:
        directory: The path to the directory to search.

    Returns:
        A set of unique IPv4 addresses found.
    """

    ipv4_regex = r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
    ipv4_addresses = set()

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    file_content = f.read()
                    matches = re.findall(ipv4_regex, file_content)
                    ipv4_addresses.update(matches)

            except (FileNotFoundError, PermissionError, UnicodeDecodeError) as e:
                print(f"Error processing {file_path}: {e}")

    return ipv4_addresses

def main():
    # directory = input("Enter the directory path: ")

    # if not os.path.isdir(directory):
    #     print("Invalid directory path.")
    #     return

    directory = '.'
    found_ips = extract_ipv4_from_files(directory)

    if found_ips:
        print("Found IPv4 addresses:")
        for ip in sorted(found_ips):
            print(ip)
    else:
        print("No IPv4 addresses found.")

if __name__ == "__main__":
    main()

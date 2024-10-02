"""
Usage:
Program_name <directory_path>

"""
import os
import hashlib

def calculate_checksum(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def check_duplicates(directory):
    file_checksums = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            checksum = calculate_checksum(file_path)
            if checksum in file_checksums:
                print(f"Duplicate file found: {file_path} (matches {file_checksums[checksum]})")
            else:
                file_checksums[checksum] = file_path


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python dedupe.py <directory>")
        sys.exit(1)
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print("Error: Please provide a valid directory path.")
        sys.exit(1)
    check_duplicates(directory)
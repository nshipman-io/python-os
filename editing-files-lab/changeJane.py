#!/usr/bin/env python3

import sys
import subprocess


def readFile(filename):
    files = []
    try:
        with open(filename, "r") as f:
            for line in f:
                files.append(line.strip())
        f.close()
    except FileNotFoundError:
        print("File: {} was not found. Please ensure file exists".format(filename))

    if files:
        return files
    return None

def renameFiles(files):
    for oldFileName in files:
        newFileName = oldFileName.replace("jane","jdoe")
        result = subprocess.run(["mv", oldFileName, newFileName], stderr=subprocess.DEVNULL)
        if result.returncode != 0:
            print("{} not moved. Check if the file exists".format(oldFileName))

def main():
    filename = sys.argv[1]
    files = readFile(filename)
    if files:
        renameFiles(files)
    else:
        print("No files to rename. Ending Program.")
        sys.exit(0)

if __name__ == "__main__":
    main()

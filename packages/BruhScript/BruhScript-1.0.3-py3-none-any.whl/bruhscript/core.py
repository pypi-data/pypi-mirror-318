import sys
import os

def interpret_bruhscript(code):
    print("👊 BruhScript is interpreting the code...")
    for line in code.splitlines():
        print(f"Processing line: {line.strip()}")

def main():
    if len(sys.argv) < 2:
        print("Usage: bruhscript <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    with open(file_path, "r") as file:
        code = file.read()

    interpret_bruhscript(code)

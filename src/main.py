import uuid

from src.dataclasses import *
from src.file_system import *
from src.output import *
from src.parsing import *



def main():
    print("Starting manual test for SuccurIndex")
    file_entry = read_toml_file_entry("7c9f4a03-b75f-4b14-bcb7-389208b3aab0")
    print_file_entry(file_entry, ["name", "links"])

    print("Test concluded")

if __name__ == "__main__":
    main()

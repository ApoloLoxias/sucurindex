import uuid

from src.dataclasses import *
from src.file_system import *
from src.output import *
from src.parsing import *



def main():
    print("Starting manual test for SuccurIndex")
    meta = read_file_metadata("uv.lock")
    file_entry = FileEntry(
        path = "uv.lock",
        size = meta["size"]
    )

    burn_toml_file_entry(file_entry)

    print(str(read_toml_file_entry(str(file_entry.id))))

    print("Test concluded")

if __name__ == "__main__":
    main()

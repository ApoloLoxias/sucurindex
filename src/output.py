import os

from src.dataclasses.file_entry import FileEntry
from src.parsing import write_toml_file_entry


def burn_toml_file_entry(file_entry: FileEntry) -> str:
    file_path = os.path.abspath(f"./metadata/{file_entry.id}.toml")
    content = write_toml_file_entry(file_entry)

    try:
        with open(file_path, mode="w") as file:
            file.write(content)
        return f"Successfully wrote '{file_entry.name}'/{file_entry.id} FileEntry to '{file_path}'"
    except Exception as e:
        return f"Failed to write '{file_entry.name}'/{file_entry.id} FileEntry to '{file_path}'"

def print_file_entry(file_entry: FileEntry, tags: list[str]=None) -> str:
    output = []
    invalid_tags = []
    valid_tags = [
            "name",
            "id",
            "description",
            "tags",
            "links",
            "mtime",
            "size",
        ]

    if not tags:
        print(file_entry)
        return f"Printed FileEntry '{file_entry.name}'/{file_entry.id} to console"

    invalid_tags = [t for t in tags if t not in valid_tags]
    if invalid_tags != []:
        print(f"Invalid tag(s): {invalid_tags}, valid tags include {valid_tags}")
        return f"Invalid tag(s): {invalid_tags}"

    output = [f"{t}: {getattr(file_entry, t)}" for t in tags]

    for line in output:
        print(line)
    return f"Printed FileEntry '{file_entry.name}'/{file_entry.id}'s {tags} to console"

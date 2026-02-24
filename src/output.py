import os

from src.dataclasses import FileEntry
from parsing import write_toml_file_entry


def burn_toml_file_entry(file_entry: FileEntry) -> str:
    file_path = os.abspath(f"./metadata/{file_entry.id}.toml")
    content = write_toml_file_entry(file_entry)

    try:
        with open(file_path, mode="w") as file:
            file.write(content)
       return f"Successfully wrote '{file_entry.name}'/{file_entry.id} FileEntry to '{file_path}'"
    except Exception as e:
        return f"Failed to write '{file_entry.name}'/{file_entry.id} FileEntry to '{file_path}'"

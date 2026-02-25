import os

from src.dataclasses import FileEntry
from src.parsing import read_toml_file_entry


def read_file_metadata(path: str) -> dict:
    file_path = os.path.abspath(path)

    if not os.path.isfile(file_path): raise FileNotFoundError(f"{path} not found or not a file")

    stat_result = os.stat(file_path)
    result = {
        "mtime": stat_result.st_mtime,
        "size": stat_result.st_size
    }

    return result

def list_file_entries() -> list[FileEntry]:
    files = [f for f in os.listdir(os.path.abspath("./metadata")) if f.endswith(".toml")]
    ids = [file[:-5] for file in files]
    file_entries = [read_toml_file_entry(id) for id in ids]
    return file_entries
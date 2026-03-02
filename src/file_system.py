import os

from src.dataclasses import FileEntry
from src.parsing import read_toml_file_entry
from src.config import get_pstorage


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
    from src.parsing import read_toml_file_entry

    files = [f for f in os.listdir(get_pstorage()) if f.endswith(".toml")]
    ids = [file[:-5] for file in files]
    file_entries = [read_toml_file_entry(id, skip_path_validation=True) for id in ids]
    
    return file_entries



def check_entries() -> dict[str, list[FileEntry]]:
    directory = get_pstorage()
    output = {"changed": [], "missing": [], "unaltered": []}

    for file in os.listdir(directory):
        path = os.path.join(get_pstorage(), file)
        file_entry = read_toml_file_entry(file[:-5], skip_path_validation=True)

        if not os.path.exists(os.path.abspath(file_entry.path)):
            output["missing"].append(file_entry)
            continue
        else:
            metadata = read_file_metadata(os.path.abspath(file_entry.path))
            has_changed = False
            for k, v in metadata.items():
                if getattr(file_entry, k) != v:
                    has_changed = True
                    break
            if has_changed:
                output["changed"].append(file_entry)
            else:
                output["unaltered"].append(file_entry)

    return output



def slither(rootpath: str) -> list[str]:
    absrootpath = os.path.abspath(rootpath)
    paths = []

    entries = os.walk(absrootpath)
    for dirpath, dirname, filenames in entries:
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            paths.append(os.path.abspath(path))

    return paths
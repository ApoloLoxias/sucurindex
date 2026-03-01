import os
import tomlkit

from uuid import UUID

from src.dataclasses.file_entry import FileEntry
from src.config import get_pstorage



def read_toml_file_entry(id: str) -> FileEntry:
    path = os.path.join(get_pstorage(), f"{id}.toml")

    if not os.path.exists(path):
        raise FileNotFoundError(f"{id} FileEntry not found")
    
    with open(path, "r") as f:
        toml = tomlkit.load(f)
    file_path = toml.get("path")
    name = toml.get("name")
    description = toml.get("description", "")
    tags = list(toml.get("tags", []))
    links = [UUID(link) for link in toml.get("links", [])] if toml.get("links", []) else []
    mtime = toml.get("mtime")
    size = toml.get("size")
    uuid = UUID(toml.get("id"))
    missing = toml.get("missing")

    file_entry = FileEntry(
        path=file_path,
        name=name,
        description=description,
        tags=tags,
        links=links,
        id=uuid,
        mtime=mtime,
        size=size,
        missing=missing,
    )
    return file_entry



def write_toml_file_entry(file_entry: FileEntry) -> str:
    dic = {
        "path": file_entry.path,
        "name": file_entry.name,
        "description": file_entry.description if file_entry.description else "",
        "tags": file_entry.tags if file_entry.tags else [],
        "links": [str(link) for link in file_entry.links] if file_entry.links else [],
        "id": str(file_entry.id),
        "mtime": file_entry.mtime,
        "size": file_entry.size,
        "missing": file_entry.missing
    }
    return tomlkit.dumps(dic)



def filter_single_attribute(universe: list[FileEntry], attr: str, term, debug: bool=False) -> list[FileEntry]:
    output = []

    for fe in universe:
        if debug: print(f"{getattr(fe, attr)} = {term}?")
        if getattr(fe, attr) == term:
            if debug: print("yes")
            output.append(fe)
        else:
            if debug: print("no")
        if debug: print("")

    return output



def filter_list_attribute(universe: list[FileEntry], attr: str, term, debug: bool=False) -> list[FileEntry]:
    output = []

    for fe in universe:
        if debug: print(f"{term} in {getattr(fe, attr)}?")
        if term in getattr(fe, attr):
            if debug: print("yes")
            output.append(fe)
        elif debug: print("no")
        if debug: print("")

    return output



def update_file_entry(file_entry: FileEntry, attributes: dict) -> FileEntry:
    upd_attr = {}

    for attr, val in attributes.items():
        upd_attr[attr] = val
    for attr, val in file_entry.dic().items():
        if attr not in upd_attr.keys():
            upd_attr[attr] = val

    return FileEntry(**upd_attr)



def update_list_attribute(attr: list, item, mode) -> list:
    # Mode accepts "a" for appending and "r" for removing
    new_attr = attr.copy()

    if mode == "a":
        if item not in attr:
            new_attr.append(item)
            return new_attr
    if mode == "r":
        if item in attr:
            new_attr.remove(item)
            return new_attr
    raise Exception(f"invalid mode: '{mode}'")
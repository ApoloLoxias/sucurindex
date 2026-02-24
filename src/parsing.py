import os
import tomlkit

from uuid import UUID

from src.dataclasses.file_entry import FileEntry



def read_toml_file_entry(id: str) -> FileEntry:
    path = os.path.abspath(f"./metadata/{id}.toml")

    if not os.path.exists(path):
        raise FileNotFoundError(f"{id} FileEntry not found")
    
    with open(path, "r") as f:
        toml = tomlkit.load(f)
    file_path = toml.get("path")
    name = toml.get("name")
    description = toml.get("description", "")
    tags = list(toml.get("tags", []))
    links = [UUID(link) for link in toml.get("links", [])]
    mtime = toml.get("mtime")
    size = toml.get("size")
    uuid = UUID(toml.get("id"))

    file_entry = FileEntry(
        path=file_path,
        name=name,
        description=description,
        tags=tags,
        links=links,
        id=uuid,
        mtime=mtime,
        size=size,
    )
    return file_entry

def write_toml_file_entry(file_entry: FileEntry) -> str:
    dic = {
        "path": file_entry.path,
        "name": file_entry.name,
        "description": file_entry.description,
        "tags": file_entry.tags,
        "links": [str(link) for link in file_entry.links],
        "id": str(file_entry.id),
        "mtime": file_entry.mtime,
        "size": file_entry.size,
    }
    return tomlkit.dumps(dic)

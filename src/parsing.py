import os
import tomlkit

from uuid import UUID

from src.dataclasses import FileEntry



def read_toml(id: str) -> FileEntry:
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
    id = UUID(toml.get("id"))

    file_entry = FileEntry(path=file_path, name=name, description=description, tags=tags, links=links, id=id)

    return file_entry



import sys
import argparse
import os

from uuid import UUID

from src.dataclasses import FileEntry
from src.file_system import list_file_entries, read_file_metadata, slither
from src.output import burn_toml_file_entry, delete_file_entry, print_file_entry
from src.parsing import read_toml_file_entry, update_file_entry, update_list_attribute, filter_list_attribute, filter_single_attribute
from src.config import get_pstorage


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
     
    parser_add = subparsers.add_parser("add")
    parser_add.add_argument("path", type=str)
    parser_add.add_argument("--name", type=str, default=None)
    parser_add.add_argument("--description", type=str, default=None)
    parser_add.add_argument("--tags", type=str, default=None, nargs='*')
    parser_add.add_argument("--links", type=str, default=None, nargs='*')

    parser_remove = subparsers.add_parser("remove")
    parser_remove.add_argument("id", type=str)

    parser_list = subparsers.add_parser("list")
    parser_list.add_argument("--id", type=str)
    parser_list.add_argument("--name", type=str)
    parser_list.add_argument("--description", type=str)
    parser_list.add_argument("--tags", type=str, nargs="*")
    parser_list.add_argument("--links", type=str, nargs="*")


    parser_read = subparsers.add_parser("read")
    parser_read.add_argument("id", type=str)

    parser_sync = subparsers.add_parser("sync")
    parser_sync.add_argument("--hard", action="store_true")

    parser_edit = subparsers.add_parser("edit")
    parser_edit.add_argument("--id", type=str)
    parser_edit.add_argument("--name", type=str)
    parser_edit.add_argument("--description", type=str)
    parser_edit.add_argument("--links", type=str, nargs='*')
    parser_edit.add_argument("--alinks", type=str, nargs='*')
    parser_edit.add_argument("--rlinks", type=str, nargs='*')
    parser_edit.add_argument("--tags", type=str, nargs='*')
    parser_edit.add_argument("--atags", type=str, nargs='*')
    parser_edit.add_argument("--rtags", type=str, nargs='*')

    parser_slither = subparsers.add_parser("slither")
    parser_slither.add_argument("path", type=str)

    args = parser.parse_args()

    command = commands[args.command]
    inner_args = vars(args)
    inner_args.pop("command")

    command(**inner_args)



def cmd_add(path: str, name: str, description: str, tags: list[str], links: list[str]):
    norm_path = os.path.abspath(path)
    file_entries = list_file_entries()
    for fe in file_entries:
        if fe.path == norm_path:
            print(f"Artifact at '{path}' already catalogued")
            return f"Artifact at '{path}' already catalogued"

    new_entry = FileEntry(
        path = path,
        name = name,
        description = description,
        tags = tags if tags else None,
        links = [UUID(link) for link in links] if links else None,
    )

    burn_toml_file_entry(new_entry)

    print(f"New entry successfully indexed: {new_entry.id}")
    return f"New entry successfully indexed: {new_entry.id}"



def cmd_remove(id: str):
    confirmation = input(f"Delete the following FileEntry?\n{print_file_entry(read_toml_file_entry(id))}\n[y/N]?")
    if confirmation.lower() == "y":
        uuid = UUID(id)
        print(delete_file_entry(uuid))
    print("Operation cancelled")
    return f"Cancelled removal of FileEntry {id}"

def cmd_list(id, name, description, tags, links):
    params = locals().copy().items()
    fes = list_file_entries()

    for param, value in params:
        if value:
            if isinstance(value, list):
                fes = filter_list_attribute(fes, param, value)
            else:
                fes = filter_single_attribute(fes, param, value)


    for fe in fes:
        print(f"{fe.name} | {fe.id}")
        print(fe.path)
        print(fe.description)
        print("- - - - - - - - - - - ")


def cmd_read(id: str):
    file_entry = read_toml_file_entry(id)
    print_file_entry(file_entry)

def cmd_sync(hard: bool=False):
    entries = list_file_entries()
    missing = []
    ok = []
    changed = []
    for entry in entries:
        if not os.path.isfile(entry.path):
            missing.append(entry)
            if hard:
                uentry = update_file_entry(entry, {"missing": True})
                burn_toml_file_entry(uentry)
        else:
            metadata = read_file_metadata(entry.path)
            if entry.mtime != metadata["mtime"] or entry.size != metadata["size"]:
                changed.append(entry)
                if hard:
                    uentry = update_file_entry(entry, {"mtime": metadata["mtime"], "size": metadata["size"]})
            else: ok.append(entry)

    print(f"Missing: {[(fe.name, fe.id) for fe in missing]}")
    print(f"Changed: {[(fe.name, fe.id) for fe in changed]}")
    print(f"Ok: {[(fe.name, fe.id) for fe in ok]}")
    return {"missing": missing, "changed": changed, "ok": ok}

def cmd_edit(id: str, name: str=None, description: str=None, tags: list[str]=None, links: list[str]=None, atags: list[str]=None, rtags: list[str]=None, alinks: list[str]=None, rlinks: list[str]=None):
    if (tags and (atags or rtags)) or (links and (alinks or rlinks)):
        print("Incompatible tags usage: list attributes must either be specified or have items added and removed, not both")
        return "Incompatible tags usage"

    path = (os.path.join(get_pstorage(), f"{id}.toml"))
    file_entry = read_toml_file_entry(id)
    metadata = read_file_metadata(file_entry.path)

    updated_attributes = {}
    if name: updated_attributes["name"] = name
    if description: updated_attributes["description"] = description
    if tags: updated_attributes["tags"] = tags
    if links: updated_attributes["links"] = links
    updated_attributes["mtime"] = metadata["mtime"]
    updated_attributes["size"] = metadata["size"]

    utags = file_entry.tags
    ulinks = file_entry.links

    if atags:
        for tag in atags:
            utags = update_list_attribute(utags, tag, "a")
    if rtags:
        for tag in rtags:
            utags = update_list_attribute(utags, tag, "r")
    if alinks:
        for link in alinks:
            ulinks = update_list_attribute(ulinks, UUID(link), "a")
    if rlinks:
        for link in rlinks:
            ulinks = update_list_attribute(ulinks, UUID(link), "r")

    if ("tags" not in updated_attributes):
        updated_attributes["tags"] = utags
    if ("links" not in updated_attributes):
        updated_attributes["links"] = ulinks

    updated_file_entry = update_file_entry(file_entry, updated_attributes)
    print(burn_toml_file_entry(updated_file_entry))


def cmd_slither(path: str):
    file_paths = slither(path)
    for path in file_paths: cmd_add(path, None, None, None, None)
    print(f"Done slithering through {path}")
    return




commands = {
    "add": cmd_add,
    "remove": cmd_remove,
    "list": cmd_list,
    "read": cmd_read,
    "sync": cmd_sync,
    "edit": cmd_edit,
    "slither": cmd_slither,
}



if __name__ == "__main__":
    main()




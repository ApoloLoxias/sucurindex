import sys
import argparse
import os

from uuid import UUID

from src.dataclasses import FileEntry
from src.file_system import list_file_entries
from src.output import burn_toml_file_entry, delete_file_entry


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
    parser_list.add_argument("x", type=int)
    parser_list.add_argument("y", type=int)

    parser_read = subparsers.add_parser("read")
    parser_read.add_argument("x", type=int)
    parser_read.add_argument("y", type=int)

    parser_sync = subparsers.add_parser("sync")
    parser_sync.add_argument("x", type=int)
    parser_sync.add_argument("y", type=int)

    parser_edit = subparsers.add_parser("edit")
    parser_edit.add_argument("x", type=int)
    parser_edit.add_argument("y", type=int)

    args = parser.parse_args()

    command = comands[args.command]
    inner_args = vars(args)
    inner_args.pop("command")

    command(**inner_args)



def cmd_add(path: str, name: str, description: str, tags: list[str], links: list[int]):
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
    uuid = UUID(id)
    print(delete_file_entry(uuid))

def cmd_list(x, y):
    print(f"{x}+{y}")

def cmd_read(x, y):
    print(f"{x}-{y}")

def cmd_sync(x,y):
    print(f"{x}{y}")

def cmd_edit(x, y):
    print(f"{y}{x}")

comands = {
    "add": cmd_add,
    "remove": cmd_remove,
    "list": cmd_list,
    "read": cmd_read,
    "sync": cmd_sync,
    "edit": cmd_edit,
}



if __name__ == "__main__":
    main()




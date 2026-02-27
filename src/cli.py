import sys
import argparse



def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    parser_add = subparsers.add_parser("add")
    parser_add.add_argument("x", type=int)
    parser_add.add_argument("y", type=int)

    parser_remove = subparsers.add_parser("remove")
    parser_remove.add_argument("x", type=int)
    parser_remove.add_argument("y", type=int)

    parser_list = subparsers.add_parser("list")
    parser_list.add_argument("x", type=int)
    parser_list.add_argument("y", type=int)

    parser_read = subparsers.add_parser("read")
    parser_read.add_argument("x", type=int)
    parser_read.add_argument("y", type=int)

    parser_sync = subparsers.add_parser("sync")
    parser_sync.add_argument("x", type=int)
    parser_sync.add_argument("y", type=int)

    args = parser.parse_args()

    command = comands[args.command]
    inner_args = vars(args)
    inner_args.pop("command")

    command(**inner_args)



def cmd_add(x, y):
    print(x+y)

def cmd_remove(x, y):
    print(x-y)

def cmd_list(x, y):
    print(f"{x}+{y}")

def cmd_read(x, y):
    print(f"{x}-{y}")

def cmd_sync(x,y):
    print(f"{x}{y}")

comands = {
    "add": cmd_add,
    "remove": cmd_remove,
    "list": cmd_list,
    "read": cmd_read,
    "sync": cmd_sync,
}



if __name__ == "__main__":
    main()




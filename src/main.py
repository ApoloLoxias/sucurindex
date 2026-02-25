import uuid

from src.dataclasses import *
from src.file_system import *
from src.output import *
from src.parsing import *



def main():
    print("Starting manual test for SuccurIndex")
    
    file_entries = list_file_entries()
    print(
        filter_file_entries({"tags": ["beach"]})
    )

    print("Test concluded")

if __name__ == "__main__":
    main()

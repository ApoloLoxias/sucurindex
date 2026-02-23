from uuid import UUID, uuid4
import os


class FileEntry:
    def __init__(self, path:str, name: str=None, description: str="", tags: list[str]=None, links: list[UUID]=None, id: UUID=None) -> None:
        if not os.path.isfile(path): raise Exception("path is not a valid file")
        self.path =  os.path.abspath(path)
        self.name = name if name else os.path.basename(path)
        self.description = description
        self.tags = tags if tags else []
        self.links = links if links else []
        self.id = id if id else uuid4()


    def __repr__(self) -> str:
        return f"FileEntry=(id={self.id}, name={self.name}, description={self.description}, tags={self.tags}, links={self.links})"


    def __str__(self) -> str:
        return(
            f"FileEntry object\n"
            f"Name: {self.name}\n"
            f"ID: {self.id}\n"
            f"Description: {self.description}\n"
            f"Tags: {self.tags}\n"
            f"Links: {self.links}\n"
        )


    def __eq__(self, other):
        return "FileEntry equality not implemented"
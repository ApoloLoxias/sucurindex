from uuid import UUID, uuid4
import os
import datetime

class FileEntry:
    def __init__(
        self,
        path:str,
        name: str=None,
        description: str="",
        tags: list[str]=None,
        links: list[UUID]=None,
        id: UUID=None,
        mtime: float=None,
        size: int=None,
        missing: bool=False,
    ) -> None:

        if not os.path.isfile(path): raise Exception("path is not a valid file")
        self.path =  os.path.abspath(path)
        self.name = name if name else os.path.basename(path)
        self.description = description
        self.tags = tags if tags else []
        self.links = links if links else []
        self.id = id if id else uuid4()
        self.mtime = mtime if mtime else os.stat(self.path).st_mtime
        self.size = size if size else os.stat(self.path).st_size
        self.missing = missing

    def __repr__(self) -> str:
        return f"FileEntry=(id={self.id}, name={self.name}, path={self.path}, description={self.description}, tags={self.tags}, links={self.links}, mtime={self.mtime}, size={self.size}, missing={self.missing})"


    def __str__(self) -> str:
        return(
            f"FileEntry object\n"
            f"Name: {self.name}\n"
            f"ID: {self.id}\n"
            f"Path: {self.path}\n"
            f"Description: {self.description}\n"
            f"Tags: {self.tags}\n"
            f"Links: {self.links}\n"
            f"Mtime: {datetime.datetime.fromtimestamp(self.mtime)}\n"
            f"Size: {self.size}"
            f"Missing: {self.missing}"
        )


    def __eq__(self, other):
        return "FileEntry equality not implemented"

    
    def dic(self):
        dic = {
            "path": self.path,
            "name": self.name,
            "id": self.id,
            "description": self.description,
            "tags": self.tags,
            "links": self.links,
            "mtime": self.mtime,
            "size": self.size,
            "missing": self.missing,
        }
        return dic
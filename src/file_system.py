import os

def read_file_metadata(path: str) -> dict:
    file_path = os.abspath(path)

    if not os.isfile(file_path): raise FileNotFoundError(f"{path} not found or not a file")

    stat_result = os.stat(file_path)
    result = {
        "mtime": stat_result.st_mtime,
        "size": stat_result.st_size
    }
    
    return result
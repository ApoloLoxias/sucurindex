# Tests for sucurindex core logical functions
# Run from sucurindex/ with: uv run python -m pytest test_logic.py

import os
import tempfile
import uuid

from src.dataclasses.file_entry import FileEntry
from src.parsing import (
    read_toml_file_entry,
    write_toml_file_entry,
    filter_single_attribute,
    filter_list_attribute,
    update_file_entry,
    update_list_attribute,
)
from src.output import burn_toml_file_entry, delete_file_entry
from src.file_system import slither, read_file_metadata


def setup_test_file():
    fd, path = tempfile.mkstemp(suffix=".txt")
    with os.fdopen(fd, "w") as f:
        f.write("test content")
    return path


def test_file_entry_creation():
    path = setup_test_file()
    try:
        entry = FileEntry(path=path, description="test file")
        assert entry.name.endswith(".txt")
        assert entry.description == "test file"
        assert entry.tags == []
        assert entry.links == []
        assert entry.missing is False
        assert isinstance(entry.id, uuid.UUID)
    finally:
        os.remove(path)


def test_file_entry_dic():
    path = setup_test_file()
    try:
        entry = FileEntry(path=path, tags=["tag1", "tag2"], description="desc")
        d = entry.dic()
        assert d["name"] == entry.name
        assert d["tags"] == ["tag1", "tag2"]
        assert d["description"] == "desc"
        assert "path" in d
        assert "id" in d
        assert "missing" in d
    finally:
        os.remove(path)


def test_update_file_entry():
    path = setup_test_file()
    try:
        entry = FileEntry(path=path, description="original")
        updated = update_file_entry(entry, {"description": "updated", "tags": ["new"]})
        
        assert updated.description == "updated"
        assert updated.tags == ["new"]
        assert updated.name == entry.name
        assert updated.id == entry.id
    finally:
        os.remove(path)


def test_update_list_attribute():
    tags = ["a", "b"]
    
    added = update_list_attribute(tags, "c", "a")
    assert "c" in added
    assert added == ["a", "b", "c"]
    
    removed = update_list_attribute(added, "a", "r")
    assert "a" not in removed
    assert removed == ["b", "c"]


def test_filter_single_attribute():
    path1 = setup_test_file()
    path2 = setup_test_file()
    try:
        entries = [
            FileEntry(path=path1, name="file1"),
            FileEntry(path=path2, name="file2"),
        ]
        
        result = filter_single_attribute(entries, "name", "file1")
        assert len(result) == 1
        assert result[0].name == "file1"
    finally:
        os.remove(path1)
        os.remove(path2)


def test_filter_list_attribute():
    path1 = setup_test_file()
    path2 = setup_test_file()
    try:
        entries = [
            FileEntry(path=path1, tags=["music", "pdf"]),
            FileEntry(path=path2, tags=["video"]),
        ]
        
        result = filter_list_attribute(entries, "tags", ["music"])
        assert len(result) == 1
        assert "music" in result[0].tags
        
        result = filter_list_attribute(entries, "tags", ["video"])
        assert len(result) == 1
        assert "video" in result[0].tags
    finally:
        os.remove(path1)
        os.remove(path2)


def test_write_toml_file_entry():
    path = setup_test_file()
    try:
        entry = FileEntry(path=path, description="test")
        toml_str = write_toml_file_entry(entry)
        assert "path" in toml_str
        assert "description = \"test\"" in toml_str
        assert ".txt" in toml_str
    finally:
        os.remove(path)


def test_burn_and_read_toml():
    path = setup_test_file()
    try:
        original = FileEntry(
            path=path,
            name="test.txt",
            description="test desc",
            tags=["tag1"],
        )
        
        result = burn_toml_file_entry(original)
        assert "Successfully wrote" in result
        
        loaded = read_toml_file_entry(str(original.id))
        assert loaded.name == original.name
        assert loaded.description == original.description
        assert loaded.tags == original.tags
        assert loaded.id == original.id
        
        delete_file_entry(original.id)
    finally:
        os.remove(path)


def test_delete_file_entry():
    path = setup_test_file()
    try:
        entry = FileEntry(path=path)
        burn_toml_file_entry(entry)
        
        result = delete_file_entry(entry.id)
        assert "Successfully deleted" in result
        
        result = delete_file_entry(entry.id)
        assert "Could not find" in result
    finally:
        if os.path.exists(path):
            os.remove(path)


def test_read_file_metadata():
    path = setup_test_file()
    try:
        metadata = read_file_metadata(path)
        assert "mtime" in metadata
        assert "size" in metadata
        assert metadata["size"] == len("test content")
    finally:
        os.remove(path)


def test_slither():
    with tempfile.TemporaryDirectory() as tmpdir:
        os.makedirs(os.path.join(tmpdir, "subdir"))
        file1 = os.path.join(tmpdir, "file1.txt")
        file2 = os.path.join(tmpdir, "subdir", "file2.txt")
        
        with open(file1, "w") as f:
            f.write("x")
        with open(file2, "w") as f:
            f.write("x")
        
        paths = slither(tmpdir)
        assert len(paths) == 2
        assert any("file1.txt" in p for p in paths)
        assert any("file2.txt" in p for p in paths)

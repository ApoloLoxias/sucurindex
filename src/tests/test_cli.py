# Tests for sucurindex CLI commands
# Run from sucurindex/ with: uv run python -m pytest tests_cli.py -v

import os
import sys
import tempfile
import uuid
from io import StringIO
from unittest.mock import patch
from pathlib import Path

import pytest


def setup_test_file():
    fd, path = tempfile.mkstemp(suffix=".txt")
    with os.fdopen(fd, "w") as f:
        f.write("test content")
    return path


def cleanup_metadata(entry_id):
    from src.config import get_pstorage
    metadata_path = os.path.join(get_pstorage(), f"{entry_id}.toml")
    if os.path.exists(metadata_path):
        os.remove(metadata_path)


class TestCmdAdd:
    def test_add_new_file(self):
        from src.cli import cmd_add
        from src.output import delete_file_entry
        
        path = setup_test_file()
        try:
            result = cmd_add(path=path, name="test_file", description="test desc", tags=["tag1"], links=None)
            assert "successfully indexed" in result
            
            entry_id = result.split(": ")[-1].strip()
            cleanup_metadata(uuid.UUID(entry_id))
        finally:
            os.remove(path)

    def test_add_duplicate_file(self):
        from src.cli import cmd_add
        from src.output import delete_file_entry
        
        path = setup_test_file()
        try:
            result1 = cmd_add(path=path, name="test_file", description="test desc", tags=None, links=None)
            entry_id = result1.split(": ")[-1].strip()
            
            result2 = cmd_add(path=path, name="test_file", description="test desc", tags=None, links=None)
            assert "already catalogued" in result2
            
            cleanup_metadata(uuid.UUID(entry_id))
        finally:
            os.remove(path)

    def test_add_with_tags(self):
        from src.cli import cmd_add
        from src.parsing import read_toml_file_entry
        
        path = setup_test_file()
        try:
            result = cmd_add(path=path, name="tagged_file", description=None, tags=["tag1", "tag2"], links=None)
            entry_id = result.split(": ")[-1].strip()
            
            loaded = read_toml_file_entry(entry_id)
            assert loaded.tags == ["tag1", "tag2"]
            
            cleanup_metadata(uuid.UUID(entry_id))
        finally:
            os.remove(path)


class TestCmdRemove:
    def test_remove_existing_entry(self):
        from src.cli import cmd_add, cmd_remove
        from src.output import delete_file_entry
        
        path = setup_test_file()
        try:
            result = cmd_add(path=path, name="to_remove", description=None, tags=None, links=None)
            entry_id = result.split(": ")[-1].strip()
            
            with patch('builtins.input', return_value='y'):
                cmd_remove(entry_id)
            
            assert not os.path.exists(os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "sucurindex", "metadata", f"{entry_id}.toml"
            ))
        finally:
            os.remove(path)

    def test_remove_cancelled(self):
        from src.cli import cmd_add, cmd_remove
        from src.output import delete_file_entry
        
        path = setup_test_file()
        try:
            result = cmd_add(path=path, name="to_cancel", description=None, tags=None, links=None)
            entry_id = result.split(": ")[-1].strip()
            
            with patch('builtins.input', return_value='n'):
                result = cmd_remove(entry_id)
            
            assert "cancelled" in result.lower()
            
            cleanup_metadata(uuid.UUID(entry_id))
        finally:
            os.remove(path)


class TestCmdList:
    def test_list_all(self, capsys):
        from src.cli import cmd_add, cmd_list
        from src.output import delete_file_entry
        
        path = setup_test_file()
        try:
            result = cmd_add(path=path, name="list_test", description="test", tags=None, links=None)
            entry_id = result.split(": ")[-1].strip()
            
            cmd_list(id=None, name=None, description=None, tags=None, links=None)
            captured = capsys.readouterr()
            assert "list_test" in captured.out
            
            cleanup_metadata(uuid.UUID(entry_id))
        finally:
            os.remove(path)

    def test_list_filter_by_name(self, capsys):
        from src.cli import cmd_add, cmd_list
        from src.output import delete_file_entry
        
        path1 = setup_test_file()
        path2 = setup_test_file()
        try:
            cmd_add(path=path1, name="match_this", description=None, tags=None, links=None)
            cmd_add(path=path2, name="other_file", description=None, tags=None, links=None)
            
            cmd_list(id=None, name="match_this", description=None, tags=None, links=None)
            captured = capsys.readouterr()
            assert "match_this" in captured.out
            assert "other_file" not in captured.out
        finally:
            os.remove(path1)
            os.remove(path2)


class TestCmdRead:
    def test_read_existing_entry(self, capsys):
        from src.cli import cmd_add, cmd_read
        from src.output import delete_file_entry
        
        path = setup_test_file()
        try:
            result = cmd_add(path=path, name="read_test", description="test description", tags=["tag1"], links=None)
            entry_id = result.split(": ")[-1].strip()
            
            cmd_read(entry_id)
            captured = capsys.readouterr()
            assert "read_test" in captured.out
            assert "test description" in captured.out
            assert "tag1" in captured.out
            
            cleanup_metadata(uuid.UUID(entry_id))
        finally:
            os.remove(path)


class TestCmdSync:
    def test_sync_all_ok(self, capsys):
        from src.cli import cmd_add, cmd_sync
        from src.output import delete_file_entry
        
        path = setup_test_file()
        try:
            result = cmd_add(path=path, name="sync_test", description=None, tags=None, links=None)
            entry_id = result.split(": ")[-1].strip()
            
            result = cmd_sync(hard=False)
            assert "ok" in result
            assert "missing" in result
            assert "changed" in result
            
            cleanup_metadata(uuid.UUID(entry_id))
        finally:
            os.remove(path)


class TestCmdEdit:
    def test_edit_name_and_description(self):
        from src.cli import cmd_add, cmd_edit
        from src.parsing import read_toml_file_entry
        from src.output import delete_file_entry
        
        path = setup_test_file()
        try:
            result = cmd_add(path=path, name="original_name", description="original desc", tags=None, links=None)
            entry_id = result.split(": ")[-1].strip()
            
            cmd_edit(id=entry_id, name="new_name", description="new desc")
            
            updated = read_toml_file_entry(entry_id)
            assert updated.name == "new_name"
            assert updated.description == "new desc"
            
            cleanup_metadata(uuid.UUID(entry_id))
        finally:
            os.remove(path)

    def test_edit_add_tags(self):
        from src.cli import cmd_add, cmd_edit
        from src.parsing import read_toml_file_entry
        from src.output import delete_file_entry
        
        path = setup_test_file()
        try:
            result = cmd_add(path=path, name="tag_edit_test", description=None, tags=["tag1"], links=None)
            entry_id = result.split(": ")[-1].strip()
            
            cmd_edit(id=entry_id, atags=["tag2"])
            
            updated = read_toml_file_entry(entry_id)
            assert "tag2" in updated.tags
            
            cleanup_metadata(uuid.UUID(entry_id))
        finally:
            os.remove(path)

    def test_edit_remove_tags(self):
        from src.cli import cmd_add, cmd_edit
        from src.parsing import read_toml_file_entry
        from src.output import delete_file_entry
        
        path = setup_test_file()
        try:
            result = cmd_add(path=path, name="tag_remove_test", description=None, tags=["tag1", "tag2"], links=None)
            entry_id = result.split(": ")[-1].strip()
            
            cmd_edit(id=entry_id, rtags=["tag1"])
            
            updated = read_toml_file_entry(entry_id)
            assert "tag1" not in updated.tags
            assert "tag2" in updated.tags
            
            cleanup_metadata(uuid.UUID(entry_id))
        finally:
            os.remove(path)


class TestCmdSlither:
    def test_slither_single_directory(self):
        from src.cli import cmd_slither
        from src.file_system import list_file_entries
        
        with tempfile.TemporaryDirectory() as tmpdir:
            file1 = os.path.join(tmpdir, "file1.txt")
            file2 = os.path.join(tmpdir, "file2.txt")
            
            with open(file1, "w") as f:
                f.write("content1")
            with open(file2, "w") as f:
                f.write("content2")
            
            initial_count = len(list_file_entries())
            cmd_slither(tmpdir)
            
            final_count = len(list_file_entries())
            assert final_count == initial_count + 2
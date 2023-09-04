import pytest
import sort
import os
import shutil


@pytest.fixture
def sort_folder():
    sort_folder = os.path.expanduser('~') + f"\\OneDrive\\Pulpit\\sorted"
    return sort_folder


def test_if_starting_conditions_are_satisfied(sort_folder):
    try:
        shutil.rmtree(sort_folder)
    except FileNotFoundError:
        print(f"Folder sorted was not created yet")
    assert True


def test_if_sorted_folder_and_its_subfolders_are_present(sort_folder):
    sort.create_folders_for_sorted_content()
    assert os.path.isdir(sort_folder)
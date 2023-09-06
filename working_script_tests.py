import pytest
import sort
import os
import shutil


@pytest.fixture
def to_review_folder():
    to_review_folder = os.path.expanduser('~') + f"\\OneDrive\\Pulpit\\to_review"
    return to_review_folder


@pytest.fixture
def sort_folder():
    sort_folder = os.path.expanduser('~') + f"\\OneDrive\\Pulpit\\sorted"
    return sort_folder


def retrieve_files_extensions_in_folder(folder):
    elements = os.listdir(folder)
    folders = []
    extensions = []
    for element in elements:
        if os.path.isdir(folder + f"\\" + element):
            folders.append(element)
        elif os.path.isfile(folder + f"\\" + element):
            extensions.append(element.split(".")[-1].lower())
    return folders, extensions


def retrieve_files_and_folders_in_folder(folder):
    elements = os.listdir(folder)
    folders = []
    files = []
    for element in elements:
        if os.path.isdir(folder + f"\\" + element):
            folders.append(element)
        elif os.path.isfile(folder + f"\\" + element):
            files.append(element.lower())
    return folders, files


def test_if_starting_conditions_are_satisfied(sort_folder):
    try:
        shutil.rmtree(sort_folder)
    except FileNotFoundError:
        pass
    assert True


def test_if_sorted_folder_and_its_subfolders_are_present(sort_folder):
    sort.create_folders_for_sorted_content()
    assert os.path.isdir(sort_folder)
    assert os.path.isdir(sort_folder + f"\\images")
    assert os.path.isdir(sort_folder + f"\\documents")
    assert os.path.isdir(sort_folder + f"\\audio")
    assert os.path.isdir(sort_folder + f"\\video")
    assert os.path.isdir(sort_folder + f"\\archives")
    assert os.path.isdir(sort_folder + f"\\unknown_format")


def test_if_only_image_files_are_copied_to_images_folder(to_review_folder, sort_folder):
    sort.copy_image_files_to_images_folder(to_review_folder)
    folders, extensions = retrieve_files_extensions_in_folder(sort_folder + f"\\images")
    assert len(folders) == 0
    assert "jpeg" in extensions
    assert "png" in extensions
    assert "jpg" in extensions
    assert "svg" in extensions
    assert "avi" not in extensions
    assert "mp4" not in extensions
    assert "mov" not in extensions
    assert "mkv" not in extensions
    assert "doc" not in extensions
    assert "docx" not in extensions
    assert "txt" not in extensions
    assert "pdf" not in extensions
    assert "xlsx" not in extensions
    assert "pptx" not in extensions
    assert "mp3" not in extensions
    assert "ogg" not in extensions
    assert "wav" not in extensions
    assert "amr" not in extensions
    assert "zip" not in extensions
    assert "gz" not in extensions
    assert "tar" not in extensions
    assert "aaa" not in extensions
    assert "txż" not in extensions


def test_if_only_video_files_are_copied_to_video_folder(to_review_folder, sort_folder):
    sort.copy_video_files_to_video_folder(to_review_folder)
    folders, extensions = retrieve_files_extensions_in_folder(sort_folder + f"\\video")
    assert len(folders) == 0
    assert "jpeg" not in extensions
    assert "png" not in extensions
    assert "jpg" not in extensions
    assert "svg" not in extensions
    assert "avi" in extensions
    assert "mp4" in extensions
    assert "mov" in extensions
    assert "mkv" in extensions
    assert "doc" not in extensions
    assert "docx" not in extensions
    assert "txt" not in extensions
    assert "pdf" not in extensions
    assert "xlsx" not in extensions
    assert "pptx" not in extensions
    assert "mp3" not in extensions
    assert "ogg" not in extensions
    assert "wav" not in extensions
    assert "amr" not in extensions
    assert "zip" not in extensions
    assert "gz" not in extensions
    assert "tar" not in extensions
    assert "aaa" not in extensions
    assert "txż" not in extensions


def test_if_only_document_files_are_copied_to_documents_folder(to_review_folder, sort_folder):
    sort.copy_document_files_to_documents_folder(to_review_folder)
    folders, extensions = retrieve_files_extensions_in_folder(sort_folder + f"\\documents")
    assert len(folders) == 0
    assert "jpeg" not in extensions
    assert "png" not in extensions
    assert "jpg" not in extensions
    assert "svg" not in extensions
    assert "avi" not in extensions
    assert "mp4" not in extensions
    assert "mov" not in extensions
    assert "mkv" not in extensions
    assert "doc" in extensions
    assert "docx" in extensions
    assert "txt" in extensions
    assert "pdf" in extensions
    assert "xlsx" in extensions
    assert "pptx" in extensions
    assert "mp3" not in extensions
    assert "ogg" not in extensions
    assert "wav" not in extensions
    assert "amr" not in extensions
    assert "zip" not in extensions
    assert "gz" not in extensions
    assert "tar" not in extensions
    assert "aaa" not in extensions
    assert "txż" not in extensions


def test_if_only_audio_files_are_copied_to_audio_folder(to_review_folder, sort_folder):
    sort.copy_audio_files_to_audio_folder(to_review_folder)
    folders, extensions = retrieve_files_extensions_in_folder(sort_folder + f"\\audio")
    assert len(folders) == 0
    assert "jpeg" not in extensions
    assert "png" not in extensions
    assert "jpg" not in extensions
    assert "svg" not in extensions
    assert "avi" not in extensions
    assert "mp4" not in extensions
    assert "mov" not in extensions
    assert "mkv" not in extensions
    assert "doc" not in extensions
    assert "docx" not in extensions
    assert "txt" not in extensions
    assert "pdf" not in extensions
    assert "xlsx" not in extensions
    assert "pptx" not in extensions
    assert "mp3" in extensions
    assert "ogg" in extensions
    assert "wav" in extensions
    assert "amr" in extensions
    assert "zip" not in extensions
    assert "gz" not in extensions
    assert "tar" not in extensions
    assert "aaa" not in extensions
    assert "txż" not in extensions


def test_if_only_archive_files_are_copied_to_archive_folder(to_review_folder, sort_folder):
    sort.copy_archive_files_to_archives_folder(to_review_folder)
    folders, extensions = retrieve_files_extensions_in_folder(sort_folder + f"\\archives")
    assert len(folders) == 0
    assert "jpeg" not in extensions
    assert "png" not in extensions
    assert "jpg" not in extensions
    assert "svg" not in extensions
    assert "avi" not in extensions
    assert "mp4" not in extensions
    assert "mov" not in extensions
    assert "mkv" not in extensions
    assert "doc" not in extensions
    assert "docx" not in extensions
    assert "txt" not in extensions
    assert "pdf" not in extensions
    assert "xlsx" not in extensions
    assert "pptx" not in extensions
    assert "mp3" not in extensions
    assert "ogg" not in extensions
    assert "wav" not in extensions
    assert "amr" not in extensions
    assert "zip" in extensions
    assert "gz" in extensions
    assert "tar" in extensions
    assert "aaa" not in extensions
    assert "txż" not in extensions


def test_if_only_unknown_format_files_are_copied_to_unknown_format_folder(to_review_folder, sort_folder):
    sort.copy_unknown_format_files_to_unknown_format_folder(to_review_folder)
    folders, extensions = retrieve_files_extensions_in_folder(sort_folder + f"\\unknown_format")
    assert len(folders) == 0
    assert "jpeg" not in extensions
    assert "png" not in extensions
    assert "jpg" not in extensions
    assert "svg" not in extensions
    assert "avi" not in extensions
    assert "mp4" not in extensions
    assert "mov" not in extensions
    assert "mkv" not in extensions
    assert "doc" not in extensions
    assert "docx" not in extensions
    assert "txt" not in extensions
    assert "pdf" not in extensions
    assert "xlsx" not in extensions
    assert "pptx" not in extensions
    assert "mp3" not in extensions
    assert "ogg" not in extensions
    assert "wav" not in extensions
    assert "amr" not in extensions
    assert "zip" not in extensions
    assert "gz" not in extensions
    assert "tar" not in extensions
    assert "aaa" in extensions
    assert "txż" in extensions


def test_if_zip_archives_are_properly_unpacked(to_review_folder, sort_folder):
    _, files = retrieve_files_and_folders_in_folder(sort_folder + f"\\archives")
    zip_files = []
    zip_filenames = []
    for file in files:
        if file.split(".")[-1] == "zip":
            zip_files.append(file)
            zip_filenames.append(file[:-4])
    sort.unzip_zip_files()
    folders, _ = retrieve_files_and_folders_in_folder(sort_folder + f"\\archives")
    for zip_filename in zip_filenames:
        assert zip_filename in folders


def test_if_tar_archives_are_properly_unpacked(to_review_folder, sort_folder):
    _, files = retrieve_files_and_folders_in_folder(sort_folder + f"\\archives")
    tar_files = []
    tar_filenames = []
    for file in files:
        if file.split(".")[-1] == "tar":
            tar_files.append(file)
            tar_filenames.append(file[:-4])
    sort.unzip_tar_files()
    folders, _ = retrieve_files_and_folders_in_folder(sort_folder + f"\\archives")
    for tar_filename in tar_filenames:
        assert tar_filename in folders


def test_if_gz_archives_are_properly_unpacked(to_review_folder, sort_folder):
    _, files = retrieve_files_and_folders_in_folder(sort_folder + f"\\archives")
    gz_files = []
    gz_filenames = []
    for file in files:
        if file.split(".")[-1] == "gz":
            gz_files.append(file)
            gz_filenames.append(file[:-3])
    sort.unzip_gz_files()
    folders, _ = retrieve_files_and_folders_in_folder(sort_folder + f"\\archives")
    for gz_filename in gz_filenames:
        assert gz_filename in folders


def test_if_nested_files_are_properly_classified_and_if_proper_folders_are_ignored(to_review_folder, sort_folder):
    shutil.rmtree(sort_folder)
    sort.sort_files(to_review_folder)
    _, files_images = retrieve_files_and_folders_in_folder(sort_folder + f"\\images")
    _, files_documents = retrieve_files_and_folders_in_folder(sort_folder + f"\\documents")
    _, files_audio = retrieve_files_and_folders_in_folder(sort_folder + f"\\audio")
    _, files_video = retrieve_files_and_folders_in_folder(sort_folder + f"\\video")
    _, files_archives = retrieve_files_and_folders_in_folder(sort_folder + f"\\archives")
    _, files_unknown_format = retrieve_files_and_folders_in_folder(sort_folder + f"\\unknown_format")
    assert f"new_plik_jpg.jpg" not in files_images
    assert f"new_plik_txt.txt" not in files_documents
    assert f"new_plik_mp3.mp3" not in files_audio
    assert f"new_plik_mp4.mp4" not in files_video
    assert f"new_plik_zip.zip" not in files_archives
    assert f"new_plik_aaa.aaa" not in files_unknown_format
    assert f"plik_txt_2.txt" in files_documents


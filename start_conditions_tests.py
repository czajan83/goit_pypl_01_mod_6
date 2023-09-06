import pytest
import os


@pytest.fixture
def known_extensions():
    known_extensions = ["jpeg", "png", "jpg", "svg", "avi", "mp4", "mov", "mkv", "doc", "docx", "txt", "pdf", "xlsx",
                        "pptx", "mp3", "ogg", "wav", "amr", "zip", "gz", "tar"]
    return known_extensions


@pytest.fixture
def to_rev_folder():
    to_rev_folder = os.path.expanduser('~') + f"\\OneDrive\\Pulpit\\to_review"
    return to_rev_folder


def retrieve_file_extension(to_rev_folder, extension):
    trf_content = os.listdir(to_rev_folder)
    for element in trf_content:
        if os.path.isfile(to_rev_folder + f"\\" + element):
            element_extension = element.split(".")[1].lower()
            if element_extension == extension:
                return extension
    return None


def retrieve_unknown_extensions(to_rev_folder, known_extensions):
    trf_content = os.listdir(to_rev_folder)
    unknown_extensions = []
    current_extensions = []
    for element in trf_content:
        if os.path.isfile(to_rev_folder + f"\\" + element):
            current_extensions.append(element.split(".")[1].lower())
    for extension in current_extensions:
        if extension not in known_extensions:
            unknown_extensions.append(extension)
    return unknown_extensions


def retrieve_folders(to_rev_folder):
    trf_content = os.listdir(to_rev_folder)
    folders = []
    for element in trf_content:
        if os.path.isdir(to_rev_folder + f"\\" + element):
            folders.append(element)
    return folders


def retrieve_empty_folders(to_rev_folder):
    folders = retrieve_folders(to_rev_folder)
    empty_folders = []
    for folder in folders:
        sub_content = os.listdir(to_rev_folder + f"\\" + folder)
        if len(sub_content) == 0:
            empty_folders.append(folder)
    return empty_folders


def retrieve_non_empty_folders(to_rev_folder):
    folders = retrieve_folders(to_rev_folder)
    non_empty_folders = []
    for folder in folders:
        sub_content = os.listdir(to_rev_folder + f"\\" + folder)
        if len(sub_content) > 0:
            non_empty_folders.append(folder)
    return non_empty_folders


def retrieve_file_with_diacritic_in(to_rev_folder, place):
    # place = 0 : file name
    # place = 1 : file extension
    trf_content = os.listdir(to_rev_folder)
    for element in trf_content:
        if os.path.isfile(to_rev_folder + f"\\" + element):
            element = element.split(f".")[place]
        for letter in element:
            if not 48 <= ord(letter) <= 57 and \
                    not 65 <= ord(letter) <= 90 and \
                    not 97 <= ord(letter) <= 122 and \
                    not ord(letter) == 95:
                return element
    return None


def test_if_to_review_folder_exists(to_rev_folder):
    assert os.path.isdir(to_rev_folder)


def test_if_to_rev_folder_contains_jpeg_file(to_rev_folder):
    assert retrieve_file_extension(to_rev_folder, f"jpeg") == f"jpeg"


def test_if_to_rev_folder_contains_png_file(to_rev_folder):
    assert retrieve_file_extension(to_rev_folder, f"png") == f"png"


def test_if_to_rev_folder_contains_jpg_file(to_rev_folder):
    assert retrieve_file_extension(to_rev_folder, f"jpg") == f"jpg"


def test_if_to_rev_folder_contains_svg_file(to_rev_folder):
    assert retrieve_file_extension(to_rev_folder, f"svg") == f"svg"


def test_if_to_rev_folder_contains_avi_file(to_rev_folder):
    assert retrieve_file_extension(to_rev_folder, f"avi") == f"avi"


def test_if_to_rev_folder_contains_mp4_file(to_rev_folder):
    assert retrieve_file_extension(to_rev_folder, f"mp4") == f"mp4"


def test_if_to_rev_folder_contains_mov_file(to_rev_folder):
    assert retrieve_file_extension(to_rev_folder, f"mov") == f"mov"


def test_if_to_rev_folder_contains_mkv_file(to_rev_folder):
    assert retrieve_file_extension(to_rev_folder, f"mkv") == f"mkv"


def test_if_to_rev_folder_contains_doc_file(to_rev_folder):
    assert retrieve_file_extension(to_rev_folder, f"doc") == f"doc"


def test_if_to_rev_folder_contains_docx_file(to_rev_folder):
    assert retrieve_file_extension(to_rev_folder, f"docx") == f"docx"


def test_if_to_rev_folder_contains_txt_file(to_rev_folder):
    assert retrieve_file_extension(to_rev_folder, f"txt") == f"txt"


def test_if_to_rev_folder_contains_pdf_file(to_rev_folder):
    assert retrieve_file_extension(to_rev_folder, f"pdf") == f"pdf"


def test_if_to_rev_folder_contains_xlsx_file(to_rev_folder):
    assert retrieve_file_extension(to_rev_folder, f"xlsx") == f"xlsx"


def test_if_to_rev_folder_contains_pptx_file(to_rev_folder):
    assert retrieve_file_extension(to_rev_folder, f"pptx") == f"pptx"


def test_if_to_rev_folder_contains_mp3_file(to_rev_folder):
    assert retrieve_file_extension(to_rev_folder, f"mp3") == f"mp3"


def test_if_to_rev_folder_contains_ogg_file(to_rev_folder):
    assert retrieve_file_extension(to_rev_folder, f"ogg") == f"ogg"


def test_if_to_rev_folder_contains_wav_file(to_rev_folder):
    assert retrieve_file_extension(to_rev_folder, f"wav") == f"wav"


def test_if_to_rev_folder_contains_amr_file(to_rev_folder):
    assert retrieve_file_extension(to_rev_folder, f"amr") == f"amr"


def test_if_to_rev_folder_contains_zip_file(to_rev_folder):
    assert retrieve_file_extension(to_rev_folder, f"zip") == f"zip"


def test_if_to_rev_folder_contains_gz_file(to_rev_folder):
    assert retrieve_file_extension(to_rev_folder, f"gz") == f"gz"


def test_if_to_rev_folder_contains_tar_file(to_rev_folder):
    assert retrieve_file_extension(to_rev_folder, f"tar") == f"tar"


def test_if_to_rev_folder_contains_file_with_unknown_extension(to_rev_folder, known_extensions):
    assert len(retrieve_unknown_extensions(to_rev_folder, known_extensions)) > 0


def test_if_to_rev_folder_contains_empty_folder(to_rev_folder):
    assert len(retrieve_empty_folders(to_rev_folder)) > 0


def test_if_to_rev_folder_contains_non_empty_folder(to_rev_folder):
    assert len(retrieve_non_empty_folders(to_rev_folder)) > 0


def test_if_to_rev_folder_contains_file_with_diacritic_letters_in_name(to_rev_folder):
    assert retrieve_file_with_diacritic_in(to_rev_folder, place=0) is not None


def test_if_to_rev_folder_contains_file_with_diacritic_letters_in_extension(to_rev_folder):
    assert retrieve_file_with_diacritic_in(to_rev_folder, place=1) is not None


def test_if_images_folder_exists(to_rev_folder):
    assert os.path.isdir(to_rev_folder + f"\\images")


def test_if_documents_folder_exists(to_rev_folder):
    assert os.path.isdir(to_rev_folder + f"\\documents")


def test_if_audio_folder_exists(to_rev_folder):
    assert os.path.isdir(to_rev_folder + f"\\audio")


def test_if_video_folder_exists(to_rev_folder):
    assert os.path.isdir(to_rev_folder + f"\\video")


def test_if_archives_folder_exists(to_rev_folder):
    assert os.path.isdir(to_rev_folder + f"\\archives")


def test_if_images_folder_contains_at_least_one_file(to_rev_folder):
    assert len(os.listdir(to_rev_folder + f"\\images")) > 0


def test_if_documents_folder_contains_at_least_one_file(to_rev_folder):
    assert len(os.listdir(to_rev_folder + f"\\documents")) > 0


def test_if_audio_folder_contains_at_least_one_file(to_rev_folder):
    assert len(os.listdir(to_rev_folder + f"\\audio")) > 0


def test_if_video_folder_contains_at_least_one_file(to_rev_folder):
    assert len(os.listdir(to_rev_folder + f"\\video")) > 0


def test_if_archives_folder_contains_at_least_one_file(to_rev_folder):
    assert len(os.listdir(to_rev_folder + f"\\archives")) > 0


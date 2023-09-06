import gzip
import os
import shutil
import tarfile
import zipfile

TO_REVIEW_FOLDER = os.path.expanduser('~') + f"\\OneDrive\\Pulpit\\to_review"
SORTED_PATH = os.path.expanduser('~') + f"\\OneDrive\\Pulpit\\sorted"


def create_folders_for_sorted_content():
    if not os.path.exists(SORTED_PATH):
        os.makedirs(SORTED_PATH)
    if not os.path.exists(SORTED_PATH + f"\\images"):
        os.makedirs(SORTED_PATH + f"\\images")
    if not os.path.exists(SORTED_PATH + f"\\documents"):
        os.makedirs(SORTED_PATH + f"\\documents")
    if not os.path.exists(SORTED_PATH + f"\\audio"):
        os.makedirs(SORTED_PATH + f"\\audio")
    if not os.path.exists(SORTED_PATH + f"\\video"):
        os.makedirs(SORTED_PATH + f"\\video")
    if not os.path.exists(SORTED_PATH + f"\\archives"):
        os.makedirs(SORTED_PATH + f"\\archives")
    if not os.path.exists(SORTED_PATH + f"\\unknown_format"):
        os.makedirs(SORTED_PATH + f"\\unknown_format")


def copy_appropriate_files_to_appropriate_folders(folder, appropriate_folder, extensions):
    copied_files = []
    for element in os.listdir(folder):
        if os.path.isfile(folder + f"\\" + element):
            if element.split(".")[-1].upper() in extensions:
                shutil.copyfile(folder + f"\\{element}", f"{SORTED_PATH}\\{appropriate_folder}\\" + element.lower())
                copied_files.append(element.lower())
    return copied_files


def copy_image_files_to_images_folder(folder):
    return copy_appropriate_files_to_appropriate_folders(folder, f"images", ["JPEG", "PNG", "JPG", "SVG"])


def copy_video_files_to_video_folder(folder):
    return copy_appropriate_files_to_appropriate_folders(folder, f"video", ["AVI", "MP4", "MOV", "MKV"])


def copy_document_files_to_documents_folder(folder):
    return copy_appropriate_files_to_appropriate_folders(folder, f"documents",
                                                         ["DOC", "DOCX", "TXT", "PDF", "XLSX", "PPTX"])


def copy_audio_files_to_audio_folder(folder):
    return copy_appropriate_files_to_appropriate_folders(folder, f"audio", ["MP3", "OGG", "WAV", "AMR"])


def copy_archive_files_to_archives_folder(folder):
    return copy_appropriate_files_to_appropriate_folders(folder, f"archives", ["ZIP", "GZ", "TAR"])


def copy_unknown_format_files_to_unknown_format_folder(folder):
    known_extensions = ["JPEG", "PNG", "JPG", "SVG", "AVI", "MP4", "MOV", "MKV", "DOC", "DOCX", "TXT", "PDF", "XLSX",
                        "PPTX", "MP3", "OGG", "WAV", "AMR", "ZIP", "GZ", "TAR"]
    copied_files = []
    for element in os.listdir(folder):
        if os.path.isfile(folder + f"\\" + element):
            if element.split(".")[-1].upper() not in known_extensions:
                shutil.copyfile(folder + f"\\{element}", f"{SORTED_PATH}\\unknown_format\\" + element.lower())
                copied_files.append(element.lower())
    return copied_files


def unzip_zip_files():
    for element in os.listdir(SORTED_PATH + f"\\archives"):
        if os.path.isfile(SORTED_PATH + f"\\archives\\{element}"):
            if element.split(".")[-1] == "zip":
                with zipfile.ZipFile(SORTED_PATH + f"\\archives\\{element}", "r") as zip_ref:
                    zip_ref.extractall(SORTED_PATH + f"\\archives\\{element[:-4]}")
                os.remove(SORTED_PATH + f"\\archives\\{element}")


def unzip_tar_files():
    for element in os.listdir(SORTED_PATH + f"\\archives"):
        if os.path.isfile(SORTED_PATH + f"\\archives\\{element}"):
            if element.split(".")[-1] == "tar":
                with tarfile.TarFile(SORTED_PATH + f"\\archives\\{element}", "r") as tar_ref:
                    tar_ref.extractall(SORTED_PATH + f"\\archives\\{element[:-4]}")
                os.remove(SORTED_PATH + f"\\archives\\{element}")


def unzip_gz_files():
    for element in os.listdir(SORTED_PATH + f"\\archives"):
        if os.path.isfile(SORTED_PATH + f"\\archives\\{element}"):
            if element.split(".")[-1] == "gz":
                os.makedirs(SORTED_PATH + f"\\archives\\{element[:-3]}")
                with gzip.open(SORTED_PATH + f"\\archives\\{element}", "rb") as sf:
                    with open(SORTED_PATH + f"\\archives\\{element[:-3]}\\{element[:-3]}", "wb") as df:
                        shutil.copyfileobj(sf, df)
                os.remove(SORTED_PATH + f"\\archives\\{element}")


def sort_files(folder):
    create_folders_for_sorted_content()
    sub_folders = []
    for element in os.listdir(folder):
        if os.path.isdir(folder + f"\\{element}"):
            if element not in ["images", "documents", "audio", "video", "archives", "unknown_format"]:
                sub_folders.append(element)
    copy_image_files_to_images_folder(folder)
    copy_video_files_to_video_folder(folder)
    copy_document_files_to_documents_folder(folder)
    copy_audio_files_to_audio_folder(folder)
    copy_archive_files_to_archives_folder(folder)
    copy_unknown_format_files_to_unknown_format_folder(folder)
    unzip_zip_files()
    unzip_tar_files()
    unzip_gz_files()
    for sub_folder in sub_folders:
        sort_files(folder + f"\\{sub_folder}")

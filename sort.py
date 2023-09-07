import gzip
import os
import shutil
import sys
import tarfile
import zipfile

# TO_REVIEW_FOLDER = os.path.expanduser('~') + f"\\OneDrive\\Pulpit\\to_review"
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


def copy_appropriate_files_to_appropriate_folders(this_folder, appropriate_folder, extensions):
    copied_files = []
    for element in os.listdir(this_folder):
        if os.path.isfile(this_folder + f"\\" + element):
            if element.split(".")[-1].upper() in extensions:
                shutil.copyfile(this_folder + f"\\{element}",
                                f"{SORTED_PATH}\\{appropriate_folder}\\" + element.lower())
                copied_files.append(element.lower())
    return copied_files


def copy_image_files_to_images_folder(this_folder):
    return copy_appropriate_files_to_appropriate_folders(this_folder, f"images", ["JPEG", "PNG", "JPG", "SVG"])


def copy_video_files_to_video_folder(this_folder):
    return copy_appropriate_files_to_appropriate_folders(this_folder, f"video", ["AVI", "MP4", "MOV", "MKV"])


def copy_document_files_to_documents_folder(this_folder):
    return copy_appropriate_files_to_appropriate_folders(this_folder, f"documents",
                                                         ["DOC", "DOCX", "TXT", "PDF", "XLSX", "PPTX"])


def copy_audio_files_to_audio_folder(this_folder):
    return copy_appropriate_files_to_appropriate_folders(this_folder, f"audio", ["MP3", "OGG", "WAV", "AMR"])


def copy_archive_files_to_archives_folder(this_folder):
    return copy_appropriate_files_to_appropriate_folders(this_folder, f"archives", ["ZIP", "GZ", "TAR"])


def copy_unknown_format_files_to_unknown_format_folder(this_folder):
    known_extensions = ["JPEG", "PNG", "JPG", "SVG", "AVI", "MP4", "MOV", "MKV", "DOC", "DOCX", "TXT", "PDF", "XLSX",
                        "PPTX", "MP3", "OGG", "WAV", "AMR", "ZIP", "GZ", "TAR"]
    copied_files = []
    for element in os.listdir(this_folder):
        if os.path.isfile(this_folder + f"\\" + element):
            if element.split(".")[-1].upper() not in known_extensions:
                shutil.copyfile(this_folder + f"\\{element}", f"{SORTED_PATH}\\unknown_format\\" + element.lower())
                copied_files.append(element.lower())
    return copied_files


def unzip_zip_files():
    for element in os.listdir(SORTED_PATH + f"\\archives"):
        if os.path.isfile(SORTED_PATH + f"\\archives\\{element}"):
            if element.split(".")[-1] == "zip":
                try:
                    with zipfile.ZipFile(SORTED_PATH + f"\\archives\\{element}", "r") as zip_ref:
                        zip_ref.extractall(SORTED_PATH + f"\\archives\\{element[:-4]}")
                    os.remove(SORTED_PATH + f"\\archives\\{element}")
                except FileExistsError:
                    pass


def unzip_tar_files():
    for element in os.listdir(SORTED_PATH + f"\\archives"):
        if os.path.isfile(SORTED_PATH + f"\\archives\\{element}"):
            if element.split(".")[-1] == "tar":
                try:
                    with tarfile.TarFile(SORTED_PATH + f"\\archives\\{element}", "r") as tar_ref:
                        tar_ref.extractall(SORTED_PATH + f"\\archives\\{element[:-4]}")
                    os.remove(SORTED_PATH + f"\\archives\\{element}")
                except FileExistsError:
                    pass


def unzip_gz_files():
    for element in os.listdir(SORTED_PATH + f"\\archives"):
        if os.path.isfile(SORTED_PATH + f"\\archives\\{element}"):
            if element.split(".")[-1] == "gz":
                try:
                    os.makedirs(SORTED_PATH + f"\\archives\\{element[:-3]}")
                    with gzip.open(SORTED_PATH + f"\\archives\\{element}", "rb") as sf:
                        with open(SORTED_PATH + f"\\archives\\{element[:-3]}\\{element[:-3]}", "wb") as df:
                            shutil.copyfileobj(sf, df)
                    os.remove(SORTED_PATH + f"\\archives\\{element}")
                except FileExistsError:
                    pass


def get_filename_and_extension(file):
    filename = f""
    extension = f""
    element_parts = file.split(".")
    for i in range(len(element_parts) - 1):
        filename += element_parts[i] + f"."
        filename = filename[:-1]
        extension = element_parts[-1]
    return filename, extension


def sort_files(this_folder):
    create_folders_for_sorted_content()
    sub_folders = []
    for element in os.listdir(this_folder):
        if os.path.isdir(this_folder + f"\\{element}"):
            if element not in ["images", "documents", "audio", "video", "archives", "unknown_format"]:
                sub_folders.append(element)
    copy_image_files_to_images_folder(this_folder)
    copy_video_files_to_video_folder(this_folder)
    copy_document_files_to_documents_folder(this_folder)
    copy_audio_files_to_audio_folder(this_folder)
    copy_archive_files_to_archives_folder(this_folder)
    copy_unknown_format_files_to_unknown_format_folder(this_folder)
    unzip_zip_files()
    unzip_tar_files()
    unzip_gz_files()
    for sub_folder in sub_folders:
        sort_files(this_folder + f"\\{sub_folder}")


def remove_unnecessary_files_and_folders_from_their_original_place(this_folder):
    for element in os.listdir(this_folder):
        if os.path.isdir(this_folder + f"\\{element}"):
            if element not in ["images", "documents", "audio", "video", "archives", "unknown_format"]:
                shutil.rmtree(this_folder + f"\\{element}")


def rename_element(element):
    new_name = f""
    for letter in element:
        if not 48 <= ord(letter) <= 57 and \
                not 65 <= ord(letter) <= 90 and \
                not 97 <= ord(letter) <= 122 and \
                not ord(letter) == 95:
            new_name += f"_"
        else:
            new_name += letter
    return new_name


def normalize(this_folder):
    for element in os.listdir(this_folder):
        if os.path.isdir(this_folder + f"\\{element}"):
            normalize(this_folder + f"\\{element}")
            new_name = rename_element(element)
            if element != new_name:
                try:
                    os.rename(this_folder + f"\\{element}", this_folder + f"\\{new_name}")
                except FileExistsError:
                    pass
        else:
            filename, extension = get_filename_and_extension(element)
            new_filename = rename_element(filename)
            if filename != new_filename:
                try:
                    os.rename(this_folder + f"\\{filename}.{extension}", this_folder + f"\\{new_filename}.{extension}")
                except FileExistsError:
                    pass


def get_found_files_and_extensions(this_folder):
    extensions = []
    files = []
    for element in os.listdir(SORTED_PATH + f"\\{this_folder}"):
        files.append(element)
        filename, extension = get_filename_and_extension(element)
        if extension not in extensions:
            extensions.append(extension)
    return files, extensions


def print_found_files_and_extensions(filetypes, files, extensions):
    print(20 * "*")
    print(f"Found {filetypes} files:")
    for file in files:
        print(f"{file}")
    print(f"\nFound {filetypes} extensions:")
    for extension in extensions:
        print(f"{extension}")
    print(f"")


def print_unpacked_archives(unpacked_archives):
    print(20 * "*")
    print(f"Found unpacked archives:")
    for my_folder in unpacked_archives:
        print(f"{my_folder}")
    print(f"")


def print_sorting_log():
    image_files, image_extensions = get_found_files_and_extensions(f"images")
    video_files, video_extensions = get_found_files_and_extensions(f"video")
    documents_files, documents_extensions = get_found_files_and_extensions(f"documents")
    audio_files, audio_extensions = get_found_files_and_extensions(f"video")
    unpacked_archives = os.listdir(SORTED_PATH + f"\\archives")
    unknown_files, unknown_extensions = get_found_files_and_extensions(f"unknown_format")
    print_found_files_and_extensions(f"images", image_files, image_extensions)
    print_found_files_and_extensions(f"video", video_files, video_extensions)
    print_found_files_and_extensions(f"documents", documents_files, documents_extensions)
    print_found_files_and_extensions(f"audio", audio_files, audio_extensions)
    print_unpacked_archives(unpacked_archives)
    print_found_files_and_extensions(f"unknown format", unknown_files, unknown_extensions)


def main(to_rev_folder):
    create_folders_for_sorted_content()
    sort_files(to_rev_folder)
    normalize(SORTED_PATH)
    print_sorting_log()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        folder = os.path.expanduser('~') + f"\\OneDrive\\Pulpit\\to_review"
    else:
        folder = sys.argv[1]
    main(folder)

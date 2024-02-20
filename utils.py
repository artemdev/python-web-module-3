import os
import shutil
import counter
import logging
from config import EXTENSION_FOLDERS, OTHER_FOLDER_NAME


def folder_name_for_extension(extension):
    folder_name = OTHER_FOLDER_NAME

    for key, value in EXTENSION_FOLDERS.items():
        if (extension.upper() in key):
            folder_name = value

    return folder_name


def remove_empty_folder(path):
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_dir() and not os.listdir(entry.path):
                os.rmdir(entry.path)


def supported_archives_list():
    return list(EXTENSION_FOLDERS.keys())[4]


def move_file(entry, destination_file_path, folder_name_for_file_extension, event):
    logging.debug(f"Moving start...")
    event.clear()
    shutil.move(entry.path, destination_file_path)
    counter.update_counter(entry, folder_name_for_file_extension)
    logging.debug(f"Moving finished ...")
    event.set()


def unpack_achive(entry, destination_file_path, folder_name_for_file_extension):
    logging.debug(f"Unpacking archive {entry.path} to {destination_file_path}")
    shutil.unpack_archive(entry.path, destination_file_path)
    counter.update_counter(entry, folder_name_for_file_extension)
    logging.debug(f"Unpacking finished")


def count_subfolders(path):
    return len([name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))])

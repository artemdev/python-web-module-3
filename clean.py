import os
import sys
from pathlib import Path
import logging
from threading import Semaphore, Thread

import utils as utils
from normalize import normalize
from config import IGNORED_DIRECTORIES
import counter

logging.basicConfig(level=logging.DEBUG,
                    format='%(threadName)s %(message)s')

PATH = '/Users/artem/Downloads'
CONDITION = Semaphore(5)
total_folder_threads = 0


def sort_files(path):
    logging.debug(f"Sorting folder {path}")

    current_folder = Path(path).name

    if (current_folder in IGNORED_DIRECTORIES):
        return

    with os.scandir(path) as it:
        for entry in it:
            if (entry.is_dir()):
                if utils.count_subfolders(path) > 8:
                    with CONDITION:
                        thread = Thread(target=sort_files,
                                        args=[(entry.path)])
                        thread.start()
                else:
                    sort_files(entry.path)
            elif (entry.is_file()):
                file_path, file_extension = os.path.splitext(entry.path)

                extension_name = file_extension[1:]

                folder_name_for_file_extension = utils.folder_name_for_extension(
                    extension_name)
                filename_normalized = normalize(
                    os.path.basename(file_path))
                extension_folder = os.path.join(
                    path, folder_name_for_file_extension)

                try:
                    os.makedirs(extension_folder)
                except os.error as e:
                    pass

                args = (entry, os.path.join(
                    extension_folder, filename_normalized + file_extension), folder_name_for_file_extension)

                if extension_name.upper() in utils.supported_archives_list():
                    with CONDITION:
                        thread = Thread(target=utils.unpack_achive,
                                        args=args)
                        thread.start()

                else:
                    with CONDITION:
                        thread = Thread(target=utils.move_file,
                                        args=args)
                        thread.start()

    utils.remove_empty_folder(path)


if (__name__ == "__main__"):
    sort_files(sys.argv[1] if len(sys.argv) > 1 else PATH)
    counter.print_results()

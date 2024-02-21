import os
from collections import defaultdict

from config import EXTENSION_FOLDERS


def create_counter():
    counter = {
        'categories': defaultdict(int),
        'supported_extensions': set(),
        'unsupported_extensions': set(),
        'without_extension': 0
    }

    for value in EXTENSION_FOLDERS.values():
        counter['categories'][value] = 0

    return counter


def update_counter(entry, folder_name_for_file_extension):
    extension = os.path.splitext(entry.path)[1][1:]

    counter['categories'][folder_name_for_file_extension] += 1

    if not extension:
        counter['without_extension'] += 1

        return

    for key in EXTENSION_FOLDERS.keys():
        if extension.upper() in key:
            counter['supported_extensions'].add(extension)
            return

    counter['unsupported_extensions'].add(extension)


def print_results():
    title = 'Following files has been moved:\n'
    header = "|{:<10}|{:10}|{:>10}|{:>10}|{:>10}|\n".format(
        *list(counter['categories'].keys()))
    body = "|{:<10}|{:<10}|{:>10}|{:>10}|{:>10}|".format(
        *list(counter['categories'].values()))

    print(title + header + body)

    if counter['supported_extensions']:
        print('Supported extensions:', ", ".join(
            list(counter['supported_extensions'])))

    if counter['unsupported_extensions']:
        print('Unsupported extensions:', ", ".join(
            list(counter['unsupported_extensions'])))

    if counter['without_extension'] > 0:
        print('Without extension:', counter['without_extension'])


counter = create_counter()

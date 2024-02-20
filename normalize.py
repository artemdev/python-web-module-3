import os

LATIN_ALPHABET = set('abcdefghijklmnopqrstuvwxyz')
CYRILLIC_ALPHABET = set('абвгдежзийклмнопрстуфхцчшщъыьэюя')
CYRILLIC_ALPHABET_CAPITALIZED = {char.upper() for char in CYRILLIC_ALPHABET}
LATIN_ALPHABET_CAPITALIZED = {char.upper() for char in LATIN_ALPHABET}
CYRILLIC_TO_LATIN = {
    'а': 'a',
    'б': 'b',
    'в': 'v',
    'г': 'g',
    'д': 'd',
    'е': 'e',
    'ё': 'e',
    'ж': 'zh',
    'з': 'z',
    'и': 'i',
    'й': 'y',
    'к': 'k',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'о': 'o',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': 'u',
    'ф': 'f',
    'х': 'kh',
    'ц': 'ts',
    'ч': 'ch',
    'ш': 'sh',
    'щ': 'shch',
    'ъ': '',
    'ы': 'y',
    'ь': '',
    'э': 'e',
    'ю': 'yu',
    'я': 'ya',
}


def normalize(name):
    base_name, extension = os.path.splitext(name)

    normalized_name = ''

    for letter in base_name:
        normalized_letter = ''

        if (letter in CYRILLIC_ALPHABET):
            normalized_letter = CYRILLIC_TO_LATIN.get(letter, '_')
        elif (letter in LATIN_ALPHABET or letter in LATIN_ALPHABET_CAPITALIZED or letter in CYRILLIC_ALPHABET_CAPITALIZED or letter.isdigit()):
            normalized_letter = letter
        else:
            normalized_letter = '_'

        normalized_name += normalized_letter

    return normalized_name + extension

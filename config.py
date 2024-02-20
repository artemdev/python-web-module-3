OTHER_FOLDER_NAME = 'other'
EXTENSION_FOLDERS = {
    ('JPEG', 'PNG', 'JPG', 'SVG'): 'images',
    ('AVI', 'MP4', 'MOV', 'MKV'): 'video',
    ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'): 'documents',
    ('MP3', 'OGG', 'WAV', 'AMR'): 'audio',
    ('ZIP', 'GZ', 'TAR'): 'archives'
    
}
IGNORED_DIRECTORIES = [*list(EXTENSION_FOLDERS.values()), OTHER_FOLDER_NAME]
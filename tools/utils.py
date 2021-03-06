import glob

import os


def file_in_dir(directory, extends):
    files = []
    for ext in extends:
        files.extend(glob.glob(os.path.join(directory, ext)))
    return files


def json_in_dir(json_file_dir):
    return file_in_dir(json_file_dir, ['*.json'])

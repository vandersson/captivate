"""Handles interaction with filesystem for images"""
from os import path, makedirs
import shutil

def persist(tmp_path, timestamp):
    """Saves the image to a file in folders specified by date"""
    date_path = create_path(timestamp)
    if not path.exists(date_path):
        makedirs(date_path)
    shutil.move(tmp_path, path.join(date_path, path.basename(tmp_path)))

def create_path(t):
    ret = path.join('.', 'uploads', str(t.tm_year), str(t.tm_mon), str(t.tm_mday))
    return ret


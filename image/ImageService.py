"""Working with images"""
from image import ImageDiskPersist
import time
import exifread

date_time_format = "%Y:%m:%d %H:%M:%S"
date_time_key = 'EXIF DateTimeOriginal'

def process_tmp_image(tmp_path):
    timestamp = find_photo_time(tmp_path)
    ImageDiskPersist.persist(tmp_path, timestamp)

def find_photo_time(tmp_path):
    with open(tmp_path, 'rb') as f:
        tags = exifread.process_file(f)
        return time.strptime(str(tags[date_time_key]), date_time_format)
        


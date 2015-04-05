"""API for image related tasks"""
from flask import Blueprint, make_response, request
import time
from image import ImageService
import tempfile
from os import path

image_api = Blueprint('image_api', __name__)

@image_api.route('/image/add', methods=['POST'])
def add_image():
    for name, file in request.files.items():
        tmp_path = path.join(tempfile.gettempdir(), "img_%s_%d" % (name, time.time()))
        file.save(tmp_path)
        ImageService.process_tmp_image(tmp_path)
    return make_response()

#@image_api.route('/image/add2', methods=['PUT'])
#def add_image2():
#    img = BytesIO(request.stream.read())
#    tags = exifread.process_file(img)
#    timestamp = time.strptime(str(tags['EXIF DateTimeOriginal']), "%Y:%m:%d %H:%M:%S")
#    print(timestamp)
#    with open('uploaded_image.jpg', 'wb') as f:
#        f.write(request.stream.read())
#    return make_response()


#def print_all_tags(tags):
#    for tag in tags.keys():
#        if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
#            t = time.strptime("2015:03:01 18:32:36", "%Y:%m:%d %H:%M:%S")
#            print("Key: %s, value %s" % (tag, tags[tag]))

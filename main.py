"""Main part of application"""
from flask import Flask, make_response
from image.ImageAPI import image_api

app = Flask(__name__)
app.register_blueprint(image_api)
IMAGE_FILES_ROOT = './uploads'

@app.route("/")
def main():
    return "Image Captivate"

if __name__ == "__main__":
    app.debug = True
    app.run()
    app.config['IMG_ROOT'] = IMAGE_FILES_ROOT

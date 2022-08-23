from flask import Flask
from flask_dropzone import Dropzone
import os

app = Flask(__name__)

dir_path = os.path.dirname(os.path.realpath(__file__))

app.config['SECRET_KEY'] = '47cc946a2fd8721de8b9025ce1b33c39e26f9e0c'

app.config.update(
    UPLOADED_PATH=os.path.join(dir_path, "static"),
    DROPZONE_ALLOWED_FILE_TYPE='image',
    DROPZONE_MAX_FILE_SIZE=3,
    DROPZONE_MAX_FILES=1
)

app.config['DROPZONE_REDIRECT_VIEW'] = 'decoded'

dropzone = Dropzone(app)



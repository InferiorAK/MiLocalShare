from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from .arg import *

app = Flask(__name__)
app.config["UPLOAD_PATH"] = args.path + "/"

def engine():
    if request.method == "POST":
        if not request.files.get("fileup").filename == "":
            files = request.files.getlist("fileup")
            if os.path.exists(app.config["UPLOAD_PATH"]):
                pass
            else:
                os.makedirs(app.config["UPLOAD_PATH"])
            for file in files:
                file_name = secure_filename(file.filename)
                # file_name = file.filename
                name, ext = os.path.splitext(file_name)
                FileFinal = ""
                outfile = name+f"_({{}})"+ext
                if os.path.exists(app.config["UPLOAD_PATH"]+file_name):
                    no = 1
                    while os.path.exists(app.config["UPLOAD_PATH"]+outfile.format(no)):
                        no += 1
                    FileFinal += outfile.format(no)
                    file.save(os.path.join(
                        app.config["UPLOAD_PATH"], FileFinal))
                else:
                    file.save(os.path.join(
                        app.config["UPLOAD_PATH"], file_name))
        else:
            pass

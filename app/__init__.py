__version__="0.1"

from flask import Flask
from flask import render_template

app=Flask(__name__, template_folder="views")

UPLOAD_FOLDER="app/static/img"

app.config["UPLOAD FOLDER"]=UPLOAD_FOLDER
@app.route('/')
#metodo principal
def index():
    return render_template('index.html')
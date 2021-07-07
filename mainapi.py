import os

from flask import Flask, request

from detecttunes.recognise import recognise_song

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to the song finder"


@app.route("/search", methods=['POST'])
def searchthissong():
    if 'record' not in request.files:
        return "must send record in post field"
    file = request.files['record']
#     if the user doesnot select a file , the browser submits anempty file without filename.
    if file.filename == '':
        return "no record was provided"
    if file:
        filename = file.filename
        filepath = os.path.join('E:/Detecttunes/detecttunes/test/ab/', filename)
        file.save(filepath)
        returnedvalued = recognise_song(filepath)
        return returnedvalued

from flask import Flask, request, redirect, Response
from gallery import gallery
import base64

app = Flask(__name__)
# Todo: Update this to a bucket in your account
bucket = 'my-playpen'

@app.route('/hello/<name>')
def hello(name):
    return 'Hello ' + name + '!'

@app.route('/gallery/download', methods=["POST"])
def download():

  if "file" not in request.form:
    return "No file name in request"
  
  file = request.form['file']
  
  if file == "":
    return "Please select a file"
  
  if file:
    try:
      
      image = gallery.download(file, bucket)
    except Exception as e:
      # Todo: Improve
      print("Something Happened: ", e)
      return e

    return Response(
      image,
      mimetype='image/jpg',
      headers={
        "Content-Disposition": "attachment;filename=image.jpg",
        "Content-type": "image/jpg"
        }
    )

  else:
    return redirect("/")

@app.route('/gallery/upload', methods=["POST"])
def upload():

  if "file" not in request.files:
    return "No file key in request"
  
  file = request.files['file']
  
  if file.filename == "":
    return "Please select a file"
  
  if file:
    try:
      response = gallery.upload(file, bucket)
    except Exception as e:
      # Todo: Improve
      print("Something Happened: ", e)
      return e

    return str(response)
  else:
    return redirect("/")
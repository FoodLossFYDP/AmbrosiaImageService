from flask import Flask, render_template, send_file
from flask import request
from PIL import Image, ImageTk
from io import BytesIO
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import base64
import json
import cv2
import queue
import socketio


app = Flask(__name__)

fig = plt.figure()

image_queue = queue.Queue()

@app.route("/process", methods=['POST'])
def process():
    print("Image received")
    img_string = request.form.get('image')
    img_data = base64.b64decode(img_string)

    # do image processing (keep android client async!!)

    image_queue.put(img_string)
    # filename = 'image.jpg'
    # with open(filename, 'wb') as f:
    #     f.write(img_data)
    # i = cv2.imread('image.jpg')
    # cv2.imshow('image', i)
    # cv2.waitKey(1)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route("/ui", methods=['GET'])
def show():
    print("UI Request received")
    filename = 'image.jpg'
    # with open(filename, 'wb') as f:
    #     f.write(image_queue.get())
    # absolutefilename = 'http://127.0.0.1:5000/uploads/' + filename
    img = image_queue.get()
    return render_template('template.html', file=img)

# @app.route('/uploads/<filename>')
# def send_file(filename):
#     print("Image Request received")
#     return send_file('image.jpg')
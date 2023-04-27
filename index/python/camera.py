import cv2
import numpy
from flask import Flask, render_template, Response, stream_with_context, request
from random import randrange

face_data = cv2.CascadeClassifier('trained_data/haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)
app = Flask('__name__')
i = 0



def video_stream():
    while True:
        ret, frame = video.read()
        if not ret:
            break
        else:
            successful_frame_read, frame = video.read()
            grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            face_coord = face_data.detectMultiScale(grayscale_img)

            for ((x, y, w, h)) in face_coord:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(128, 255), randrange(128, 255), randrange(128, 255)), 5)
                if(str(face_coord.all) > str(0)):
                   i = i + 1
                   print(i)

            ret, buffer = cv2.imencode('.jpeg',frame)
            frame = buffer.tobytes()
            yield (b' --frame\r\n' b'Content-type: imgae/jpeg\r\n\r\n' + frame +b'\r\n')


@app.route('/camera')
def camera():
    return render_template('camera.html')


@app.route('/video_feed')
def video_feed():
    return Response(video_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')


app.run(host='0.0.0.0', port='5000', debug=False)

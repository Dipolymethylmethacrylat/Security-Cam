import cv2
from random import randrange

i = 0

#face_data = cv2.CascadeClassifier('haarcascade_frontalface_extended.xml')
face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)

while True:

    successful_frame_read, frame = video.read()
    grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces
    face_coord = face_data.detectMultiScale(grayscale_img)

    #src, coordinates, color, thickness
    for ((x, y, w, h)) in face_coord:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(128, 255), randrange(128, 255), randrange(128, 255)), 5)
        i = 0
        if(str(face_coord.all) > str(0)):
            i = i + 1
        print(i)



    cv2.imshow('Cool', frame)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break  

video.release()

print("Code Stopped")

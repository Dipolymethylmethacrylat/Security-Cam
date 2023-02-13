import cv2
from random import randrange

face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture(0)

while True:

    successful_frame_read, frame = camera.read()
    grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces
    face_coord = face_data.detectMultiScale(grayscale_img)

    #src, coordinates, color, thickness
    for ((x, y, w, h)) in face_coord:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(128, 255), randrange(128, 255), randrange(128, 255)), 5)
        print(face_coord)

    cv2.imshow('Cool', frame)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break  


camera.release()


"""
#scaling the image gray so ai can process faster
grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#detect faces
face_coord = face_data.detectMultiScale(grayscale_img)


#src, coordinates, color, thickness
for((x, y, w, h)) in face_coord:
    cv2.rectangle(img, (x,y), (x+w, y+h), (randrange(255), randrange(255), randrange(255)), 5)
    print(face_coord)



#opens the image while waiting for key
cv2.imshow('Cool', img)
cv2.waitKey()
"""


print("Code Stopped")

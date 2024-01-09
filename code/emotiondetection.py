import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
import cv2
from deepface import DeepFace

# Classifier gives (x,y), width and height
face_classifier = cv2.CascadeClassifier()
face_classifier.load(cv2.samples.findFile("haarcascade_frontalface_default.xml"))

# Capture video source (laptop webcam, external webcam, etc)
cap = cv2.VideoCapture(1)

# Read each frame (series of images will make a video)
while True:
    ret, frame = cap.read()
    # RGB to grayscale then pass to classifier
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(frame_gray)

    # Give deepface an image so that it returns an emotion
    response = DeepFace.analyze(frame, actions=("emotion",), enforce_detection=False)
    print(response)


    # print(faces)

    for face in faces:
        # Create rectangle on frame
        x, y, w, h = face
        # print(response[0]['dominant_emotion'])
        cv2.putText(frame, text = response[0]['dominant_emotion'], org=(x,y), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1, color=(0, 255, 0))
        new_frame = cv2.rectangle(frame, (x, y), (x+w, y+h), color=(255, 0, 0), thickness=2)



        cv2.imshow("", new_frame)
    if(cv2.waitKey(30) == 27):
        break
cap.release()
cv2.destroyAllWindows()
import cv2

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
    # print(faces)

    for face in faces:
        # Create rectangle on frame
        x, y, w, h = face
        new_frame = cv2.rectangle(frame, (x, y), (x+w, y+h), color=(255, 0, 0), thickness=2)



        cv2.imshow("", new_frame)
    if(cv2.waitKey(30) == 27):
        break
cap.release()
cv2.destroyAllWindows()
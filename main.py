import cv2
import csv
from datetime import datetime

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

cap = cv2.VideoCapture(0)

marked = False

def markAttendance():
    global marked
    if not marked:
        with open('attendance.csv', 'a') as f:
            now = datetime.now()
            time = now.strftime('%H:%M:%S')
            f.write(f'FaceDetected,{time}\n')
            print("Attendance Marked Successfully")
            marked = True

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

        cv2.putText(frame, "Face Detected Successfully", (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

        markAttendance()

    cv2.imshow('Smart Attendance System', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
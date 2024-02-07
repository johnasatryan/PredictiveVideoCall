import sys
import cv2
from PySide2.QtCore import QTimer, Qt, QFile
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel
from PySide2.QtUiTools import QUiLoader
import os
from pathlib import Path

class CameraWindow(QMainWindow):
    def __init__(self, ui):
        super().__init__()
        loader = QUiLoader()
        self.previous_frame = None

        self.ui = ui
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        self.setWindowTitle("Camera Example")
        self.setGeometry(100, 100, 800, 600)


        # Initialize OpenCV video capture
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Error: Could not open video stream.")
            exit()

        # Set up a QTimer to fetch frames from the video capture
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(20)  # Update interval in ms
        self.ui.endButton.clicked.connect(self.closeEvent)



    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            face_positions = ""

            self.previous_frame = gray
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                position = "left" if x + w/2 < frame.shape[1] / 2 else "right"
                face_info = f"Face at X: {x}, Y: {y}\nPosition: {position}\n"
                face_positions += face_info


            self.ui.console.setText(face_positions)




            # Convert the captured frame to RGB
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            # Convert the image to Qt format
            qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qt_image)
            # Scale pixmap to fit in the QLabel
            self.ui.cameraView.setPixmap(pixmap.scaled(self.ui.cameraView.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def closeEvent(self, event):
        self.cap.release()  # Release the video capture object


    def stop_camera(self):
            # Method to stop the camera and close the window
            if self.timer.isActive():
                self.timer.stop()
            if self.cap.isOpened():
                self.cap.release()
            self.ui.cameraView.clear()  # Clear the QLabel
            self.close()  # Close the window

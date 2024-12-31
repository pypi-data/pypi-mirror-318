import cv2
from kamera.settings import process_frame


class CameraStream:
    def __init__(self, camera_index=0, rotate=0, brightness=1.0, grayscale=False):
        self.camera_index = camera_index
        self.rotate = rotate
        self.brightness = brightness
        self.grayscale = grayscale
        self.cap = cv2.VideoCapture(camera_index)

    def get_frame(self):
        success, frame = self.cap.read()
        if not success:
            return None
        # Process the frame using the settings
        frame = process_frame(
            frame,
            rotate=self.rotate,
            brightness=self.brightness,
            grayscale=self.grayscale,
        )
        _, buffer = cv2.imencode(".jpg", frame)
        return buffer.tobytes()

    def release(self):
        self.cap.release()

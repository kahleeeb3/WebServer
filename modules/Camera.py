import cv2

class FrameCapture:
    def __init__(self, camera_index=0, frame_size=(640, 480)):
        self.camera_index = camera_index
        self.frame_size = frame_size
        self.cap = None
    
    def start(self):
        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            raise RuntimeError("Error: could not open camera.")
        
    def get_frame_data(self) -> bytes:
        # Check capture available
        if self.cap is None:
            raise RuntimeError("Camera not initialized. Call open() first.")
        
        # capture a single frame
        success, frame = self.cap.read()
        if not success:
            raise RuntimeError("Failed to read frame")
        
        # Encode as JPG
        success, frame_data = cv2.imencode('.jpg', frame)
        if not success:
            raise RuntimeError("Failed to encode frame as JPEG")

        return frame_data.tobytes()

    def stop(self):
        if self.cap is not None:
            self.cap.release()
            self.cap = None
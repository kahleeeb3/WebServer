from webserver_helper import WebServer, VideoChannel
from FrameCapture import *

server = WebServer()
server_camera = VideoChannel(server.app, "/camera")
server.start()

camera = FrameCapture()
camera.start()

try:
    while True:
        camera_frame = camera.get_frame_data(quality=20) # increase quality as needed
        server_camera.update(camera_frame)

except Exception as e:
    print(e)
except KeyboardInterrupt as e:
    print("User Exited Application")
finally:
    camera.stop()
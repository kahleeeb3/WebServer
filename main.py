from modules.WebServer import *
from modules.Camera import *

# configure server
server = WebServer()
server_video0 = VideoChannel(server.app, "/video0")
server.start()

# configure camera
camera = FrameCapture()
camera.start()



try:
    while True:

        # update video
        video0_frame = camera.get_frame_data()
        server_video0.update(video0_frame)

except Exception as e:
    print(e)
except KeyboardInterrupt as e:
    print("User Exited Application")
finally:
    camera.stop()
from modules.WebServer import *
from modules.Camera import *
from modules.Plot import *
import time

# configure server
server = WebServer()
server_video0 = VideoChannel(server.app, "/video0")
server_plot = VideoChannel(server.app, "/plot")
text_channel = TextChannel(server.app, "/status")
server.start()

# configure camera
camera = FrameCapture()
camera.start()

# configure plot
plot = RandomScatterPlot()
start_time = time.time()


try:
    while True:
        
        # update the plot
        plot.update()
        plot_frame = plot.get_frame_data(quality=20)
        server_plot.update(plot_frame)

        # update video
        video0_frame = camera.get_frame_data(quality=20)
        server_video0.update(video0_frame)

        # update test
        text_channel.update(f'Server Up Time: {time.time()-start_time}')

except Exception as e:
    print(e)
except KeyboardInterrupt as e:
    print("User Exited Application")
finally:
    camera.stop()
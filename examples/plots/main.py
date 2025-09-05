from webserver_helper import WebServer, VideoChannel
from RandomScatterPlots import *

server = WebServer()
plot = RandomScatterPlot()
server_plot = VideoChannel(server.app, "/plot")
server.start()

while True:
    plot.update()
    plot_frame = plot.get_frame_data(quality=20) # increase quality as needed
    server_plot.update(plot_frame)
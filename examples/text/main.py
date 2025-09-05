from webserver_helper import WebServer, TextChannel
import time

server = WebServer()
text = TextChannel(server.app, "/text")
server.start()
start = time.time()

while True:
    end = time.time()
    text.update(f"Server Up Time: {end-start}")
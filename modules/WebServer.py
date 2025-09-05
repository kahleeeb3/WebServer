from flask import Flask, render_template, Response
from werkzeug.serving import make_server
import threading

class WebServer:
    def __init__(self, host="0.0.0.0", port=5000):
        self.host = host
        self.port = port
        self.app = Flask(__name__, template_folder='./server/', static_folder='./server/')
        self._server = None
        self._thread = None

        @self.app.route("/")
        def index():
            return render_template("index.html")
    
    def start(self):
        # if server is alive, skip
        if self._thread and self._thread.is_alive():
            print("Server [Warning]: Server is Already Running")
            return
        
        # Start the thread
        self._server = make_server(self.host, self.port, self.app, threaded=True, passthrough_errors=True)
        self._thread = threading.Thread(
            target=self._server.serve_forever,
            daemon=True
        )
        self._thread.start()
        print(f"Server running at: http://{self.host}:{self.port}")

class VideoChannel:
    def __init__(self, app: Flask, route: str):
        self.app = app
        self.route = route
        self.latest_data = None
        self.frame_num = 0
        self.condV = threading.Condition()
        self._register()

    def _register(self):
        def video_feed():
            return Response(
                self._stream_thread(),
                mimetype="multipart/x-mixed-replace; boundary=frame"
            )
        self.app.add_url_rule(self.route, endpoint=self.route.strip('/'), view_func=video_feed)

    def update(self, frame_data:bytes):
        with self.condV:
            self.latest_data = frame_data
            self.frame_num += 1
            self.condV.notify_all()

    def _stream_thread(self):
        last_sent = -1
        while True:
            with self.condV:
                self.condV.wait_for(
                    lambda: self.latest_data is not None and self.frame_num != last_sent, timeout=1.0
                )
                if self.latest_data is None or self.frame_num == last_sent:
                    continue # no new frame, wait again
                frame_data = self.latest_data
                last_sent = self.frame_num
                yield (b"--frame\r\n"
                   b"Content-Type: image/jpeg\r\n"
                   b"Content-Length: " + str(len(frame_data)).encode() + b"\r\n\r\n" +
                   frame_data + b"\r\n")
                
class TextChannel:
    def __init__(self, app: Flask, route: str):
        self.app = app
        self.route = route
        self.latest_text = ""
        self.update_num = 0
        self.condV = threading.Condition()
        self._register()

    def _register(self):
        def text_feed():
            return Response(self._stream_thread(), mimetype="text/event-stream")

        # Make endpoint unique
        self.app.add_url_rule(self.route, endpoint=self.route.strip('/'), view_func=text_feed)

    def update(self, new_text: str):
        """Update the text sent to clients."""
        with self.condV:
            self.latest_text = new_text
            self.update_num += 1
            self.condV.notify_all()

    def _stream_thread(self):
        """Generator that yields updated text using SSE."""
        last_sent = -1
        while True:
            with self.condV:
                self.condV.wait_for(lambda: self.update_num != last_sent, timeout=1.0)
                if self.update_num == last_sent:
                    continue
                last_sent = self.update_num
                yield f"data: {self.latest_text}\n\n"
    

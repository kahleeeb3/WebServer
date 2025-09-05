from flask import Flask, render_template
from werkzeug.serving import make_server
from threading import Thread

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
        self._thread = Thread(
            target=self._server.serve_forever,
            daemon=True
        )
        self._thread.start()
        print(f"Server running at: http://{self.host}:{self.port}")

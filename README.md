# WebServer-Helper
Lightweight wrapper around a Python Flask server, designed to run a background web server for displaying data from code in headless environments.

## Setup
```
mkdir modules, server
```
```
New-Item -ItemType File server/index.html
```
```bash
python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate
python -m pip install --upgrade pip
```
```bash
git clone https://github.com/kahleeeb3/WebServer-Helper.git modules/WebServer-Helper
cd modules/WebServer-Helper
pip install -e .
cd ../../
```
```
project/
├─ modules/
│  └─ webserver_helper/
├─ server/
│  └─ index.html
└─ main.py
```
```json
// Remove package not found error in VSCode
// .vscode/settings.json
{
    "python.analysis.extraPaths": [
        "./WebServer-Helper"
    ]
}
```
## Example
```python
# main.py
from webserver_helper import WebServer, TextChannel
import time

server = WebServer()
text = TextChannel(server.app, "/text")
server.start()
start = time.time()

while True:
    end = time.time()
    text.update(f"Server Up Time: {end-start}")
```
```html
<!-- index.html -->
 <head>
    <title>WebServer</title>
    <script>
        const evtSource = new EventSource("/text");
        evtSource.onmessage = function (e) {
            document.getElementById("text").innerText = e.data;
        };
    </script>
</head>

<h1>Hello World</h1>
<p id="text"></p>
```

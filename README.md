# WebServer-Helper
Lightweight wrapper around a Python Flask server, designed to run a background web server for displaying data from code in headless environments.

## Setup
```bash
# On Windows
python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate
python -m pip install --upgrade pip
```
```bash
git clone https://github.com/kahleeeb3/WebServer-Helper.git
cd WebServer-Helper
pip install -e .
cd ../
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

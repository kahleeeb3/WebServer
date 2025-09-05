# WebServer-Helper
Lightweight wrapper around a Python Flask server, designed to run a background web server for displaying data from code in headless environments.

## 🛠️ Suggested Development Environment
I suggest using a virtual environment and the following folder structure:
```
project/
├─ modules/
│  └─ webserver_helper/
├─ server/
│  └─ index.html
└─ main.py
```

### 1. Create a Virtual Environment
```bash
# For Windows PS
python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate
python -m pip install --upgrade pip
```
```bash
# For Linux Bash
python -m venv venv
source env/bin/activate
python -m pip install --upgrade pip
```

### 2. Clone and Install Repository
```bash
git clone https://github.com/kahleeeb3/WebServer-Helper.git modules/WebServer-Helper
cd modules/WebServer-Helper
pip install -e .
cd ../../
```

### 3. Fix VSCode Error (Optional)
If using VSCode, you need to add this to your `.vscode/settings.json` file:
```json
{
    "python.analysis.extraPaths": [
        "./modules/WebServer-Helper"
    ]
}
```

## 📂 Examples
Check out the [examples](./examples/) folder for general usage demonstrations. 

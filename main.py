import os
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

now = datetime.now()
path = Path(os.getenv("repo_path"))

os.chdir(path)

os.makedirs("log", exist_ok=True)
with open("log/logs.txt", "a") as f:
    f.write(f"A new commit done on {now.strftime('%Y-%m-%d %H:%M:%S')}\n\n")



os.system("git add .")
os.system(f"git commit -m \"This commit is done on {now.strftime('%Y-%m-%d %H:%M:%S')}\"")
os.system("git push -u origin main")
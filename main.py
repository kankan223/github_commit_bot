import os
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

now = datetime.now()
path = os.getenv("path")

os.chdir(path)



os.system("git add .")
os.system(f"git commit -m \"This commit is done on {now.strftime("%Y-%m-%d %H:%M:%S")}\"")
os.system("git push -u origin main")
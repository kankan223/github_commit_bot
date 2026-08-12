# exec(open('script.sh').read())   

import os
from datetime import datetime

now = datetime.now()

os.system("git add .")
os.system(f"git commit -m \"This commit is done on {now.strftime("%Y-%m-%d %H:%M:%S")}\"")
os.system("git push -u origin main")
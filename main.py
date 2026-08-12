# exec(open('script.sh').read())   

import os
from datetime import datetime

now = datetime.now()

os.system("git add .")
os.system(f"git commit -m \"this commit is done on {now.strftime("%Y-%m-%d %H:%M:%S")}\"")
# os.system("git add .")
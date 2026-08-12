# exec(open('script.sh').read())   

import os
import datetime

os.system("git add .")
os.system(f"git commit -m \"this commit is done on {datetime.datetime}\"")
# os.system("git add .")
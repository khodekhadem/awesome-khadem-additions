import os
import subprocess
output = subprocess.check_output("setxkbmap -query", shell=True)
output = output.decode("utf-8")

if (output[48:53] == "ir,us"):
    os.system("setxkbmap us,ir")
if (output[48:53] == "us,ir"):
    os.system("setxkbmap ir,us")


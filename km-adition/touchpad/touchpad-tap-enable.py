import os
import subprocess
import sys

command_file = "~/.config/awesome/km-adition/touchpad/touchpad-tap-enable.sh"
zir_dastoor = str(sys.argv[1])

if zir_dastoor == "enable":
    os.system("~/.config/awesome/km-adition/touchpad/touchpad-tap-enable.sh")

elif zir_dastoor == "first-set":
    output = subprocess.check_output("xinput --list", shell=True)
    output = output.decode("utf-8")
    a = output.find("Touchpad")
    b = output.rfind("↳",0,322)
    # xinput set-prop "ELAN1200:00 04F3:306F Touchpad" "libinput Tapping Enabled" 1
    output ='xinput set-prop "'+output[b+2:a]+'Touchpad'+'" "libinput Tapping Enabled" 1'
    os.system("echo {} > {}".format(output,command_file))

elif zir_dastoor == "help" or zir_dastoor == "-h" or zir_dastoor == "--help" or zir_dastoor ==  "-help" or zir_dastoor ==  "--h" :
    print("""

    ##-----help-----##
python3 this-script-name.py --help   ===> show this page
python3 this-script-name.py first-set   ===> set touchpad name (tashkhis model touchpad)
python3 this-script-name.py enable      ===> enable 2tap instead of right click  (roshan kardan 2zarbe baraye click rast)


            """)



import os
import subprocess
import sys

zir_dastoor = str(sys.argv[1])
output = subprocess.check_output('xrandr --prop --verbose | grep -A10 " connected" | grep "Brightness"', shell=True)
output = output.decode("utf-8")
a = output.find('Brightness')
output = output[a+12:]
output = float(output)
now_bright = output
print(output)
main_display = subprocess.check_output('cat ~/.config/awesome/km-adition/change-brightness/display.txt', shell=True)
main_display = main_display.decode("utf-8")
main_display = main_display[:len(main_display)-1]

display = subprocess.check_output('xrandr | grep " connected" | cut -f1 -d " "', shell=True)
display = display.decode("utf-8")
if zir_dastoor == "help" or zir_dastoor == "-h" or zir_dastoor == "--help" or zir_dastoor ==  "-help" or zir_dastoor ==  "--h" :
    print("""

    ##-----help-----##
python3 this-script-name.py --help       ===> this page
python3 this-script-name.py first-set    ===> set monitor name (tashkhis model safe namayesh)
python3 this-script-name.py down         ===> decrease brightness (noor kam mishe)
python3 this-script-name.py up           ===> increase brightness (noor ziyad mishe)
python3 this-script-name.py brightness   ===> show current brightness (namayesh mizan noor safe namayesh)


            """)
if zir_dastoor == "first-set" :
    display = subprocess.check_output('xrandr | grep " connected" | cut -f1 -d " "', shell=True)
    display = display.decode("utf-8")
    display = "echo "+display[:len(display)-1]+" > ~/.config/awesome/km-adition/change-brightness/display.txt"
    print(display)
    os.system(display)

if zir_dastoor == "brightness":
    os.system('xrandr --prop --verbose | grep -A10 " connected" | grep "Brightness"')

if zir_dastoor == "down" :
    if now_bright > 0.2 :
        output = "xrandr --output {} --brightness {}".format(main_display, output-0.05)
        os.system(output)
        print(output)
    else:
        print("az mahdoode kharej shodi")
if zir_dastoor == "up" :
    if now_bright < 1.0 :
        output = "xrandr --output {} --brightness {}".format(main_display, output+0.05)
        os.system(output)
    else:
        print("az mahdoode kharej shodi")

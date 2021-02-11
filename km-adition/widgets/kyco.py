import os
os.system("acpi")
#os.system('echo -e "\e[92m-----------"')
os.system("echo -------------------------------------------------------")
os.system('xrandr --prop --verbose | grep -A10 " connected" | grep "Brightness"|cut -c 2-')
os.system("echo -------------------------------------------------------")
os.system('amixer get Master | grep % | cut -c 3-')

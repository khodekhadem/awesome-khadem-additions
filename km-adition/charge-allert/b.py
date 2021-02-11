import tkinter as tk
import subprocess
import time
quit_text = """
 Quit 
"""
output = subprocess.check_output("acpi", shell=True)
output = output.decode("utf-8")
output_org = output
darsadplace = output.find("%")
output = output[darsadplace-2:darsadplace+1]
#print(output)
#output = "15%"
if output_org.find("charging") != -1 :
	if  output=='14%' or output=='13%'or output==' 8%'or output==' 7%':
	        time.sleep(1)
	        if output=='14%' or output=='13%'or output==' 8%'or output==' 7%':
	                mw = tk.Tk()
	                mw.option_add("*Button.Background", "black")
	                mw.option_add("*Button.Foreground", "red")
	                mw.title('The game')
	                mw.geometry("500x250")
	                mw.resizable(0, 0)
	                back = tk.Frame(master=mw,bg='red')
	                back.pack_propagate(0)
	                back.pack(fill=tk.BOTH, expand=1)

	                info = tk.Label(
	                        master=back,
	                        text='  battery is running low  ',
	                        font=("Courier", 28),
	                        bg='red',
	                        fg='black'
	                        )
	                info.pack()

	                info = tk.Label(
	                        master=back,
	                        text=output,
	                        font=("Courier", 50),
	                        bg='red',
	                        fg='black'
	                        )
	                info.pack()

	                info = tk.Label(
	                        master=back,
	                        text='connet charger',
	                        font=("Courier", 28),
	                        bg='red',
	                        fg='black'
	                        )
	                info.pack()
	                close = tk.Button(master=back,
	                        text=quit_text,
	                        font=("Courier", 21),
	                        command=mw.destroy
	                        )
	                close.pack()
	                mw.mainloop()
	else:
	        print(output_org)

import tkinter as tk
import subprocess
import os
import sys


def set_keyrate():
    delay = delay_entry.get()
    rate = rate_entry.get()
    try:
        # Get the directory of the current executable
        exe_dir = os.path.dirname(sys.executable)
        # Construct the path to keyrate.exe
        keyrate_path = os.path.join(exe_dir, "keyrate.exe")
        # Call the keyrate.exe with the delay and rate as command line arguments
        subprocess.check_call([keyrate_path, delay, rate])
        status_label.config(text="Keyrate set successfully")
    except subprocess.CalledProcessError:
        status_label.config(text="Failed to set keyrate")


root = tk.Tk()

delay_label = tk.Label(root, text="Delay (Windows Default is around 200):")
delay_label.pack()
delay_entry = tk.Entry(root)
delay_entry.pack()

rate_label = tk.Label(root, text="Rate (Windows Default is around 30):")
rate_label.pack()
rate_entry = tk.Entry(root)
rate_entry.pack()

set_button = tk.Button(root, text="Set Keyrate", command=set_keyrate)
set_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.geometry("500x120")

root.mainloop()

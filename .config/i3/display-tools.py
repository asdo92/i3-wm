#!/usr/bin/env python3

import tkinter as tk
import os
import psutil

def check_process_running(process_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            return True
    return False

class MainWindow:
  def __init__(self, master):
    self.master = master
    master.title("Display-Tools.py")

    # Set theme and window size
    master.configure(bg='#23283f')
    master.geometry('350x315')

    self.boton1 = tk.Button(master, text="Run ARandR", command=self.exec_command1, bg='#205d2c', fg="white")
    self.boton1.pack(side=tk.TOP, pady=10)

    self.boton2 = tk.Button(master, text="Run ~/.config/i3/startxrandr.sh", command=self.exec_command2, bg='#205d2c', fg="white")
    self.boton2.pack(side=tk.TOP, pady=10)

    self.boton3 = tk.Button(master, text="Run xfce4-screenshooter", command=self.exec_command3, bg='#205d2c', fg="white")
    self.boton3.pack(side=tk.TOP, pady=10)

    self.boton6 = tk.Button(master, text="Run SimpleScreenRecorder", command=self.exec_command6, bg='#205d2c', fg="white")
    self.boton6.pack(side=tk.TOP, pady=10)

    self.boton4 = tk.Button(master, text="Start/Restart Conky i3", command=self.exec_command4, bg='#205d2c', fg="white")
    self.boton4.pack(side=tk.TOP, pady=10)
    
    self.boton5 = tk.Button(master, text="Exit", command=self.exec_command5, bg='#205d2c', fg="white")
    self.boton5.pack(side=tk.TOP, pady=10)

    # Set center buttons
    self.boton1.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH)
    self.boton2.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH)
    self.boton3.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH)
    self.boton4.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH)
    self.boton5.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH)
    self.boton6.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH)

  def exec_command1(self):
    print('# Run ARandR')
    command = "arandr"
    os.system(command)

  def exec_command2(self):
    print('# Run ~/.config/i3/startxrandr.sh')
    command = "killall startxrandr.sh"
    os.system(command)
    command = " ~/.config/i3/startxrandr.sh &"
    os.system(command)

  def exec_command3(self):
    print('# Run xfce4-screenshooter"')
    command = "xfce4-screenshooter"
    os.system(command)

  def exec_command6(self):
    print('# Run SimpleScreenRecorder"')
    command = "simplescreenrecorder"
    os.system(command)

  def exec_command4(self):
    print('# Start/Restart Conky i3')
    command = "killall conky && sleep 1"
    os.system(command)
    command = "conky -c ~/.config/conky/conkyrc_i3 &"
    os.system(command)

  def exec_command5(self):
    command = "exit"
    os.system(command)
    exit()

root = tk.Tk()
window = MainWindow(root)
root.mainloop()

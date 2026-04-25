#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog
import utils
import shutil
import numpy as np
import os

max_value = 1
min_value = 0
current_value = 0

def up_button():
    global current_value
    current_value = (current_value + 1) % len(Stacked_frames)
    Stacked_frames[current_value].tkraise()

def down_button():
    global current_value
    current_value = (current_value - 1) % len(Stacked_frames)
    Stacked_frames[current_value].tkraise()

def button_press():
    current_path = os.getcwd()
    base_dir = os.path.join(current_path, "Rocket Launch Data sets")
    folder_name_start = "Launch_Data_#"
    folder_path = utils.create_folder(base_dir, folder_name_start)
    file_path = open_file(folder_path)
    if os.path.getsize(file_path) == 0:
        print("File is empty")
        return
    else:
        data = np.genfromtxt(file_path, delimiter=",", skip_header=2, names=True)
        time = data["time"]
        temp = data["temp"]
        pressure = data["pressure"]
        humidity = data["humidity"]
    utils.plot_tvt(folder_path, time, temp)
    utils.plot_pvt(folder_path, time, pressure)
    utils.plot_hvt(folder_path, time, humidity)


def open_file(folder_path):
    file_path = filedialog.askopenfilename(title = "Select a Text File",
    filetypes = (("Text files", "*.txt"),))
    if file_path:
        file_name.config(text=f"Selected: {file_path}")
        file_path = shutil.move(file_path, folder_path)
    return file_path



#root setup
root = tk.Tk()
root.title("Data Processing")
root.attributes('-fullscreen', True)
root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))
root.overrideredirect(True)
root.configure(background='gray54')

#topframe
top_frame = tk.Frame(root, bg='gray26', height='40')
top_frame.pack_propagate(False)
top_frame.pack(side="top", fill="x")
#top frame widgets
top_format = {"font": ("Terminal", 12), "bg": "gray26", "fg": "gray54", 'relief': 'flat', 'activebackground': 'red', 'borderwidth': '0'}
title_label = tk.Label(top_frame, text='Time vs Altitude', **top_format)
exit_btn = tk.Button(top_frame, text = 'X', command = root.destroy, **top_format, width=3)
#widget placement
title_label.pack(side="left")
exit_btn.pack(side='right', anchor='e')

#btm_frame
btm_frame = tk.Frame(root, bg='gray26', height='200')
btm_frame.pack_propagate(False)
btm_frame.pack(side="bottom", fill="x")
#btm_widgets
btm_format = {"font": ("Terminal", 12), "bg": "gray26", "fg": "gray54", 'relief': 'flat', 'borderwidth': '0'}
switch_left_btn = tk.Button(btm_frame, command = down_button, text = '<', **btm_format, width=3)
switch_right_btn = tk.Button(btm_frame, command = up_button, text = '>', **btm_format, width=3)
select_file_btn = tk.Button(btm_frame, text = 'Select File', **btm_format, command = button_press)
file_name = tk.Label(btm_frame, **btm_format)
#widget placement
switch_left_btn.pack(side='left', anchor='n')
switch_right_btn.pack(side='left', anchor='n')
select_file_btn.pack(side='right', anchor='n')
file_name.pack(side='right', anchor='n')


#center frame
cen_frame = tk.Frame(root, bg='gray1')
cen_frame.pack(side="bottom", expand=True, fill="both")
#stacked frames
TvA_frame = tk.Frame(cen_frame, bg='gray54')
TvA_frame.place(relwidth=1, relheight=1)
wip = tk.Label(TvA_frame, text='WIP', **top_format)
wip.pack()

TvAc_frame = tk.Frame(cen_frame, bg='gray30')
TvAc_frame.place(relwidth=1, relheight=1)
wip2 = tk.Label(TvAc_frame, text='WIP2', **top_format)
wip2.pack()



Stacked_frames = [TvA_frame, TvAc_frame]
Stacked_frames[current_value].tkraise()

root.mainloop()
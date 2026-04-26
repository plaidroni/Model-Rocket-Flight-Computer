#!/usr/bin/env python3
import tkinter as tk
import utils
import os
from PIL import Image, ImageTk
import json

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

with open(os.path.join(script_dir, 'graph_settings.json'), 'r') as file:
    settings = json.load(file)

current_value = 0
max_altitude = 10000

def up_button():
    global current_value
    current_value = (current_value + 1) % len(Stacked_frames)
    Stacked_frames[current_value].tkraise()

def down_button():
    global current_value
    current_value = (current_value - 1) % len(Stacked_frames)
    Stacked_frames[current_value].tkraise()

def open_btn():
    global settings
    txt_file = utils.open_file()
    folder = utils.create_graphs(txt_file, settings)
    load_graphs(folder)


def view_btn():
    load_graphs(utils.open_folder())

def load_graphs(folder):
    labels = [wip, wip2, wip3]
    names = ["graph1.png", "graph2.png", "graph3.png"]

    images = []

    for label, name in zip(labels, names):
        img = Image.open(os.path.join(folder, name))
        photo = ImageTk.PhotoImage(img)
        label.config(image=photo)
        label.image = photo
        images.append(photo)


#root setup
root = tk.Tk()
root.title("Data Processing")
root.attributes('-fullscreen', True)
root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))
root.overrideredirect(True)
root.configure(background='gray54')

#topframe
top_frame = tk.Frame(root, bg='gray26', height='40', relief='solid', borderwidth = 1,)
top_frame.pack_propagate(False)
top_frame.pack(side="top", fill="x")
#top frame widgets
top_format = {"font": ("Terminal", 12), "bg": "gray26", "fg": "gray54", 'relief': 'flat', 'activebackground': 'red', 'borderwidth': '0'}
title_label = tk.Label(top_frame, text='Rocket Launch Data Visualizer', **top_format)
exit_btn = tk.Button(top_frame, text = 'X', command = root.destroy, **top_format, width=3)
#widget placement
title_label.pack(side="left")
exit_btn.pack(side='right', anchor='e')

#btm_frame
btm_frame = tk.Frame(root, bg='gray26', height='200', relief='solid', borderwidth = 1)
btm_frame.pack_propagate(False)
btm_frame.pack(side="bottom", fill="x")
#btm_widgets
btm_format = {"font": ("Terminal", 12), "bg": "gray26", "fg": "gray54", 'relief': 'flat', 'borderwidth': '0'}
switch_left_btn = tk.Button(btm_frame, command = down_button, text = '<', **btm_format, width=3)
switch_right_btn = tk.Button(btm_frame, command = up_button, text = '>', **btm_format, width=3)

select_file_btn = tk.Button(btm_frame, text = 'Upload Data', **btm_format, command = open_btn)
select_folder_btn = tk.Button(btm_frame, text = 'View Data', **btm_format, command = view_btn)
file_name = tk.Label(btm_frame, **btm_format)
#widget placement
switch_left_btn.pack(side='left', anchor='n')
switch_right_btn.pack(side='left', anchor='n')

select_file_btn.pack(side='right', anchor='n')
select_folder_btn.pack(side='right', anchor='n')
file_name.pack(side='right', anchor='n')

#side frame
side_frame = tk.Frame(root, bg='gray26', width='200',)
side_frame.pack_propagate(False)
side_frame.pack(side="left", fill="y")
#side widgets
side_format = {"font": ("Terminal", 12), "bg": "gray26", "fg": "gray54", 'relief': 'flat', 'borderwidth': '0'}
max_alt_label = tk.Label(side_frame, **side_format, text = f'Apogee={max_altitude} m')
dlable1 = tk.Label(side_frame, **side_format, text = f'data1={max_altitude} m')
dlable2 =tk.Label(side_frame, **side_format, text = f'data2={max_altitude} m')
dlable3 =tk.Label(side_frame, **side_format, text = f'data3={max_altitude} m')
dlable4 =tk.Label(side_frame, **side_format, text = f'data4={max_altitude} m')
#widget placement
max_alt_label.pack(side="top")
dlable1.pack(side="top")
dlable2.pack(side="top")
dlable3.pack(side="top")
dlable4.pack(side="top")

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

TvAcc_frame = tk.Frame(cen_frame, bg='gray30')
TvAcc_frame.place(relwidth=1, relheight=1)
wip3 = tk.Label(TvAcc_frame, text='WIP3', **top_format)
wip3.pack()



Stacked_frames = [TvA_frame, TvAc_frame, TvAcc_frame]
Stacked_frames[current_value].tkraise()

root.mainloop()
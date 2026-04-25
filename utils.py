#!/usr/bin/env python3
from matplotlib import pyplot as plt
from tkinter import filedialog
import shutil
import numpy as np
import os
import math

base_dir = os.path.join(os.getcwd(), "Rocket Launch Data sets")



def create_folder():
    global base_dir
    os.makedirs(base_dir,exist_ok=True)
    existing_folders = [
        name for name in os.listdir(base_dir)
        if os.path.isdir(os.path.join(base_dir, name)) and name.startswith('Launch_Data_#')
    ]
    next_number = len(existing_folders)+ 1
    folder_name = f"Launch_Data_#{next_number:03d}"
    folder_path = os.path.join(base_dir,folder_name)
    os.makedirs(folder_path)
    return folder_path


def open_file():
    path = filedialog.askopenfilename(title="Select a Text File", filetypes=(("Text files", "*.txt"),))
    return path

def open_folder():
    global base_dir
    path = filedialog.askdirectory(initialdir=base_dir, title="Select a Folder")
    return path

def create_graphs(txt_file, settings):
    folder_path = create_folder()
    txt_file = shutil.move(txt_file, folder_path)
    data = np.genfromtxt(txt_file, delimiter=",", skip_header=2, names=True)
    #name data
    time = data["time"]
    temp = data["temp"]
    pressure = data["pressure"]
    altitude = calc(pressure)
    air_density = calc(temp)
    #create data based on settings
    save_fig(plot_graph(time, temp, settings, "time", "temp", "time vs temp"), folder_path, "graph1.png")
    save_fig(plot_graph(time, altitude, settings, "altitude", "time", "altitude vs time"), folder_path, "graph2.png")
    save_fig(plot_graph(altitude, air_density, settings, altitude, air_density, "altitude vs air_density"), folder_path, "graph3.png")
    return folder_path

def plot_graph(x, y, settings, ylabel, xlabel, label):
    plt.style.use(settings["style"])
    fig, ax = plt.subplots()

    if settings["graph_type"] == "line":
        ax.plot(x, y, color=settings["color"], label = label)

    elif settings["graph_type"] == "scatter":
        ax.scatter(x, y, color=settings["color"], label = label)

    elif settings["graph_type"] == "bar":
        ax.bar(x, y, color=settings["color"], label = label)

    ax.set_title(settings["title"])
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if settings["legend"]:
        ax.legend()

    if settings["grid"]:
        ax.grid()

    return fig

def save_fig(fig, folder_path, file_name):
    path = os.path.join(folder_path, file_name)
    fig.savefig(path)
    plt.close(fig)
    return path

def calc(pressure):
    altitude = 44330 * (1 - pow(pressure / 101.325, 1 / 5.255))
    return altitude

def calc2(temp, humidity, pressure):
    a = 0.61078
    b = 17.27
    c = 237.3
    svp = a*math.exp((b*temp)/(temp+c))
    p_v = (humidity/100)*svp
    p_d = pressure
    sgca = 287.05
    sgcv = 461.495

    temp_k=temp+273.15
    air_density = (p_d/sgca*temp_k)+(p_v/sgcv*temp_k)
    print("air density",air_density)
    return air_density

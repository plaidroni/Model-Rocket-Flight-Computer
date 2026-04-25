from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
#!/usr/bin/env python3
import os




def create_folder(base_dir, folder_name_start):

    os.makedirs(base_dir,exist_ok=True)
    existing_folders = [
        name for name in os.listdir(base_dir)
        if os.path.isdir(os.path.join(base_dir, name)) and name.startswith(folder_name_start)
    ]
    next_number = len(existing_folders)+ 1
    folder_name = f"{folder_name_start}{next_number:03d}"
    folder_path = os.path.join(base_dir,folder_name)
    os.makedirs(folder_path)
    return folder_path

def plot_tvt(folder_path, time, temp):
    tvt_plot_file = os.path.join(folder_path, "temperature_plot.png")
    fig, ax = plt.subplots()
    ax.plot(time, temp, label="Temperature", color='red')
    ax.set_title("Temperature vs Time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Temp")
    ax.legend()
    ax.grid()

    plt.savefig(tvt_plot_file)
    plt.show()
    return fig

def plot_pvt(folder_path, time, pressure):
    pvt_plot_file = os.path.join(folder_path, "pressure_plot.png")
    plt.figure()
    plt.plot(time, pressure, label="pressure (°C)", color='red')
    plt.xlabel("Time")
    plt.ylabel("pressure")
    plt.title("pressure vs Time")
    plt.legend()
    plt.grid()

    plt.savefig(pvt_plot_file)
    plt.show()
    return pvt_plot_file

def plot_hvt(folder_path, time, humidity):
    hvt_plot_file = os.path.join(folder_path, "humidity_plot.png")
    plt.figure()
    plt.plot(time, humidity, label="humidity (°C)", color='red')
    plt.xlabel("Time")
    plt.ylabel("humidity")
    plt.title("humidity vs Time")
    plt.legend()
    plt.grid()

    plt.savefig(hvt_plot_file)
    plt.show()
    return hvt_plot_file

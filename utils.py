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
    plot_file = os.path.join(folder_path, "temperature_plot.png")
    plt.figure()
    plt.plot(time, temp, label="Temperature (°C)", color='red')
    plt.xlabel("Time")
    plt.ylabel("Temperature")
    plt.title("Temperature vs Time")
    plt.legend()
    plt.grid()

    plt.savefig(plot_file)
    plt.show()

def plot_pvt(folder_path, time, pressure):
    plot_file = os.path.join(folder_path, "pressure_plot.png")
    plt.figure()
    plt.plot(time, pressure, label="pressure (°C)", color='red')
    plt.xlabel("Time")
    plt.ylabel("pressure")
    plt.title("pressure vs Time")
    plt.legend()
    plt.grid()

    plt.savefig(plot_file)
    plt.show()

def plot_hvt(folder_path, time, humidity):
    plot_file = os.path.join(folder_path, "humidity_plot.png")
    plt.figure()
    plt.plot(time, humidity, label="humidity (°C)", color='red')
    plt.xlabel("Time")
    plt.ylabel("humidity")
    plt.title("humidity vs Time")
    plt.legend()
    plt.grid()

    plt.savefig(plot_file)
    plt.show()

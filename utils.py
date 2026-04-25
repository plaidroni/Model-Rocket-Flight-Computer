from skimage import io, color
import numpy as np
from PIL import Image
from datetime import datetime
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
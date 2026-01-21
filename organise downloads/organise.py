#!/usr/bin/env python3
import os
import shutil

def organize_folder(folder):
    file_types = {
        'Images': ['.jpeg', '.jpg', '.png', '.gif', '.webp', '.tiff', '.gif',],
        'Videos': ['.mp4', '.avi', '.mov', '.webm',],
        'Documents': ['.pdf', '.docx', '.txt', '.md', '.text', '.html', '.xls', '.csv',],
        'Archives': ['.zip', '.rar',],
        'Music': ['.mp3', '.opus', '.flac', '.m4a', '.m4b', '.mp4', '.aac', '.3gp', '.3g2', '.mp4a',],
        'Iso Images': ['.iso', '.img',],
        'Linux': ['.deb',],
    }

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            for folder_name, extensions in file_types.items():
                if ext in extensions:
                    target_folder = os.path.join(folder, folder_name)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    print(f'Moved {filename} to {folder_name}')

organize_folder('/home/lee/Downloads')


import os
import shutil
import datetime
import schedule
import time

source_dir = r"C:/Users/User/Pictures/Screenshots"
destination_dir = r"C:/Users/User/Desktop/Backups"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    if os.path.exists(dest_dir):
        print(f"Backup already exists: {dest_dir}")
        return

    shutil.copytree(source, dest_dir)
    print(f"Folder copied to: {dest_dir}")

schedule.every().day.at("10:15").do(copy_folder_to_directory, source_dir, destination_dir)

while True:
    schedule.run_pending()
    time.sleep(1)

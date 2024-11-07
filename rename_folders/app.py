import os
import shutil
from dotenv import load_dotenv

# load .env-file
load_dotenv()


# load paths from env-file
base_path = os.getenv('BASE_PATH')
target_path = os.getenv('TARGET_PATH')
increment = 1400000  # value to add to foldername


# load id's from ignore file
with open('ignore.txt', 'r') as f:
    move_ids = [line.strip() for line in f if line.strip().isdigit()]

# add counting for testing
processed_count = 0
max_processed = 10000

# loop through folders
for folder_name in os.listdir(base_path):

    folder_path = os.path.join(base_path, folder_name)
    
    # check if it is a folder and has a digit name
    if os.path.isdir(folder_path) and folder_name.isdigit():
        
        folder_number = int(folder_name)
        
        # safty check: is folder_number less then increment value
        if folder_number < increment:
            
            # new folder name
            new_folder_name = str(folder_number + increment)
            new_folder_path = os.path.join(base_path, new_folder_name)
            
            # rename folder
            os.rename(folder_path, new_folder_path)
            print(f"{folder_name} renamed to {new_folder_name}")
            
            # check if old foldername is in move_ids (list with ignored values)
            if folder_name in move_ids:
                # move folder to target_path
                target_folder_path = os.path.join(target_path, new_folder_name)
                shutil.move(new_folder_path, target_folder_path)
                print(f"{new_folder_name} moved to {target_folder_path}")
            
            # increment counting
            processed_count += 1
            if processed_count >= max_processed:
                print("stop. max loops are reached")
                break
        else:
            print(f"{folder_name} already increased")
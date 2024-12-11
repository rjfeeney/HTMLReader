import os
import shutil

def copy_to_public(source_dir: str, destination_dir: str) -> None:
    contents = os.listdir(source_dir)
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
    os.mkdir(destination_dir)
    for item in contents:
        full_path = os.path.join(source_dir, item)
        if os.path.isfile(full_path):
            print(f"Copying {item}")  # Debug statement
            destination_path = os.path.join(destination_dir, item)
            shutil.copy(full_path, destination_path)
        else:
            new_directory = os.path.join(destination_dir, item)
            os.mkdir(new_directory)
            copy_to_public(full_path, new_directory)
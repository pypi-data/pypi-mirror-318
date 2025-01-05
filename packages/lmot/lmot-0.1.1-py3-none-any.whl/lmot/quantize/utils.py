import os
import shutil
import logging

logger = logging.getLogger(__name__)

def copy_end_with_str_files(file_end_with_str, source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for filename in os.listdir(source_dir):
        if filename.endswith(file_end_with_str):
            source_file = os.path.join(source_dir, filename)
            target_file = os.path.join(target_dir, filename)
            if os.path.exists(target_file):
                continue
            shutil.copy(source_file, target_file)

def safe_make_dir(dir_path):
    if os.path.exists(dir_path):
        logging.info(f"Path {dir_path} already exists, removing it.")
        shutil.rmtree(dir_path)

    os.makedirs(dir_path, exist_ok=True)
import os
import shutil
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("python-dotenv is not installed. Please install it with 'pip install python-dotenv'.")
    sys.exit(1)

def clear_directory(directory):
    """Deletes all files and subdirectories in the given directory."""
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
        else:
            os.remove(item_path)

def copy_directory(src, target):
    """Copies all files and subdirectories from src to target."""
    if not os.path.exists(src):
        print(f"The source directory {src} does not exist.")
        return

    # Clear target directory if it exists, else create it
    if os.path.exists(target):
        clear_directory(target)
    else:
        os.makedirs(target)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        target_path = os.path.join(target, item)

        if os.path.isdir(src_path):
            shutil.copytree(src_path, target_path, dirs_exist_ok=True)
        else:
            shutil.copy2(src_path, target_path)

if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env file

    src_directory = os.getenv("SRC_DIRECTORY")
    target_directory = os.getenv("TARGET_DIRECTORY")

    if not src_directory or not target_directory:
        print("Error: .env file is missing or SRC_DIRECTORY/TARGET_DIRECTORY are not set.")
        sys.exit(1)

    copy_directory(src_directory, target_directory)

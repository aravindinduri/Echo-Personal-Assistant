import os
import json
import time
import re

EXCLUDED_DIRS = {
    "node_modules", "__pycache__", ".git", ".vscode", ".idea", "venv", "env",
    "build", "dist", "tmp"
}

EXCLUDED_EXTENSIONS = {".code", ".log", ".tmp", ".swp", ".bak", ".lock", ".cache"}

def is_valid_file(file_name):
    """Checks if the file is not hidden, does not contain special characters, and is not in excluded extensions."""
    if file_name.startswith("."):  
        return False
    if re.search(r"[^a-zA-Z0-9_.-]", file_name): 
        return False
    if any(file_name.endswith(ext) for ext in EXCLUDED_EXTENSIONS):
        return False
    return True

def get_all_files_and_folders(root_directory):
    """Scans all files and folders in the given root directory and stores details in a dictionary."""
    file_data = {}

    for root, dirs, files in os.walk(root_directory):
        if any(part.startswith('.') for part in root.split(os.sep) if part):
            continue

        if any(excluded in root.split(os.sep) for excluded in EXCLUDED_DIRS):
            continue

        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in EXCLUDED_DIRS]

        valid_files = [f for f in files if is_valid_file(f)]
        
        if valid_files:
            file_data[root] = []
            for file_name in valid_files:
                file_path = os.path.join(root, file_name)
                try:
                    file_info = {
                        "name": file_name,
                        "size": os.path.getsize(file_path),  
                        "created": time.ctime(os.path.getctime(file_path)) 
                    }
                    file_data[root].append(file_info)
                except Exception as e:
                    print(f"⚠️ Error accessing {file_path}: {e}")

    return file_data

def save_to_json(data, output_file):
    """Saves the collected file data to a JSON file."""
    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)
    print(f"✅ File and folder data saved to {output_file}")

if __name__ == "__main__":
    home_directory = os.path.expanduser("~") 
    output_file = "filtered_files_data.json"

    print("🔍 Scanning files and folders... This may take a while.")
    file_data = get_all_files_and_folders(home_directory)
    
    save_to_json(file_data, output_file)
    print("🎉 Done! JSON file generated successfully.")

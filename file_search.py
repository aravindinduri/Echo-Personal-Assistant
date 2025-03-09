import os
import json

def load_json(filepath):
    """Load JSON data from a file."""
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading JSON: {e}")
        return None

def find_file_path(json_data, filename):
    """Search for a file in the JSON and return its full path."""
    for directory, files in json_data.items():
        for file in files:
            if file["name"] == filename:
                return os.path.join(directory, filename)
    return None  # File not found

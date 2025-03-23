# # import os
# # import subprocess
# # from speech import speak

# # def execute_command(command):
# #     """Execute a given terminal command in a new terminal window."""
# #     if not command:
# #         return
# #     speak(f"Executing command:")
# #     print(f"🚀 Running: ")
    
# #     home_dir = os.path.expanduser("~")
# #     subprocess.Popen([
# #         "gnome-terminal",
# #         "--working-directory", home_dir,
# #         "--", "bash", "-c", f"{command}; exec bash"
# #     ])


# import os
# import json
# import subprocess
# from speech import speak

# def load_json(filepath):
#     """Load JSON data from a file."""
#     try:
#         with open(filepath, 'r') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         print(f"❌ Error: JSON file '{filepath}' not found.")
#         return None
#     except json.JSONDecodeError:
#         print(f"❌ Error: JSON file '{filepath}' contains invalid JSON.")
#         return None

# def find_file_path(json_data, filename):
#     """Search for a file in the JSON and return its full path."""
#     for directory, files in json_data.items():
#         for file in files:
#             if file["name"] == filename:
#                 return os.path.join(directory, filename) 
#     return None 

# def execute_command(command, file_path):
#     """Execute a given terminal command in a new terminal window."""
#     if not command or not file_path:
#         print("❌ File not found or no command provided.")
#         return
    
#     file_directory = os.path.dirname(file_path)
#     file_name = os.path.basename(file_path)
    
#     full_command = command.replace("<filepath>", file_path)

#     speak(f"Executing command: {full_command}")
#     print(f"🚀 Running: {full_command}")

#     subprocess.Popen([
#         "gnome-terminal",
#         "--working-directory", file_directory,
#         "--", "bash", "-c", f"{full_command}; exec bash"
#     ])

import os
import json
import subprocess
from speech import speak

def load_json(filepath):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"❌ Error: JSON file '{filepath}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"❌ Error: JSON file '{filepath}' contains invalid JSON.")
        return None

def find_file_path(json_data, filename):
    for directory, files in json_data.items():
        for file in files:
            if file["name"].lower() == filename.lower():
                return os.path.join(directory, file["name"])  
    return None

def execute_command(command, file_path=None):
    if not command:
        print("❌ No command provided.")
        return

    if file_path:
        working_directory = os.path.dirname(file_path)
        full_command = f"{command} {file_path}"  
    else:
        working_directory = os.path.expanduser("~")
        full_command = command

    speak(f"Executing:")
    print(f"🚀 Running:")

    subprocess.run(full_command, shell=True, cwd=working_directory, check=True)

if __name__ == "__main__":
    json_data = load_json("files.json")
    if json_data:
        file_path = find_file_path(json_data, "example.txt")
        execute_command("cat", file_path)  
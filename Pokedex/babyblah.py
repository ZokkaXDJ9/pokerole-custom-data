import os
import json

# Set the target directory
directory = "."

# Loop through all files in the directory
for filename in os.listdir(directory):
    old_path = os.path.join(directory, filename)

    # --- 1. Rename the file if "Baby" is in the filename ---
    if "Baby" in filename:
        new_filename = filename.replace("Baby", "Low")
        new_path = os.path.join(directory, new_filename)
        os.rename(old_path, new_path)
        print(f'Renamed file: "{filename}" → "{new_filename}"')
        filename = new_filename  # Update filename for JSON processing
        old_path = new_path

    # --- 2. If it's a .json file, try to update "name" field ---
    if filename.endswith(".json"):
        try:
            with open(old_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            if "name" in data and "Baby" in data["name"]:
                old_name = data["name"]
                data["name"] = data["name"].replace("Baby", "Low")

                with open(old_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2)

                print(f'Updated "name" in "{filename}": "{old_name}" → "{data["name"]}"')
        except Exception as e:
            print(f'Could not process "{filename}": {e}')

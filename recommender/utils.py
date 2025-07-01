# recommender/utils.py

import json

def load_outfits(file_path):
    """
    Loads outfit data from the JSON file.
    """
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: outfits.json file not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return []

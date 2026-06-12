import json 
from pathlib import Path 


def save_contacts(file_path: str, saved_list: list) -> str: 
    with open(file_path, 'w') as file:
        json.dump(saved_list, file, indent=4)
    
    return 'contacts have been saved!'

def load_contacts(file_path: str):

    if Path(file_path).exists():
        with open(file_path, 'r') as file:
            loaded_data = json.load(file)
            return loaded_data
    else:
        print('the file doesnt exist yet. ')
        return []


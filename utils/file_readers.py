from typing import List

def read_ocean_file(file_path: str) -> List[List[str]]:
    """Reads file from file_path and returns List[List(str)] in format that is accepted by Ocean class"""
    with open(file_path, 'r') as f:
        read_file = f.read().splitlines()
    return [[*i] for i in read_file]  # unpack list of strings into list of lists of characters

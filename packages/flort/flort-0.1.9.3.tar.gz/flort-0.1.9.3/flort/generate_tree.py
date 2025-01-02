import os
import argparse
from pathlib import Path
import logging
from datetime import datetime



def is_binary_file(file_path):
    """Check if a file is binary."""
    try:
        with open(file_path, 'rb') as file:
            chunk = file.read(1024)
            if b'\x00' in chunk:
                return True
            text_characters = bytes(range(32, 127)) + b'\n\r\t\f\b'
            if bool(chunk.translate(None, text_characters)):
                return True
        return False
    except Exception as e:
        logging.error(f"Error determining if file is binary {file_path}: {e}")
        return True

def clean_content(file_path):
    """Cleans up the content of a file by removing unnecessary whitespace."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
        cleaned_lines = [line.strip() for line in lines if line.strip()]
        return '\n'.join(cleaned_lines)



def write_file(file_path, data, mode='a'):
    """Writes data to the specified file, or echoes to console if path is 'stdio'."""
    try:
        if file_path == "stdio":
            print(data)  # Output to console
        else:
            with open(file_path, mode) as file:
                file.write(data)
            logging.info(f"Output written to: {file_path}. Mode: {'create' if mode == 'w' else 'append'}.")
    except IOError as e:
        logging.error(f"Failed to write to {file_path}: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred while writing to {file_path}: {e}")


def generate_tree(path_list,output):
    """
    Generates a tree structure from a path list with depth information,
    listing directories first and then files.

    Args:
        path_list (list): A list of dictionaries containing paths and their depths.

    Returns:
        str: A formatted tree structure.
    """
    write_file(output,f"## Directory Tree\n")

    structure = []

    for item in path_list:
        path = item["path"]
        depth = item["depth"]
        indent = '|   ' * (depth - 1) + '|-- ' if depth > 0 else ''

        if item['type'] == 'dir':
            structure.append(f"{indent}{path.name}/")
        elif item['type'] == 'file':
            structure.append(f"{indent}{path.name}")
    

    write_file(output,'\n'.join(structure))
    

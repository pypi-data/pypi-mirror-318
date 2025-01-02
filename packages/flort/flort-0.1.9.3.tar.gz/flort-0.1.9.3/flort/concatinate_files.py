import os
from pathlib import Path
import logging
from datetime import datetime

from .generate_tree import write_file


def list_files(directories=None,  extensions=None, include_all=False, include_hidden=False,ignore_dirs=None):
        """Lists files in multiple directories."""
    #try:
        files_info = []
        num_files = 0
        if None==directories:
            return
        total_files=0
        for directory in directories:
            directory_path = Path(directory)
            if not directory_path.is_dir():
                logging.error(f"The path {directory} is not a valid directory.")
                continue

            logging.info(f"Processing directory: {directory_path}")

            for file_path in directory_path.rglob('*'):
                absolute_path = file_path.resolve()

                # Check if the file's directory or its parent directories should be ignored
#                if ignore_dirs and any(absolute_path.is_relative_to(ignore_dir) for ignore_dir in ignore_dirs):
                if ignore_dirs and any(str(absolute_path).startswith(str(ignore_dir)) for ignore_dir in ignore_dirs):

                    continue
                total_files+=1

                if file_path.is_file() and '.git' not in file_path.parts:
                    if not include_hidden and file_path.name.startswith('.'):
                        continue
                    #if is_binary_file(file_path):
                     #   print("binary .")
                     #   continue
                    if include_all or (extensions and file_path.suffix.lower() in extensions):
                        num_files += 1
                        file_info = [f"Path: {file_path}", f"File: {file_path.name}", "-------"]

                        try:
                            with open(file_path, 'r') as f:
                                file_info.append(f.read())
                        except Exception as e:
                            logging.error(f"Error reading file {file_path}: {e}")
                        
                        files_info.append('\n'.join(file_info))

        logging.info(f"Files processed: {num_files} of {total_files}")
        return '\n'.join(files_info)
    #except Exception as e:
    #    logging.error(f"Error processing directories: {e}")
    #    return ""



def concat_files(file_list,output):
    """
    Concatenates the contents of files from a provided file list,
    listing directories first and then files.

    Args:
        file_list (list): A list of dictionaries containing file paths and their depths.

    Returns:
        str: Concatenated contents of all directories and files.
    """
    dir_results = []
    file_results = []
    write_file(output,f"## File data\n")
    for item in file_list:
        file_path = item["path"]
        if file_path.is_file():  # Then process files
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    write_file(output,f"--- File: {item['relative_path']}\n{f.read()}\n")
                    
            except Exception as e:
                logging.error(f"Error reading file {file_path}: {e}")
                file_results.append(f"--- File: {file_path} ---\nError reading file.")

     
            


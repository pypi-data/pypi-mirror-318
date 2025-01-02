import os
import argparse
import logging
from datetime import datetime
from pathlib import Path

from .traverse import get_paths
from .generate_tree import generate_tree, write_file
from .concatinate_files import concat_files
from .python_outline import python_outline_files

def configure_logging(verbose):
    """Configures logging level based on verbosity flag."""
    level = logging.INFO if verbose else logging.WARNING
    logging.basicConfig(level=level, format='%(asctime)s - %(levelname)s - %(message)s')

def print_configuration(directories, extensions, include_all, include_hidden, ignore_dirs=None):
    """Prints the directories and extensions being processed."""
    logging.info(f"Processing: {', '.join(directories)}")
    logging.info(f"Types: {', '.join(extensions)}")
    logging.info(f"All files: {include_all}")
    logging.info(f"Hidden files: {include_hidden}")
    if ignore_dirs:
        for dir in ignore_dirs:
            logging.info(f"Omitting: {dir}")

def main():
    """Main function to parse arguments and execute operations."""
    output_file = f"{os.path.basename(os.getcwd())}.flort"
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    parser = argparse.ArgumentParser(
        description="flort: create a single file of all given extensions, recursively for all directories given. Ignores binary files.",
        prog='flort',
        add_help=False,
        prefix_chars='-',
        allow_abbrev=False
    )
    parser.add_argument('directories', metavar='DIRECTORY', default=".", type=str, nargs='*', help='Directories to list files from, defaults to the current working directory.')
    parser.add_argument('--ignore-dirs', type=str, help='Directories to ignore (comma-separated list).')
    parser.add_argument('-h', '--help', action='help', help='Show this help message and exit.')
    parser.add_argument('--output', type=str, default=output_file, help='Output file path. Defaults to the basename of the current directory if not specified. "stdio" will output to console.')
    parser.add_argument('--outline', action='store_true', help='Create an outline of the files instead of a source dump.')
    parser.add_argument('--no-dump', action='store_true', help='Do not dump the source files')
    parser.add_argument('--no-tree', action='store_true', help='Do not print the tree at the beginning.')
    parser.add_argument('--all', action='store_true', help='Include all files regardless of extensions.')
    parser.add_argument('--hidden', action='store_true', help='Include hidden files.')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose logging (INFO level).')
    args, unknown_args = parser.parse_known_args()

    # Configure logging
    configure_logging(args.verbose)

    # Handle ignore_dirs argument
    if args.ignore_dirs:
        ignore_dirs = [Path(ignore_dir).resolve() for ignore_dir in args.ignore_dirs.split(',')]
    else:
        ignore_dirs = []

    # Treat unknown args as extensions that start with '--'
    extensions = [f".{ext.lstrip('-')}" for ext in unknown_args if ext.startswith('--')]

    # Print configuration
    print_configuration(args.directories, extensions, args.all, args.hidden, ignore_dirs)

    if not extensions and not args.all:
        logging.error("No extensions provided and --all flag not set. No files to process.")
        return

    #file creation here
    write_file(args.output, f"## Florted: {current_datetime}\n",'w')

    path_list = get_paths(args.directories, extensions=extensions, include_all=args.all, include_hidden=args.hidden, ignore_dirs=ignore_dirs)
    if not args.no_tree:
        generate_tree(path_list, args.output)

    if args.outline==True:
        python_outline_files(path_list, args.output)
    
    if not args.no_dump:
        concat_files(path_list, args.output)

if __name__ == "__main__":
    main()

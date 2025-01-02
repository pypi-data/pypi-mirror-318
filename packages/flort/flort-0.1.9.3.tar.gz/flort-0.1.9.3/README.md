# Flort

**Flort** is a utility tool designed to flatten your source code directory into a single file, making it convenient for Large Language Model (LLM) usage. It supports various options to include/exclude files based on extensions, binary detection, and hidden file visibility.

## Features

- **Directory Flattening**: Combine files from multiple directories into a single output file.
- **File Filtering**: Filter files by extensions, hidden status, and binary detection.
- **Customizable Output**: Option to output to a file or standard output.
- **Directory Tree Generation**: Generate a visual directory tree structure.

## Installation

You can install flort from PyPI:

```bash
pip install flort
```

## Usage

The primary usage of flort is through the command line interface (CLI). Below are some common commands and options:

```bash
flort [DIRECTORY]... [--output OUTPUT] [--no-tree] [--all] [--hidden] [--ignore-dirs DIRS] [--EXTENSIONS]...
```

- **DIRECTORY**: One or more directories to process. Defaults to the current working directory if not specified.
- **--output**: Output file path. If not specified, the result is printed to the standard output.
- **--ignore-dirs**: Comma-separated list of directories to ignore.
- **--no-tree**: Do not print the directory tree at the beginning.
- **--all**: Include all files regardless of extensions.
- **--hidden**: Include hidden files.
- **--EXTENSIONS**: List of file extensions to include. Each extension should be prefixed with `--`.

### Examples

1. **Basic Usage**: Process files in `src/` and `lib/`, including only `.py` and `.txt` files.
    ```bash
    flort src lib --py --txt
    ```

2. **Include All Files**: Process all files in `src/` and `lib/`, ignoring file extensions.
    ```bash
    flort src lib --all
    ```

3. **Include Hidden Files**: Process files in `src/`, including hidden files and only `.md` files.
    ```bash
    flort src --hidden --md
    ```

4. **Output to File**: Process files in `src/` and output to `output.txt`.
    ```bash
    flort src --output output.txt --py --txt
    ```

5. **Ignore Specific Directories**: Process files in `src/`, ignoring `__pycache__` and `build` directories.
    ```bash
    flort src --ignore-dirs __pycache__,build --py --txt
    ```

## Development

To set up the development environment, clone the repository and install the dependencies:

```bash
git clone https://github.com/chris17453/flort.git
cd flort
pip install -r requirements.txt
```

Run the tests to ensure everything is working correctly:

```bash
make tests
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests on the GitHub repository.

## License

This project is licensed under the BSD License. See the [LICENSE](LICENSE) file for more details.

## Author

Chris Watkins - [chris@watkinslabs.com](mailto:chris@watkinslabs.com)

## Acknowledgments

Special thanks to the open-source community for their invaluable contributions and support.

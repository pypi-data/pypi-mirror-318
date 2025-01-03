import base64
import os

from pathlib import Path

SKIP_FILENAMES = [".DS_Store", ".gitkeep"]


def encode_file(path: str) -> str:
    value = open(path, "r").read()
    encoded_value = base64.b64encode(value.encode()).decode()
    return encoded_value


def decode_template(template: str) -> str:
    return base64.b64decode(template).decode()


def write_to_file(filename: str, value: str):
    output_file = Path(filename)
    output_file.parent.mkdir(exist_ok=True, parents=True)
    output_file.write_text(value)


def encode_templates_to_dict(directory: str) -> dict:
    templates = {}
    for root, subdirs, files in os.walk(directory):
        for filename in files:
            if filename in SKIP_FILENAMES:
                continue
            absolute_path = root + "/" + filename
            relative_path = absolute_path.replace(directory + "/", "")
            encoded_value = encode_file(absolute_path)
            templates[relative_path] = encoded_value
    return templates


def list_static_files(directory: str):
    static_files = []
    for root, subdirs, files in os.walk(directory):
        for filename in files:
            if filename in SKIP_FILENAMES:
                continue
            absolute_path = root + "/" + filename
            relative_path = absolute_path.replace(directory + "/", "")
            static_files.append(relative_path)
    return static_files

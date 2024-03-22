import shutil
import os
import re
import sys
import yaml
import subprocess
import glob
import concurrent.futures
from pathlib import Path


def create_package_id(library_name):
    pattern = r"[-\.\[\]]"
    package_id = re.sub(pattern, "", library_name)
    return package_id


def add_library_info_to_yaml(yaml_file_path, package_id, library_name):
    with open(yaml_file_path, "r") as file:
        content = yaml.safe_load(file) or {}

    content["PackageID"] = package_id
    content["Library"] = [
        {
            "Name": library_name,
            "URL": None,
            "Reference": [{"Author": None, "URL": None}],
        }
    ]

    with open(yaml_file_path, "w") as file:
        yaml.safe_dump(
            content, file, default_flow_style=False, sort_keys=False, indent=2
        )


def copy_and_rename_base_file(base_file, new_libraries_dir, library_name):
    package_id = create_package_id(library_name)
    new_file_name = f"{package_id}.yaml"
    new_file_path = os.path.join(new_libraries_dir, new_file_name)

    shutil.copy(base_file, new_file_path)
    add_library_info_to_yaml(new_file_path, package_id, library_name)

    print(f"Created {new_file_name}")


def format_yaml_with_prettier(yaml_file_path) -> None:
    try:
        subprocess.run(["prettier", "--write", yaml_file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error formatting file {yaml_file_path}: {e}")


def main(base_file, library_name):
    copy_and_rename_base_file(
        base_file, Path.cwd() / "data" / "libraries", library_name
    )
    print(f"Processed {library_name} library in")
    format_yaml_with_prettier(f"./data/libraries/{library_name}.yaml")
    print("All YAML files have been formatted.")


if __name__ == "__main__":
    base_file = Path.cwd() / "utils" / "libraries" / "base.yaml"
    library_name = sys.argv[1]
    main(base_file, library_name)

"""
==============================================================
 This script add new yaml features / modify the existing ones
==============================================================
"""


import yaml
import glob
import concurrent.futures
import os
import subprocess
from pathlib import Path


def load_new_features(new_features_file):
    """Load new features from the YAML file."""
    with open(new_features_file, "r") as file:
        new_features = yaml.safe_load(file)
    return new_features


def add_new_features_to_file(yaml_file_path, new_features):
    """Add new features to an existing YAML file and save it."""
    with open(yaml_file_path, "r") as file:
        content = yaml.safe_load(file) or {}

    # Merge new features with existing content
    # This overwrite existing keys if they match new feature keys
    updated_content = {**content, **new_features}

    with open(yaml_file_path, "w") as file:
        yaml.safe_dump(
            updated_content, file, default_flow_style=False, sort_keys=False, indent=2
        )


def format_yaml_with_prettier(yaml_file_path) -> None:
    try:
        subprocess.run(["prettier", "--write", yaml_file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error formatting file {yaml_file_path}: {e}")


def main(libraries_path, new_features_file):
    new_features = load_new_features(new_features_file)
    yaml_files = glob.glob(os.path.join(libraries_path, "*.yaml"))

    for yaml_file in yaml_files:
        add_new_features_to_file(yaml_file, new_features)
    print(f"Added new features to {len(yaml_files)} YAML files.")

    # List of YAML files to format
    yaml_files = glob.glob(os.path.join(libraries_path, "*.yaml"))
    # Use ThreadPoolExecutor to format files in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Schedule the formatting function for each YAML file
        futures = [
            executor.submit(format_yaml_with_prettier, yaml_file)
            for yaml_file in yaml_files
        ]
        # Wait for all futures to complete, if needed
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()  # You can use result or log it if needed
            except Exception as exc:
                print(f"Generated an exception: {exc}")
    print("All YAML files have been formatted.")


if __name__ == "__main__":
    libraries_path = Path.cwd().parent.parent / "data" / "libraries"
    new_features_file = Path.cwd() / "new_features.yaml"
    main(libraries_path, new_features_file)

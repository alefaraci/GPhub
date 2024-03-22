"""
========================================================================
 This script fetches the libraries version from the github repositories
========================================================================
"""

import os
import glob
import requests
import yaml
import subprocess
import concurrent.futures
from pathlib import Path
from rich.progress import track
from rich.console import Console

console = Console()
console._log_render.omit_repeated_times = False


def get_headers(params_dir) -> dict:
    try:
        with open(params_dir / "params.yaml", "r") as file:
            config = yaml.safe_load(file)
        github_token = config["github"]["token"]
        return {"Authorization": f"token {github_token}"}
    except Exception as e:
        raise ValueError(f"Error reading config file: {e}")


def format_yaml_with_prettier(yaml_file_path) -> None:
    try:
        subprocess.run(["prettier", "--write", yaml_file_path], check=True)
    except subprocess.CalledProcessError as e:
        console.log(f"Error formatting file {yaml_file_path}: {e}")


def fetch_latest_release_or_tag(repo_name, headers) -> tuple[str | None, str | None]:
    """Fetch the latest release or tag from a GitHub repository."""
    repo_url = f"https://api.github.com/repos/{repo_name}"
    releases_url = f"{repo_url}/releases/latest"
    tags_url = f"{repo_url}/tags"

    # Try to get the latest release
    response = requests.get(releases_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["tag_name"], data["html_url"]

    # If no release found, try to get the latest tag
    response = requests.get(tags_url, headers=headers)
    if response.status_code == 200:
        tags = response.json()
        if tags:
            return (
                tags[0]["name"],
                f"https://github.com/{repo_name}/releases/tag/{tags[0]['name']}",
            )
    return None, None


def main(libraries_dir, params_dir) -> None:

    headers = get_headers(params_dir)
    yaml_files = glob.glob(os.path.join(libraries_dir, "*.yaml"))

    for yaml_file in track(yaml_files, description="[blue bold]Fetching latest release"):
        # for yaml_file in yaml_files:
        with open(yaml_file, "r") as file:
            content = yaml.safe_load(file)

        # Assuming each file has a single repository
        if content.get("Repository"):
            repo_name = content["Repository"][0]["Name"]
            version_name, version_url = fetch_latest_release_or_tag(repo_name, headers)

            if version_name and version_url:
                # Update the version information in the YAML content
                content["Version"][0]["Name"] = version_name
                content["Version"][0]["URL"] = version_url

                # Write the updated content back to the file
                with open(yaml_file, "w") as file:
                    yaml.safe_dump(
                        content,
                        file,
                        default_flow_style=False,
                        sort_keys=False,
                        indent=2,
                    )
    console.log("[green]Version information updated for all YAML files.")

    # FORMATTING YAML FILES
    console.log("[dark_orange3]Formatting YAML files with Prettier...")
    yaml_files = glob.glob(os.path.join(libraries_dir, "*.yaml"))
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(format_yaml_with_prettier, yaml_file) for yaml_file in yaml_files]
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
            except Exception as exc:
                console.log(f"Generated an exception: {exc}")
    console.log("[green bold]All YAML files have been updated and formatted.")


if __name__ == "__main__":
    libraries_dir = Path.cwd().parent.parent / "data" / "libraries"
    params_dir = Path.cwd().parent.parent / "config" / "_default"
    main(libraries_dir, params_dir)

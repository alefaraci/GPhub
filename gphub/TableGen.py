"""
====================================================================
 This script generates a Table.html file from the localhost webpage
====================================================================
"""

import subprocess
import sys
import time
from pathlib import Path
import shutil
from bs4 import BeautifulSoup


def download_webpage(url) -> None:
    try:
        subprocess.run(["wget", "-p", "-k", "-R", "livereload.js*", url], check=True)
        print("wget command executed successfully.")
        time.sleep(0.5)
    except subprocess.CalledProcessError as e:
        print(f"Error executing wget: {e}")
        sys.exit(1)


def embed_css_into_html(html_path, css_path) -> None:
    # Read and indent CSS content
    css_content = css_path.read_text(encoding="utf-8")
    indented_css_content = "\n\t\t".join(css_content.splitlines())

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "lxml")

    # Replace the <link> tag with the new <style> tag
    link_tag = soup.find("link", {"href": css_path.name})
    if link_tag:
        new_style_tag = soup.new_tag("style")
        new_style_tag.string = indented_css_content
        link_tag.replace_with(new_style_tag)
        html_path.write_text(soup.prettify(), encoding="utf-8")


def main(localhost) -> None:
    base_path = Path.cwd() / localhost
    download_webpage("http://" + localhost)

    css_file_path = base_path / "style.css"
    html_file_path = base_path / "index.html"

    if css_file_path.exists() and html_file_path.exists():
        embed_css_into_html(html_file_path, css_file_path)

        # Rename and move the HTML file to the current directory
        (base_path / "index.html").rename(Path.cwd().parent / "Table.html")

        # Cleanup: delete the downloaded webpage directory
        shutil.rmtree(base_path)
        print("The Table.html has been successfully generated.")
    else:
        print("Required files not found.")
        sys.exit(1)


if __name__ == "__main__":
    localhost = "localhost:1313"
    main(localhost)

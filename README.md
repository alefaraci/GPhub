# Kriging-Table-HTML

A comprehensive guide to Kriging metamodeling toolboxes is available in the `Table.html` file.

## 🧑🏻‍💻 Developing the table

The table is built using `HTML`, `CSS`, and `JavaScript`, and it is served by a `Python server` using the `aiohttp` package and `websockets` for WebSocket support and `watchdog` for monitoring file changes.

### Setting `aiohttp` server

#### 🛠️ Installation

You need to install the `aiohttp`, `websockets`, `watchdog` Python packages.

```shell
pip install aiohttp websockets watchdog
```

#### 🛜 Running the server

You can start your server by executing:

```shell
python3 server.py
```

#### 🌐 Open the table on the browser

The table is served at `http://localhost:8000/main.html` ➡️ [Link](http://localhost:8000/main.html)

### 🆕 Adding a new package

To add a new package add a new dictionary entry to the `.packages/List.py` file having the following format:

```python
"GPvecchia": {
        "URL": "https://cran.r-project.org/package=GPvecchia",
        "Language": ["R"],
        "License": {
            "type": ["GPL2", "GPL3"],
            "URL": [
                "https://cran.r-project.org/web/licenses/GPL-2",
                "https://cran.r-project.org/web/licenses/GPL-3",
            ],
        },
        "Reference": {
            "Authors": "Katzfuss et al. (2017)",
            "URL": "https://arxiv.org/abs/1708.06302",
        },
        "Release": {
            "version": "v0.1.6",
            "URL": "https://cran.r-project.org/src/contrib/GPvecchia_0.1.6.tar.gz",
        },
        "Developers": [
            {
                "color": "blue",
                "name": "Southern Methodist University",
                "URL": "https://www.smu.edu/",
            },
        ],
        "Docs": [
            {
                "color": "default",
                "URL": "https://cran.r-project.org/web/packages/GPvecchia/GPvecchia.pdf",
                "link": "cran.r-project.org/web/packages/GPvecchia/GPvecchia.pdf",
            },
            {
                "color": "blue",
                "URL": "https://cran.r-project.org/web/packages/GPvecchia/vignettes/GPvecchia_vignette.html",
                "link": "cran.r-project.org/web/packages/GPvecchia/vignettes/GPvecchia_vignette",
            },
        ],
        "Support": [
            {
                "color": "default",
                "URL": "",
                "link": "",
            },
        ],
    },
"""
`
```

Then build the project running:

```shell
python3 build.py
```

### ⚠️ Fixing or adding new data to an existing package

Modify the `.packages/List.py` file at the `package_name` entry point.

Then rebuild the project running the script:

```shell
python3 build.py
```

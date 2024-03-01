# Kriging-Table-HTML

<p align="center">
    <img title="Kriging-Table-HTML" alt="Kriging-Table-HTML" src="https://res.cloudinary.com/dkytv4nwx/image/upload/v1709317441/Screenshot_2024-03-01_alle_19.12.28_tjgara.png">
</p>

---

<div align="center"><p>
A comprehensive guide to Kriging metamodeling toolboxes.
<br> Check the full table opening the <code>Table.html</code> file on the web browser of your choice.
</p></div>

<div align="center"><p>
    <a href="https://github.com/alefaraci/Kriging-Table-HTML/releases/tag/devs">
      <img title="version" alt="version" src="https://img.shields.io/badge/version-v0.0.dev-brightgreen">
    </a>
    <a href="https://www.python.org">
      <img title="language" alt="language" src="https://img.shields.io/badge/language-python-blue">
    </a>
    <a href="https://html.spec.whatwg.org">
      <img title="language" alt="language" src="https://img.shields.io/badge/language-html-orange">
    </a>
    <a href="https://www.w3.org/TR/CSS/">
      <img title="language" alt="language" src="https://img.shields.io/badge/language-CSS-green">
    </a>
    <a href="developer.mozilla.org/it/docs/Web/JavaScript">
      <img title="language" alt="language" src="https://img.shields.io/badge/language-JS-yellow">
    </a>
    <a href="https://github.com/alefaraci/Kriging-Table-HTML/blob/main/LICENSE">
      <img title="license" alt="license" src="https://img.shields.io/badge/license-MIT-brightgreen.svg">
    </a>
    <a href="https://github.com/alefaraci/Kriging-Table-HTML/issues">
      <img title="issues" alt="issues" src="https://img.shields.io/badge/issues-1-red">
    </a>
    </p>
</div>

---

## 🧑🏻‍💻 Developing the table

The table is built using `HTML`, `CSS`, and `JavaScript`, and it is served by a `Python server`.

### Setting server

#### 🛜 Running the server

You can start your server by executing:

```shell
cd devs
python3 -m http.server
```

#### 🌐 Open the table on the browser

The table is served at `http://localhost:8000/main.html` ➡️ [Link](http://localhost:8000/main.html)

---

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
cd devs
python3 build.py
```

or to auto-build on changes:

```python
find . -name '*.py' | entr -r python3 build.py
```

### ⚠️ Fixing or adding new data to an existing package

Modify the `.packages/List.py` file at the `package_name` entry point.

Then rebuild the project running the script:

```shell
cd devs
python3 build.py
```

or to auto-build on changes:

```python
find . -name '*.py' | entr -r python3 build.py
```

## Acknowledgements

This project has received funding from the [European Union’s Horizon 2020](https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-2020_en) research and innovation programme under the [Marie Sklodowska-Curie](https://marie-sklodowska-curie-actions.ec.europa.eu) grant agreement No. 955393.

## License

Licensed under the [MIT license](https://github.com/alefaraci/Kriging-Table-HTML/blob/main/LICENSE).

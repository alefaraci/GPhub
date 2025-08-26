<p align="center">
    <img title="GPhubLogo" alt="GPhub" src="https://res.cloudinary.com/dkytv4nwx/image/upload/v1710786255/GPhubLogo_nn1pyz.svg" width="300">
</p>

[![build](https://img.shields.io/badge/build-passing-brightgreen)](https://img.shields.io/badge/build-passing-brightgreen)
[![version](https://img.shields.io/badge/version-v0.0.dev-brightgreen)](https://github.com/alefaraci/Kriging-Table-HTML/releases/tag/devs)
[![language](https://img.shields.io/badge/language-GO-blue)](https://go.dev)
[![language](https://img.shields.io/badge/language-html-orange)](https://html.spec.whatwg.org)
[![language](https://img.shields.io/badge/language-CSS-green)](https://www.w3.org/TR/CSS/)
[![language](https://img.shields.io/badge/language-JS-yellow)](developer.mozilla.org/it/docs/Web/JavaScript)
[![license](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://github.com/alefaraci/Kriging-Table-HTML/blob/main/LICENSE)
[![issues](https://img.shields.io/badge/issues-1-red)](https://github.com/alefaraci/Kriging-Table-HTML/issues)

![GPhub](https://res.cloudinary.com/dkytv4nwx/image/upload/v1709317441/Screenshot_2024-03-01_alle_19.12.28_tjgara.png)

`GPhub` offers an interactive guide to Gaussian Process (GP) libraries. This project is built using [`Hugo Framework`](https://gohugo.io/), `GO Template`, `HTML`, `CSS`, and `JS`. The guide features a comprehensive dynamic table to provide an easy-to-use and intuitive reference for exploring the GP libraries available to the data science community. Whether new to GP or experienced in the field, the table simplifies the process of selecting the ideal GP tool that best suits one's needs.

The table is available by opening the `Table.html` file on a web browser of your choice.

## Citing GPhub

If you use GPhub in your research, please cite our [Journal paper]().

```
@article{Faraci2024,
  doi = {},
  url = {},
  year = {2024},
  publisher = {Springer},
  volume = {},
  number = {},
  pages = {},
  author = {Faraci, A., Beaurepaire, P., Gayton, N.},
  title = {GPhub: a comprehensive guide to Gaussian Process libraries, bridging theory with practice through features, limitations, and performance.},
  journal = {Structural and Multidisciplinary Optimization}
}
```

---

# Contributing

Contributions to GPhub are warmly welcomed. There are several ways you can contribute:

- **Improving the Guide**: Help us enhance the content and accuracy of our guide. This includes updating library information, adding new GP tools, and refining our descriptions to make them more helpful.
- **Technical Enhancements**: Contribute to the development of the site by improving its design, enhancing the functionality of the dynamic table, or fixing bugs.
- **Feedback and Suggestions**: Share your insights on how we can improve GPhub. We're always looking for feedback on the usability of the guide, new features that could be added, or any other suggestions you might have.

## How to Contribute

- **Fork the Repository**: Start by forking the GPhub repository on GitHub. This allows you to make changes without affecting the main project.
- **Create a Pull Request**: Once you've made your changes, submit a pull request. Be sure to provide a detailed description of your contributions and why they are beneficial to the project.
- **Code Review**: After submission, your pull request will be reviewed by the project maintainers. This process ensures that contributions align with the project's standards and goals.
- **Integration**: Once approved, your contributions will be merged into the project, becoming a part of the GPhub guide.

## Editing

### 👨‍💻 Adding a new library to the Table

To add a new library to the table create a new `PackageName.yaml` entry in the `./gphub/data` directory using this YAML template:

```YAML
PackageID: null
Library:
  - Name: null
    URL: null
    Reference:
      - Author: null
        URL: null
Language:
  - null
License:
  - Name: null
    URL: null
Repository:
  - Name: null
    URL: null
Version:
  - Name: null
    URL: null
Developer:
  - Tag: null
    Name: null
    URL: null
Docs:
  - Name: null
    URL: null
Support:
  - Name: null
    URL: null
Framework:
  - null
GPU: false
Trend:
  - Types:
    - Tag: null
      Name: null
    URL: null
LengthScale:
  - null
Correlation:
  - Types:
    - Tag: null
      Name: null
    URL: null
Mixture: false
MixtureModels:
  - Types:
    - Tag: null
      Name: null
    URL: null
```

### ⚠️ Fixing or adding data to an existing library

Modify the `./gphub/data/PackageName.yaml` file.

---

# Installation

## Install Hugo

Refer to [Hugo website](https://gohugo.io/installation/) for details on how to install Hugo.

#### Homebrew (macOS - Linux)

```sh
brew install hugo
```

#### MacPorts (macOS)

```MacPorts
sudo port install hugo
```

## Install Python dependencies

#### BeautifulSoup

```sh
pip install beautifulsoup4 lxml
```

## Deploy

### 🛜 Running on a local server

You can start your local server via hugo by executing:

```shell
cd gphub
hugo serve -D
```

The table is served at [`http://localhost:1313`](http://localhost:1313)

### ⤵️ Fetching version data from the GitHub repositories

You can fetch the version data of the libraries by running:

```shell
python FetchVersion.py
```

### 🛠️ Building a static HTML file

You can generate a static file `Table.html` by running:

```shell
python TableGen.py
```

---

# Acknowledgments

This project has received funding from the [European Union’s Horizon 2020](https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-2020_en) research and innovation programme under the [Marie Sklodowska-Curie](https://marie-sklodowska-curie-actions.ec.europa.eu) grant agreement No. 955393.

# License

Licensed under the [MIT license](https://github.com/alefaraci/Kriging-Table-HTML/blob/main/LICENSE).

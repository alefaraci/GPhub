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

`GPhub` offers an interactive guide to Gaussian Process (GP) libraries. This project is built using `GO Template`, `HTML`, `CSS`, and `JS`. The guide features a comprehensive dynamic table to provide an easy-to-use and intuitive reference for exploring the GP libraries available to the data science community. Whether new to GP or experienced in the field, the table simplifies the process of selecting the ideal GP tool that best suits one's needs.

# Usage: displaying the table

### 🛜 Running a local server

You can start your local server by executing:

```shell
make
```

The table is served at [`http://localhost:8080`](http://localhost:8080)

### 🛠️ Building a static HTML file

You can generate a static file `Table.html` by running:

```shell
sh TableHTMLgen.sh
```

The table is available by opening the `Table.html` file on the web browser of your choice.

# Contributing

The table is built using `GO Template`, `HTML`, `CSS`, and `JavaScript`.

### 👨‍💻 Adding a new library to the Table

To add a new library to the table create a new `PackageName.go` entry to the `./database` directory using this template:

```go
package database

import (
    "github.com/alefaraci/krightml/table/cells"
    "github.com/alefaraci/krightml/table/rows"
)

var TemplateVar = rows.Library{
    PackageID:    "TemplateID",
    PackageName:  "Template",
    PackageURL:   "",
    Reference:    "",
    ReferenceURL: "",
    Language:     []string{""},
    Licenses: []cells.NameURL{
        {
            Name: "",
            URL:  "",
        },
    },
    Version:    "",
    VersionURL: "",
    Developers: []cells.TagNameURL{
        {
            Tag:  "",
            Name: "",
            URL:  "",
        },
    },
    Docs: []cells.NameURL{
        {
            Name: "",
            URL:  "",
        },
    },
    Support: []cells.NameURL{
        {
            Name: "",
            URL:  "",
        },
    },
    Frameworks: []string{""},
    GPU:        false,
    Trends: []cells.TagGroup{
        {
            Group: []cells.TagName{
                {
                    Tag:  "",
                    Name: "",
                },
            },
            URL: "",
        },
    },
    LengthScale: []string{""},
    Correlation: []cells.TagGroup{
        {
            Group: []cells.TagName{
                {
                    Tag:  "",
                    Name: "",
                },
            },
            URL: "",
        },
    },
    Mixture: false,
    MixtureModels: []cells.TagGroup{
        {
            Group: []cells.TagName{
                {
                    Tag:  "",
                    Name: "",
                },
            },
            URL: "",
        },
    },
}
```

Then include the `TemplateVar` into the `TableRows` in the `main.go` file:

```go
package main

...

// serveTemplate handles the root path and renders the HTML page using Go templates
func serveTemplate(w http.ResponseWriter, r *http.Request) {

    ...
	// Insert data into the Table template
	TableRows := []rows.Library{
		database.AbstractGPsjl,
		database.Albatross,
		...
		database.TemplateVar,
	}

...
```

Finally rebuild the project by running:

```shell
make
```

or:

```shell
sh TableHTMLgen.sh
```

### ⚠️ Fixing or adding data to an existing library

Modify the `./database/PackageName.go` file.

Then rebuild the project by running:

```shell
make
```

or:

```shell
sh TableHTMLgen.sh
```

# Citing GPhub

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

# Acknowledgments

This project has received funding from the [European Union’s Horizon 2020](https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-2020_en) research and innovation programme under the [Marie Sklodowska-Curie](https://marie-sklodowska-curie-actions.ec.europa.eu) grant agreement No. 955393.

# License

Licensed under the [MIT license](https://github.com/alefaraci/Kriging-Table-HTML/blob/main/LICENSE).

package database

import (
    "github.com/alefaraci/krightml/table/cells"
    "github.com/alefaraci/krightml/table/rows"
)

var MUQ = rows.Library{
    PackageID: "MUQ",
    PackageName: "MUQ",
    PackageURL:   "https://mituq.bitbucket.io/source/_site/",   
    Reference:    "Parno et al. (2021)",
    ReferenceURL: "https://doi.org/10.21105/joss.03076",
    Language:     []string{"Cpp", "Python"},
    Licenses: []cells.NameURL{
        {
            Name: "BSD3",
            URL:  "https://bitbucket.org/mituq/muq2/src/master/LICENSE",
        },
    },
    Version:    "v0.4.3",
    VersionURL: "https://mituq.bitbucket.io/source/_site/latest/index.html",
    Developers: []cells.TagNameURL{
        {
            Tag:  "red",
            Name: "Massachusetts Institute of Technology",
            URL:  "https://www.mit.edu",
        },
		{
            Tag:  "green",
            Name: "Dartmouth College",
            URL:  "https://math.dartmouth.edu",
        },
		{
            Tag:  "purple",
            Name: "New York University",
            URL:  "https://www.nyu.edu",
        },
		{
            Tag:  "re",
            Name: "Heidelberg University",
            URL:  "https://www.uni-heidelberg.de",
        },
		{
            Tag:  "blue",
            Name: "National Science Foundation",
            URL:  "https://www.nsf.gov",
        },
		{
            Tag:  "green",
            Name: "US Department of Energy",
            URL:  "https://www.energy.gov",
        },
    },
    Docs: []cells.TagNameURL{
        {
            Tag:  "default",
            Name: "docs",
            URL:  "https://mituq.bitbucket.io/source/_site/latest/index.html",
        },
		{
            Tag:  "default",
            Name: "examples",
            URL:  "https://mituq.bitbucket.io/source/_site/examples.html",
        },
		{
            Tag:  "default",
            Name: "py examples",
            URL:  "https://bitbucket.org/mituq/muq2-examples/src/master/",
        },
    },
    Support: []cells.TagNameURL{
        {
            Tag:  "default",
            Name: "slack",
            URL:  "https://mituq.bitbucket.io/source/_site/index.html",
        },
    },
    Frameworks: []string{""},
    GPU:        false,
    Trends: []cells.TagGroup{
        {
        Group: []cells.TagName{
            {
                Tag:  "default",
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
                Tag:  "default",
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
                Tag:  "default",
                Name: "",
            },
        },
        URL: "",
    },
    },
}
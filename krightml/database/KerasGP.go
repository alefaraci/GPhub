package database

import (
    "github.com/alefaraci/krightml/table/cells"
    "github.com/alefaraci/krightml/table/rows"
)

var KerasGP = rows.Library{
    PackageID: "KerasGP",
    PackageName: "Keras-GP",
    PackageURL:   "https://github.com/alshedivat/keras-gp",   
    Reference:    "Al-Shedivat et al. (2017)",
    ReferenceURL: "https://jmlr.org/papers/v18/16-498.html",
    Language:     []string{"Python"},
    Licenses: []cells.NameURL{
        {
            Name: "MIT",
            URL:  "https://github.com/alshedivat/keras-gp/blob/master/LICENSE",
        },
    },
    Version:    "v0.3.2",
    VersionURL: "https://github.com/alshedivat/keras-gp/releases/tag/0.3.2",
    Developers: []cells.TagNameURL{
        {
            Tag:  "red",
            Name: "Carnegie Mellon University",
            URL:  "https://www.cmu.edu/",
        },
		{
            Tag:  "red",
            Name: "Cornell University",
            URL:  "https://www.cornell.edu/",
        },
		{
            Tag:  "default",
            Name: "Keras-GP contributors",
            URL:  "https://github.com/alshedivat/keras-gp/graphs/contributors",
        },
    },
    Docs: []cells.TagNameURL{
        {
            Tag:  "default",
            Name: "examples",
            URL:  "https://github.com/alshedivat/keras-gp/tree/master/examples",
        },
		{
            Tag:  "default",
            Name: "tutorials",
            URL:  "https://github.com/alshedivat/keras-gp/tree/master/tutorials",
        },
    },
    Support: []cells.TagNameURL{
        {
            Tag:  "default",
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
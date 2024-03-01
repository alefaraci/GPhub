package database

import (
    "github.com/alefaraci/krightml/table/cells"
    "github.com/alefaraci/krightml/table/rows"
)

var UQpy = rows.Library{
    PackageID: "UQpy",
    PackageName: "UQpy",
    PackageURL:   "https://sites.google.com/site/jhusurg/UQpy",   
    Reference:    "Olivier et al. (2020)",
    ReferenceURL: "https://www.sciencedirect.com/science/article/abs/pii/S1877750320305056",
    Language:     []string{"Python"},
    Licenses: []cells.NameURL{
        {
            Name: "MIT",
            URL:  "https://github.com/SURGroup/UQpy/blob/master/LICENSE",
        },
    },
    Version:    "v4.1.5",
    VersionURL: "https://github.com/SURGroup/UQpy/releases/tag/v4.1.5",
    Developers: []cells.TagNameURL{
        {
            Tag:  "blue",
            Name: "Johns Hopkins University",
            URL:  "https://sites.google.com/site/jhusurg/home?authuser=0",
        },
		{
            Tag:  "default",
            Name: "UQpy contributors",
            URL:  "https://github.com/SURGroup/UQpy/graphs/contributors",
        },
    },
    Docs: []cells.TagNameURL{
        {
            Tag:  "default",
            Name: "docs",
            URL:  "https://uqpyproject.readthedocs.io/en/latest/",
        },
    },
    Support: []cells.TagNameURL{
        {
            Tag:  "default",
            Name: "GitHub discussions",
            URL:  "https://github.com/SURGroup/UQpy/discussions",
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
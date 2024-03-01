package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var George = rows.Library{
    PackageID: "george",
    PackageName: "george",
    PackageURL:   "https://george.readthedocs.io/en/latest/",
    Reference:    "Ambikasaran et al. (2015)",
    ReferenceURL: "https://ieeexplore.ieee.org/document/7130620",
    Language:     []string{"Python"},
    Licenses: []cells.NameURL{
        {
            Name: "MIT",
            URL:  "https://github.com/dfm/george/blob/main/LICENSE",
        },
    },
    Version:    "v0.4.1",
    VersionURL: "https://github.com/dfm/george/releases/tag/v0.4.1",
    Developers: []cells.TagNameURL{
        {
            Tag:  "purple",
            Name: "New York University",
            URL:  "https://www.nyu.edu",
        },
		{
            Tag:  "blue",
            Name: "Simons Foundation",
            URL:  "https://www.simonsfoundation.org/",
        },
		{
            Tag:  "default",
            Name: "george contributors",
            URL:  "https://github.com/dfm/george/graphs/contributors",
        },
    },
    Docs: []cells.TagNameURL{
        {
            Tag:  "default",
            Name: "docs",
            URL:  "https://george.readthedocs.io/en/latest/user/",
        },
		{
            Tag:  "default",
            Name: "tutorials",
            URL:  "https://george.readthedocs.io/en/latest/tutorials/",
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

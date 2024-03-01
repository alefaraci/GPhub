package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var Libgp = rows.Library{
    PackageID: "libgp",
    PackageName: "libgp",
    PackageURL:   "https://github.com/mblum/libgp",
    Reference:    "",
    ReferenceURL: "",
    Language:     []string{"Cpp"},
    Licenses: []cells.NameURL{
        {
            Name: "BSD3",
            URL:  "https://github.com/mblum/libgp/blob/master/COPYING",
        },
    },
    Version:    "v0.1.4",
    VersionURL: "https://github.com/mblum/libgp/blob/master/README.md#release-notes",
    Developers: []cells.TagNameURL{
        {
            Tag:  "blue",
            Name: "",
            URL:  "",
        },
    },
    Docs: []cells.TagNameURL{
        {
            Tag:  "default",
            Name: "docs",
            URL:  "https://github.com/mblum/libgp/tree/master/doxygen",
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

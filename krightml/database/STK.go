package database

import (
    "github.com/alefaraci/krightml/table/cells"
    "github.com/alefaraci/krightml/table/rows"
)

var STK = rows.Library{
    PackageID: "STK",
    PackageName: "STK",
    PackageURL:   "https://github.com/stk-kriging/stk",   
    Reference:    "Bect et al. (2023)",
    ReferenceURL: "https://github.com/stk-kriging/stk/",
    Language:     []string{"Matlab", "Octave"},
    Licenses: []cells.NameURL{
        {
            Name: "GPL3",
            URL:  "https://github.com/stk-kriging/stk/blob/master/COPYING",
        },
    },
    Version:    "v2.8.1",
    VersionURL: "https://github.com/stk-kriging/stk/releases/tag/2.8.1",
    Developers: []cells.TagNameURL{
        {
            Tag:  "red",
            Name: "CentraleSupélec",
            URL:  "https://www.centralesupelec.fr",
        },
		{
            Tag:  "default",
            Name: "STK contributors",
            URL:  "https://github.com/stk-kriging/stk/graphs/contributors",
        },
    },
    Docs: []cells.TagNameURL{
        {
            Tag:  "default",
            Name: "docs",
            URL:  "https://stk-kriging.github.io/release/latest/doc/html/index.html",
        },
		{
            Tag:  "default",
            Name: "examples",
            URL:  "https://github.com/stk-kriging/stk/tree/master/examples",
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
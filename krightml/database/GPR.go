package database

import (
    "github.com/alefaraci/krightml/table/cells"
    "github.com/alefaraci/krightml/table/rows"
)

var GPR = rows.Library{
    PackageID: "GPR",
    PackageName: "GPR",
    PackageURL:   "https://github.com/ChristophJud/GPR",   
    Reference:    "n/a",
    ReferenceURL: "",
    Language:     []string{"Cpp"},
    Licenses: []cells.NameURL{
        {
            Name: "Apache2",
            URL:  "https://github.com/ChristophJud/GPR/blob/master/LICENSE",
        },
    },
    Version:    "n/a",
    VersionURL: "",
    Developers: []cells.TagNameURL{
        {
            Tag:  "teal",
            Name: "University of Basel",
            URL:  "https://www.unibas.ch",
        },
    },
    Docs: []cells.TagNameURL{
        {
            Tag:  "default",
            Name: "",
            URL:  "",
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
                Name: "White",
            },
				{
                Tag:  "default",
                Name: "RBF",
            },
				{
                Tag:  "default",
                Name: "Periodic",
            },
				{
                Tag:  "default",
                Name: "Rational Quadratic",
            },
        },
        URL: "",
    },
    },
    Mixture: true,
    MixtureModels: []cells.TagGroup{
        {
        Group: []cells.TagName{
            {
                Tag:  "default",
                Name: "Sum",
            },
				{
                Tag:  "default",
                Name: "Product",
            },
        },
        URL: "",
    },
    },
}
package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var Gokriging = rows.Library{
    PackageID: "gokriging",
    PackageName: "go-kriging",
    PackageURL:   "https://github.com/lvisei/go-kriging",
    Reference:    "n/a",
    ReferenceURL: "",
    Language:     []string{"GO"},
    Licenses: []cells.NameURL{
        {
            Name: "MIT",
            URL:  "https://github.com/lvisei/go-kriging/blob/main/LICENSE",
        },
    },
    Version:    "v0.0.1-alpha.15",
    VersionURL: "https://github.com/lvisei/go-kriging/releases/tag/v0.0.1-alpha.15",
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

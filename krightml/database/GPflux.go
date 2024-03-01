package database

import (
    "github.com/alefaraci/krightml/table/cells"
    "github.com/alefaraci/krightml/table/rows"
)

var GPflux = rows.Library{
    PackageID: "GPflux",
    PackageName: "GPflux",
    PackageURL:   "https://secondmind-labs.github.io/GPflux/#",   
    Reference:    "Dutordoir et al. (2021)",
    ReferenceURL: "https://arxiv.org/abs/2104.05674",
    Language:     []string{"Python"},
    Licenses: []cells.NameURL{
        {
            Name: "Apache2",
            URL:  "https://github.com/secondmind-labs/GPflux/blob/develop/LICENSE",
        },
    },
    Version:    "v0.4.3",
    VersionURL: "https://github.com/secondmind-labs/GPflux/releases/tag/v0.4.3",
    Developers: []cells.TagNameURL{
        {
            Tag:  "yellow",
            Name: "University of Cambridge",
            URL:  "https://www.cam.ac.uk",
        },
		{
            Tag:  "purple",
            Name: "Imperial College London",
            URL:  "https://www.imperial.ac.uk",
        },
		{
            Tag:  "purple",
            Name: "University College London",
            URL:  "https://www.ucl.ac.uk",
        },
		{
            Tag:  "purple",
            Name: "Secondimind labs",
            URL:  "https://www.secondmind.ai",
        },
		{
            Tag:  "default",
            Name: "GPflux contributors",
            URL:  "https://github.com/secondmind-labs/GPflux/graphs/contributors",
        },
    },
    Docs: []cells.TagNameURL{
        {
            Tag:  "default",
            Name: "docs",
            URL:  "https://secondmind-labs.github.io/GPflux/#getting-started",
        },
		{
            Tag:  "default",
            Name: "tutorials",
            URL:  "https://secondmind-labs.github.io/GPflux/tutorials.html",
        },
		{
            Tag:  "default",
            Name: "API",
            URL:  "https://secondmind-labs.github.io/GPflux/autoapi/gpflux/index.html",
        },
    },
    Support: []cells.TagNameURL{
        {
            Tag:  "default",
            Name: "slack",
            URL:  "https://secondmind-labs.slack.com/join/shared_invite/zt-ph07nuie-gMlkle__tjvXBay4FNSLkw#/shared-invite/email",
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
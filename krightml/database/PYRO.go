package database

import (
    "github.com/alefaraci/krightml/table/cells"
    "github.com/alefaraci/krightml/table/rows"
)

var PYRO = rows.Library{
    PackageID: "PYRO",
    PackageName: "PYRO",
    PackageURL:   "https://pyro.ai",   
    Reference:    "Bingham et al. (2019)",
    ReferenceURL: "http://jmlr.org/papers/v20/18-403.html",
    Language:     []string{"Python"},
    Licenses: []cells.NameURL{
        {
            Name: "Apache2",
            URL:  "https://github.com/pyro-ppl/pyro/blob/dev/LICENSE.md",
        },
    },
    Version:    "v1.9.0",
    VersionURL: "https://github.com/pyro-ppl/pyro/releases/tag/1.9.0",
    Developers: []cells.TagNameURL{
        {
            Tag:  "default",
            Name: "Uber AI",
            URL:  "https://eng.uber.com/uber-ai/",
        },
		{
            Tag:  "red",
            Name: "Stanford University",
            URL:  "https://www.stanford.edu",
        },
		{
            Tag:  "blue",
            Name: "Broad Institute",
            URL:  "https://www.broadinstitute.org",
        },
		{
            Tag:  "default",
            Name: "Linux Foundation",
            URL:  "https://www.linuxfoundation.org",
        },
		{
            Tag:  "default",
            Name: "PYRO contributors",
            URL:  "https://github.com/pyro-ppl/pyro/graphs/contributors",
        },
    },
    Docs: []cells.TagNameURL{
        {
            Tag:  "default",
            Name: "docs",
            URL:  "https://pyro.ai/examples/gp.html",
        },
		{
            Tag:  "default",
            Name: "examples",
            URL:  "https://pyro.ai/examples/",
        },
    },
    Support: []cells.TagNameURL{
        {
            Tag:  "default",
            Name: "forum",
            URL:  "http://forum.pyro.ai/",
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
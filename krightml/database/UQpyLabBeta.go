package database

import (
    "github.com/alefaraci/krightml/table/cells"
    "github.com/alefaraci/krightml/table/rows"
)

var UQpyLabBeta = rows.Library{
    PackageID: "UQpyLabBeta",
    PackageName: "UQ[py]Lab Beta",
    PackageURL:   "https://uqpylab.uq-cloud.io",   
    Reference:    "Lataniotis et al. (2021)",
    ReferenceURL: "https://www.eccomasproceedia.org/conferences/thematic-conferences/uncecomp-2021/8033",
    Language:     []string{"Python"},
    Licenses: []cells.NameURL{
        {
            Name: "BSD3",
            URL:  "https://www.uqlab.com/copy-of-release-notes",
        },
    },
    Version:    "v0.95",
    VersionURL: "https://uqpylab.uq-cloud.io/#beta-testing-application",
    Developers: []cells.TagNameURL{
        {
            Tag:  "default",
            Name: "RSUQ ETH Zürich",
            URL:  "https://sudret.ibk.ethz.ch/software/uqpylab.html",
        },
		{
            Tag:  "default",
            Name: "UQ[py]Lab contributors",
            URL:  "https://uqpylab.uq-cloud.io/contributors",
        },
    },
    Docs: []cells.TagNameURL{
        {
            Tag:  "default",
            Name: "docs",
            URL:  "https://uqpylab.uq-cloud.io/getting-started",
        },
		{
            Tag:  "default",
            Name: "user manuals",
            URL:  "https://uqpylab.uq-cloud.io/documentation",
        },
		{
            Tag:  "default",
            Name: "examples",
            URL:  "https://uqpylab.uq-cloud.io/examples",
        },
    },
    Support: []cells.TagNameURL{
        {
            Tag:  "default",
            Name: "contact form",
            URL:  "https://www.uqlab.com/contact",
        },
		{
            Tag:  "default",
            Name: "forum",
            URL:  "https://uqworld.org/c/uq-with-uqlab/7",
        },
    },
    Frameworks: []string{""},
    GPU:        false,
    Trends: []cells.TagGroup{
        {
        Group: []cells.TagName{
            {
                Tag:  "default",
                Name: "Zero",
            },
				{
                Tag:  "default",
                Name: "Constant",
            },
				{
                Tag:  "default",
                Name: "Linear",
            },
				{
                Tag:  "default",
                Name: "Quadratic",
            },
				{
                Tag:  "default",
                Name: "Polynomial",
            },
				{
                Tag:  "default",
                Name: "Custom",
            },
        },
        URL: "https://storage.googleapis.com/uqpylab-doc-html/UserManual_Kriging.html#[58,%22XYZ%22,71.434,547.221,null]",
    },
    },
    LengthScale: []string{"Isotropic", "Anisotropic"},
    Correlation: []cells.TagGroup{
        {
        Group: []cells.TagName{
            {
                Tag:  "default",
                Name: "Linear",
            },
				{
                Tag:  "default",
                Name: "Exponential",
            },
				{
                Tag:  "default",
                Name: "Gaussian",
            },
				{
                Tag:  "default",
                Name: "Matern32",
            },
				{
                Tag:  "default",
                Name: "Materm52",
            },
        },
        URL: "https://storage.googleapis.com/uqpylab-doc-html/UserManual_Kriging.html#[59,%22XYZ%22,85.039,437.866,null]",
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
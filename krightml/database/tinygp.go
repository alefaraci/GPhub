package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var Tinygp = rows.Library{
    PackageID: "tinygp",
    PackageName: "tinygp",
    PackageURL:   "https://tinygp.readthedocs.io/en/stable/",
    Reference:    "Foreman-Mackey et al. (2024)",
    ReferenceURL: "https://zenodo.org/records/10463641",
    Language:     []string{"Python"},
    Licenses: []cells.NameURL{
        {
            Name: "MIT",
            URL:  "https://github.com/dfm/tinygp/blob/main/LICENSE",
        },
    },
    Version:    "v0.3.0",
    VersionURL: "https://github.com/dfm/tinygp/releases/tag/v0.3.0",
    Developers: []cells.TagNameURL{
        {
            Tag:  "blue",
            Name: "Simons Foundation",
            URL:  "https://www.simonsfoundation.org",
        },
		{
            Tag:  "default",
            Name: "tinygp contributors",
            URL:  "https://github.com/dfm/tinygp/graphs/contributors",
        },
    },
    Docs: []cells.TagNameURL{
        {
            Tag:  "default",
            Name: "docs",
            URL:  "https://tinygp.readthedocs.io/en/stable/guide.html",
        },
		{
            Tag:  "default",
            Name: "tutorials",
            URL:  "https://tinygp.readthedocs.io/en/stable/tutorials.html",
        },
		{
            Tag:  "default",
            Name: "API",
            URL:  "https://tinygp.readthedocs.io/en/stable/api/index.html",
        },
    },
    Support: []cells.TagNameURL{
        {
            Tag:  "default",
            Name: "GitHub discussions",
            URL:  "https://github.com/dfm/tinygp/discussions",
        },
    },
    Frameworks: []string{"JAX"},
    GPU:        true,
    Trends: []cells.TagGroup{
        {
        Group: []cells.TagName{
            {
                Tag:  "default",
                Name: "Custom",
            },
        },
        URL: "https://tinygp.readthedocs.io/en/stable/api/summary/tinygp.means.Mean.html",
    },
    },
    LengthScale: []string{""},
    Correlation: []cells.TagGroup{
        {
        Group: []cells.TagName{
            {
                Tag:  "default",
                Name: "Conditioned",
            },
				{
                Tag:  "default",
                Name: "Custom",
            },
				{
                Tag:  "default",
                Name: "Constant",
            },
				{
                Tag:  "default",
                Name: "Polynomial",
            },
				{
                Tag:  "default",
                Name: "Exponetial",
            },
				{
                Tag:  "default",
                Name: "RBF",
            },
				{
                Tag:  "default",
                Name: "Matern32",
            },
				{
                Tag:  "default",
                Name: "Matern52",
            },
				{
                Tag:  "default",
                Name: "Cosine",
            },
				{
                Tag:  "default",
                Name: "Exponential Sine Squared",
            },
				{
                Tag:  "default",
                Name: "Rational Quadratic",
            },
        },
        URL: "https://tinygp.readthedocs.io/en/stable/api/kernels.html",
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
				{
                Tag:  "default",
                Name: "DotProduct",
            },
        },
        URL: "https://tinygp.readthedocs.io/en/stable/api/kernels.html",
    },
    },
}

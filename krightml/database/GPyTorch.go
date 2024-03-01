package database

import (
    "github.com/alefaraci/krightml/table/cells"
    "github.com/alefaraci/krightml/table/rows"
)

var GPyTorch = rows.Library{
    PackageID: "GPyTorch",
    PackageName: "GPyTorch",
    PackageURL:   "https://gpytorch.ai",   
    Reference:    "Gardner et al. (2018)",
    ReferenceURL: "https://arxiv.org/abs/1809.11165",
    Language:     []string{"Python"},
    Licenses: []cells.NameURL{
        {
            Name: "MIT",
            URL:  "https://github.com/cornellius-gp/gpytorch/blob/master/LICENSE",
        },
    },
    Version:    "v1.11",
    VersionURL: "https://github.com/cornellius-gp/gpytorch/releases/tag/v1.11",
    Developers: []cells.TagNameURL{
        {
            Tag:  "red",
            Name: "Cornell University",
            URL:  "https://www.cornell.edu/",
        },
		{
            Tag:  "blue",
            Name: "The University of British Columbia",
            URL:  "https://www.ubc.ca",
        },
		{
            Tag:  "blue",
            Name: "Meta",
            URL:  "https://research.facebook.com",
        },
		{
            Tag:  "purple",
            Name: "New York University",
            URL:  "https://www.nyu.edu/",
        },
		{
            Tag:  "brown",
            Name: "University of Pennsylvania",
            URL:  "https://www.upenn.edu/",
        },
		{
            Tag:  "default",
            Name: "GPyTorch contributors",
            URL:  "https://github.com/cornellius-gp/gpytorch/graphs/contributors",
        },
    },
    Docs: []cells.TagNameURL{
        {
            Tag:  "default",
            Name: "docs",
            URL:  "https://docs.gpytorch.ai/en/stable/",
        },
		{
            Tag:  "default",
            Name: "examples",
            URL:  "https://github.com/cornellius-gp/gpytorch/tree/master/examples/",
        },
    },
    Support: []cells.TagNameURL{
        {
            Tag:  "default",
            Name: "stackoverflow",
            URL:  "https://stackoverflow.com/questions/tagged/gpytorch",
        },
		{
            Tag:  "default",
            Name: "GitHub discussions",
            URL:  "https://github.com/cornellius-gp/gpytorch/discussions",
        },
    },
    Frameworks: []string{"PyTorch"},
    GPU:        true,
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
        },
        URL: "https://docs.gpytorch.ai/en/stable/kernels.html",
    },
    },
    LengthScale: []string{"Isotropic", "Anisotropic"},
    Correlation: []cells.TagGroup{
        {
        Group: []cells.TagName{
            {
                Tag:  "default",
                Name: "Cosine",
            },
				{
                Tag:  "default",
                Name: "Cylindrical",
            },
				{
                Tag:  "default",
                Name: "Linear",
            },
				{
                Tag:  "default",
                Name: "Matern",
            },
				{
                Tag:  "default",
                Name: "Periodic",
            },
				{
                Tag:  "default",
                Name: "Picewise Polynomial",
            },
				{
                Tag:  "default",
                Name: "Polynomial",
            },
				{
                Tag:  "default",
                Name: "RBF",
            },
				{
                Tag:  "default",
                Name: "RQK",
            },
				{
                Tag:  "default",
                Name: "Spectral Delta",
            },
				{
                Tag:  "default",
                Name: "Arc",
            },
				{
                Tag:  "default",
                Name: "Index",
            },
				{
                Tag:  "default",
                Name: "LCMK",
            },
				{
                Tag:  "default",
                Name: "Multitask",
            },
				{
                Tag:  "default",
                Name: "Grid",
            },
				{
                Tag:  "default",
                Name: "Grid Interpolation",
            },
				{
                Tag:  "default",
                Name: "Inducing Point",
            },
				{
                Tag:  "default",
                Name: "RFFK",
            },
        },
        URL: "https://docs.gpytorch.ai/en/stable/kernels.html",
    },
    },
    Mixture: true,
    MixtureModels: []cells.TagGroup{
        {
        Group: []cells.TagName{
            {
                Tag:  "default",
                Name: "Spectral Mixture",
            },
				{
                Tag:  "default",
                Name: "Additive",
            },
				{
                Tag:  "default",
                Name: "Product",
            },
				{
                Tag:  "default",
                Name: "Scale",
            },
        },
        URL: "https://docs.gpytorch.ai/en/stable/kernels.html",
    },
    },
}
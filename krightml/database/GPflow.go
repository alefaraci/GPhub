package database

import (
    "github.com/alefaraci/krightml/table/cells"
    "github.com/alefaraci/krightml/table/rows"
)

var GPflow = rows.Library{
    PackageID: "GPflow",
    PackageName: "GPflow",
    PackageURL:   "https://www.gpflow.org",   
    Reference:    "Matthews et al. (2017)",
    ReferenceURL: "https://jmlr.org/papers/v18/16-537.html",
    Language:     []string{"Python"},
    Licenses: []cells.NameURL{
        {
            Name: "Apache2",
            URL:  "https://github.com/GPflow/GPflow/blob/develop/LICENSE",
        },
    },
    Version:    "v2.9.1",
    VersionURL: "https://github.com/GPflow/GPflow/releases/tag/v2.9.1",
    Developers: []cells.TagNameURL{
        {
            Tag:  "yellow",
            Name: "University of Cambridge",
            URL:  "https://www.cam.ac.uk",
        },
		{
            Tag:  "blue",
            Name: "University of Oxford",
            URL:  "https://www.ox.ac.uk",
        },
		{
            Tag:  "blue",
            Name: "Kyoto University",
            URL:  "https://www.kyoto-u.ac.jp",
        },
		{
            Tag:  "default",
            Name: "University of Edinburgh",
            URL:  "https://www.ed.ac.uk",
        },
		{
            Tag:  "purple",
            Name: "The University of Manchster",
            URL:  "https://www.manchester.ac.uk",
        },
		{
            Tag:  "red",
            Name: "Lancaster University",
            URL:  "https://www.lancaster.ac.uk",
        },
		{
            Tag:  "default",
            Name: "GPflow contributors",
            URL:  "https://github.com/GPflow/GPflow/graphs/contributors",
        },
    },
    Docs: []cells.TagNameURL{
        {
            Tag:  "default",
            Name: "docs",
            URL:  "https://gpflow.github.io/GPflow/develop/getting_started.html",
        },
    },
    Support: []cells.TagNameURL{
        {
            Tag:  "default",
            Name: "slack",
            URL:  "https://gpflow.slack.com/join/shared_invite/enQtOTE5MDA0Nzg5NjA2LTYwZWI3MzhjYjNlZWI1MWExYzZjMGNhOWIwZWMzMGY0YjVkYzAyYjQ4NjgzNDUyZTgyNzcwYjAyY2QzMWRmYjE#/shared-invite/email",
        },
		{
            Tag:  "default",
            Name: "GitHub discussions",
            URL:  "https://github.com/GPflow/GPflow/discussions",
        },
		{
            Tag:  "default",
            Name: "stackoverflow",
            URL:  "https://stackoverflow.com/tags/gpflow",
        },
    },
    Frameworks: []string{"TensorFlow"},
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
                Name: "Polynomial",
            },
				{
                Tag:  "default",
                Name: "Additive",
            },
				{
                Tag:  "default",
                Name: "Constant",
            },
				{
                Tag:  "default",
                Name: "Function",
            },
				{
                Tag:  "default",
                Name: "Identity",
            },
				{
                Tag:  "default",
                Name: "Linear",
            },
				{
                Tag:  "default",
                Name: "Product",
            },
				{
                Tag:  "default",
                Name: "Switched Function",
            },
        },
        URL: "https://gpflow.github.io/GPflow/develop/api/gpflow/functions/index.html#gpflow.functions.MeanFunction",
    },
    },
    LengthScale: []string{"Isotropic", "Anisotropic"},
    Correlation: []cells.TagGroup{
        {
        Group: []cells.TagName{
            {
                Tag:  "default",
                Name: "ArcCosine",
            },
				{
                Tag:  "default",
                Name: "Bias",
            },
				{
                Tag:  "default",
                Name: "Change Points",
            },
				{
                Tag:  "default",
                Name: "Constant",
            },
				{
                Tag:  "default",
                Name: "Convolutional",
            },
				{
                Tag:  "default",
                Name: "Coregion",
            },
				{
                Tag:  "default",
                Name: "Cosine",
            },
				{
                Tag:  "default",
                Name: "Exponential",
            },
				{
                Tag:  "default",
                Name: "Independent Latent",
            },
				{
                Tag:  "default",
                Name: "Linear",
            },
				{
                Tag:  "default",
                Name: "Linear Coregionaliztion",
            },
				{
                Tag:  "default",
                Name: "Matern12",
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
                Name: "Multioutput",
            },
				{
                Tag:  "default",
                Name: "Periodic",
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
                Name: "Rational Quadratic",
            },
				{
                Tag:  "default",
                Name: "Separate Independent",
            },
				{
                Tag:  "default",
                Name: "Shared Independent",
            },
				{
                Tag:  "default",
                Name: "Squared Exponential",
            },
				{
                Tag:  "default",
                Name: "Static",
            },
				{
                Tag:  "default",
                Name: "Stationary",
            },
				{
                Tag:  "default",
                Name: "White",
            },
        },
        URL: "https://gpflow.github.io/GPflow/develop/api/gpflow/kernels/index.html",
    },
    },
    Mixture: true,
    MixtureModels: []cells.TagGroup{
        {
        Group: []cells.TagName{
            {
                Tag:  "default",
                Name: "Combination",
            },
				{
                Tag:  "default",
                Name: "Product",
            },
				{
                Tag:  "default",
                Name: "Sum",
            },
        },
        URL: "https://gpflow.github.io/GPflow/develop/api/gpflow/kernels/index.html",
    },
    },
}
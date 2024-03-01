package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var AbstractGPsjl = rows.Library{
	PackageID:    "AbstractGPsjl",
	PackageName:  "AbstractGPs.jl",
	PackageURL:   "https://juliagaussianprocesses.github.io/AbstractGPs.jl/dev/",
	Reference:    "n/a",
	ReferenceURL: "",
	Language:     []string{"Julia"},
	Licenses: []cells.NameURL{
		{
			Name: "MIT",
			URL:  "https://github.com/JuliaGaussianProcesses/AbstractGPs.jl/blob/master/LICENSE",
		},
	},
	Version:    "v0.5.19",
	VersionURL: "https://github.com/JuliaGaussianProcesses/AbstractGPs.jl/releases/tag/v0.5.19",
	Developers: []cells.TagNameURL{
		{
			Tag:  "default",
			Name: "AbstractGPs.jl contributors",
			URL:  "https://github.com/JuliaGaussianProcesses/AbstractGPs.jl/graphs/contributors",
		},
	},
	Docs: []cells.TagNameURL{
		{
			Tag:  "default",
			Name: "docs",
			URL:  "https://juliagaussianprocesses.github.io/AbstractGPs.jl/dev/api/",
		},
		{
			Tag:  "default",
			Name: "examples",
			URL:  "https://juliagaussianprocesses.github.io/AbstractGPs.jl/dev/concrete_features/",
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

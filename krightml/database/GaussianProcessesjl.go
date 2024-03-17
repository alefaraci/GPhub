package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var GaussianProcessesjl = rows.Library{
	PackageID:    "GaussianProcessesjl",
	PackageName:  "GaussianProcesses.jl",
	PackageURL:   "https://stor-i.github.io/GaussianProcesses.jl/latest/",
	Reference:    "Fairbrother et al. (2022)",
	ReferenceURL: "https://www.jstatsoft.org/article/view/v102i01",
	Language:     []string{"Julia"},
	Licenses: []cells.NameURL{
		{
			Name: "MIT",
			URL:  "https://github.com/STOR-i/GaussianProcesses.jl/blob/master/LICENSE.md",
		},
	},
	Version:    "v0.12.5",
	VersionURL: "https://github.com/STOR-i/GaussianProcesses.jl/releases/tag/v0.12.5",
	Developers: []cells.TagNameURL{
		{
			Tag:  "red",
			Name: "Lancaster University",
			URL:  "https://www.lancaster.ac.uk/stor-i/",
		},
		{
			Tag:  "red",
			Name: "EPFL",
			URL:  "https://www.epfl.ch/en/",
		},
		{
			Tag:  "default",
			Name: "GaussianProcesses.jl contributors",
			URL:  "https://github.com/STOR-i/GaussianProcesses.jl/graphs/contributors",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "docs",
			URL:  "https://stor-i.github.io/GaussianProcesses.jl/latest/",
		},
		{
			Name: "tutorials",
			URL:  "https://stor-i.github.io/GaussianProcesses.jl/latest/classification_example/",
		},
		{
			Name: "jupyter notebooks",
			URL:  "https://github.com/STOR-i/GaussianProcesses.jl/tree/master/notebooks",
		},
	},
	Support: []cells.NameURL{
		{
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
					Tag:  "",
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
					Tag:  "",
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
					Tag:  "",
					Name: "",
				},
			},
			URL: "",
		},
	},
}

package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var TemporalGPjl = rows.Library{
	PackageID:    "TemporalGPjl",
	PackageName:  "TemporalGP.jl",
	PackageURL:   "https://github.com/JuliaGaussianProcesses/TemporalGPs.jl",
	Reference:    "Tebbutt et al. (2021)",
	ReferenceURL: "https://proceedings.mlr.press/v161/tebbutt21a.html",
	Language:     []string{"Julia"},
	Licenses: []cells.NameURL{
		{
			Name: "MIT",
			URL:  "https://github.com/JuliaGaussianProcesses/TemporalGPs.jl/blob/master/LICENSE",
		},
	},
	Version:    "v0.6.8",
	VersionURL: "https://github.com/JuliaGaussianProcesses/TemporalGPs.jl/releases/tag/v0.6.8",
	Developers: []cells.TagNameURL{
		{
			Tag:  "yellow",
			Name: "University of Cambridge",
			URL:  "https://www.cam.ac.uk/",
		},
		{
			Tag:  "default",
			Name: "Aalto University",
			URL:  "https://www.aalto.fi/en",
		},
		{
			Tag:  "default",
			Name: "TemporalGPs.jl contributors",
			URL:  "https://github.com/JuliaGaussianProcesses/TemporalGPs.jl/graphs/contributors",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "examples",
			URL:  "https://github.com/JuliaGaussianProcesses/TemporalGPs.jl/tree/master/examples",
		},
		{
			Name: "talk",
			URL:  "https://www.youtube.com/watch?v=dysmEpX1QoE",
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

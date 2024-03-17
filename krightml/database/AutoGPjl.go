package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var AutoGPjl = rows.Library{
	PackageID:    "AutoGPjl",
	PackageName:  "AutoGP.jl",
	PackageURL:   "https://probsys.github.io/AutoGP.jl/stable/",
	Reference:    "Saad et al. (2023)",
	ReferenceURL: "https://arxiv.org/abs/2307.09607",
	Language:     []string{"Julia"},
	Licenses: []cells.NameURL{
		{
			Name: "Apache2",
			URL:  "https://github.com/probsys/AutoGP.jl/blob/main/LICENSE.txt",
		},
	},
	Version:    "",
	VersionURL: "",
	Developers: []cells.TagNameURL{
		{
			Tag:  "red",
			Name: "Carnegie Mellon University",
			URL:  "https://www.cmu.edu/",
		},
		{
			Tag:  "green",
			Name: "Google Research",
			URL:  "https://research.google/",
		},
		{
			Tag:  "purple",
			Name: "Massachusetts Institute of Technology",
			URL:  "https://www.mit.edu/",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "docs",
			URL:  "https://probsys.github.io/AutoGP.jl/stable/gp.html",
		},
		{
			Name: "tutorials",
			URL:  "https://probsys.github.io/AutoGP.jl/stable/tutorials/overview.html",
		},
		{
			Name: "API",
			URL:  "https://probsys.github.io/AutoGP.jl/stable/api.html",
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

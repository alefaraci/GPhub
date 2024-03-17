package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var GPJax = rows.Library{
	PackageID:    "GPJax",
	PackageName:  "GPJax",
	PackageURL:   "https://docs.jaxgaussianprocesses.com",
	Reference:    "Pinder et al. (2022)",
	ReferenceURL: "https://joss.theoj.org/papers/10.21105/joss.04455#",
	Language:     []string{"Python"},
	Licenses: []cells.NameURL{
		{
			Name: "Apache2",
			URL:  "https://github.com/JaxGaussianProcesses/GPJax/blob/main/LICENSE",
		},
	},
	Version:    "v0.8.0",
	VersionURL: "https://github.com/JaxGaussianProcesses/GPJax/releases/tag/v0.8.0",
	Developers: []cells.TagNameURL{
		{
			Tag:  "red",
			Name: "Lancaster University",
			URL:  "https://www.lancaster.ac.uk",
		},
		{
			Tag:  "default",
			Name: "GPJax contributors",
			URL:  "https://github.com/JaxGaussianProcesses/GPJax/graphs/contributors",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "docs",
			URL:  "https://docs.jaxgaussianprocesses.com",
		},
		{
			Name: "tutorials",
			URL:  "https://docs.jaxgaussianprocesses.com/examples/regression/",
		},
	},
	Support: []cells.NameURL{
		{
			Name: "GitHub discussions",
			URL:  "https://github.com/orgs/JaxGaussianProcesses/discussions",
		},
	},
	Frameworks: []string{"JAX"},
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

package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var Celerite2 = rows.Library{
	PackageID:    "celerite2",
	PackageName:  "celerite2",
	PackageURL:   "https://celerite2.readthedocs.io/en/latest/tutorials/first/",
	Reference:    "Gordon et al. (2020)",
	ReferenceURL: "https://iopscience.iop.org/article/10.3847/1538-3881/abbc16",
	Language:     []string{"Cpp", "Python"},
	Licenses: []cells.NameURL{
		{
			Name: "MIT",
			URL:  "https://github.com/exoplanet-dev/celerite2/blob/main/LICENSE",
		},
	},
	Version:    "v0.3.0",
	VersionURL: "https://github.com/exoplanet-dev/celerite2/releases/tag/v0.3.0",
	Developers: []cells.TagNameURL{
		{
			Tag:  "purple",
			Name: "University of Washington",
			URL:  "https://www.washington.edu",
		},
		{
			Tag:  "uiBlue",
			Name: "Flatiron Institute",
			URL:  "https://www.simonsfoundation.org/flatiron/",
		},
		{
			Tag:  "default",
			Name: "celertie2 contributors",
			URL:  "https://github.com/exoplanet-dev/celerite2/graphs/contributors",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "docs",
			URL:  "https://celerite2.readthedocs.io/en/latest/",
		},
		{
			Name: "tutorials",
			URL:  "https://celerite2.readthedocs.io/en/latest/tutorials/first/",
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

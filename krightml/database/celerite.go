package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var Celerite = rows.Library{
	PackageID:    "celerite",
	PackageName:  "celerite",
	PackageURL:   "https://celerite.readthedocs.io/en/stable/",
	Reference:    "Foreman-Mackey et al. (2017)",
	ReferenceURL: "https://iopscience.iop.org/article/10.3847/1538-3881/aa9332",
	Language:     []string{"Cpp", "Julia", "Python"},
	Licenses: []cells.NameURL{
		{
			Name: "MIT",
			URL:  "https://github.com/dfm/celerite/blob/main/LICENSE",
		},
	},
	Version:    "v0.4.2",
	VersionURL: "https://github.com/dfm/celerite/releases/tag/v0.4.2",
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
			Tag:  "teal",
			Name: "Indian Institute of Science",
			URL:  "https://www.iisc.ac.in",
		},
		{
			Tag:  "blue",
			Name: "Columbia University",
			URL:  "https://www.columbia.edu",
		},
		{
			Tag:  "default",
			Name: "celertie contributors",
			URL:  "https://github.com/dfm/celerite/graphs/contributors",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "docs",
			URL:  "https://celerite.readthedocs.io/en/stable/",
		},
		{
			Name: "API",
			URL:  "https://celerite.readthedocs.io/en/stable/cpp/api/",
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

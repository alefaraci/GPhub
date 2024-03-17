package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var PyGPs = rows.Library{
	PackageID:    "pyGPs",
	PackageName:  "pyGPs",
	PackageURL:   "https://github.com/marionmari/pyGPs",
	Reference:    "Neumann et al. (2015)",
	ReferenceURL: "https://jmlr.org/papers/v16/neumann15a.html",
	Language:     []string{"Python"},
	Licenses: []cells.NameURL{
		{
			Name: "FreeBSD",
			URL:  "https://github.com/marionmari/pyGPs/blob/master/COPYRIGHT.txt",
		},
	},
	Version:    "v1.3.5",
	VersionURL: "https://github.com/marionmari/pyGPs/releases/tag/v1.3.5",
	Developers: []cells.TagNameURL{
		{
			Tag:  "red",
			Name: "Washington University",
			URL:  "https://wustl.edu",
		},
		{
			Tag:  "teal",
			Name: "Fraunhofer IAIS",
			URL:  "https://www.iais.fraunhofer.de/en.html",
		},
		{
			Tag:  "green",
			Name: "TU Dortmund",
			URL:  "https://www.tu-dortmund.de/en/",
		},
		{
			Tag:  "yellow",
			Name: "Sproutling",
			URL:  "https://www.crunchbase.com/organization/sproutling",
		},
		{
			Tag:  "default",
			Name: "pyGPs contributors",
			URL:  "https://github.com/marionmari/pyGPs/graphs/contributors",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "docs",
			URL:  "https://www.cse.wustl.edu/~m.neumann/pyGPs_doc/",
		},
		{
			Name: "examples",
			URL:  "https://www.cse.wustl.edu/~m.neumann/pyGPs_doc/Examples.html",
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

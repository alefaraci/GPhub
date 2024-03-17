package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var GPy = rows.Library{
	PackageID:    "GPy",
	PackageName:  "GPy",
	PackageURL:   "https://sheffieldml.github.io/GPy/",
	Reference:    "GPy (2012)",
	ReferenceURL: "http://github.com/SheffieldML/GPy",
	Language:     []string{"Python"},
	Licenses: []cells.NameURL{
		{
			Name: "BSD3",
			URL:  "https://github.com/SheffieldML/GPy/blob/devel/LICENSE.txt",
		},
	},
	Version:    "v1.13.1",
	VersionURL: "https://github.com/SheffieldML/GPy/releases/tag/v1.13.1",
	Developers: []cells.TagNameURL{
		{
			Tag:  "purple",
			Name: "University of Sheffield",
			URL:  "https://www.sheffield.ac.uk/dcs/research/groups/machine-learning",
		},
		{
			Tag:  "default",
			Name: "GPy contributors",
			URL:  "https://github.com/SheffieldML/GPy/graphs/contributors",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "docs",
			URL:  "https://gpy.readthedocs.io/en/deploy/",
		},
		{
			Name: "jupyter notebooks",
			URL:  "https://nbviewer.org/github/SheffieldML/notebook/blob/master/GPy/index.ipynb",
		},
	},
	Support: []cells.NameURL{
		{
			Name: "mailing-list",
			URL:  "https://lists.shef.ac.uk/sympa/subscribe/gpy-users",
		},
		{
			Name: "GitHub discussions",
			URL:  "https://github.com/SheffieldML/GPy/discussions",
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

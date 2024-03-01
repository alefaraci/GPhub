package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var AutoGP = rows.Library{
	PackageID:    "AutoGP",
	PackageName:  "AutoGP",
	PackageURL:   "https://arxiv.org/abs/1610.05392",
	Reference:    "Krauth et al. (2017)",
	ReferenceURL: "https://arxiv.org/abs/1610.05392",
	Language:     []string{"Python"},
	Licenses: []cells.NameURL{
		{
			Name: "Apache2",
			URL:  "https://github.com/ebonilla/AutoGP/blob/master/LICENSE",
		},
	},
	Version:    "n/a",
	VersionURL: "",
	Developers: []cells.TagNameURL{
		{
			Tag:  "yellow",
			Name: "The University of New South Wales",
			URL:  "https://www.unsw.edu.au/",
		},
		{
			Tag:  "blue",
			Name: "EURECOM",
			URL:  "https://www.eurecom.fr/",
		},
		{
			Tag:  "default",
			Name: "AutoGP contributors",
			URL:  "https://github.com/ebonilla/AutoGP/graphs/contributors",
		},
	},
	Docs: []cells.TagNameURL{
		{
			Tag:  "default",
			Name: "",
			URL:  "",
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

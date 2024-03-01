package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var Albatross = rows.Library{
	PackageID:    "albatross",
	PackageName:  "albatross",
	PackageURL:   "https://swiftnav-albatross.readthedocs.io/en/latest/",
	Reference:    "n/a",
	ReferenceURL: "",
	Language:     []string{"Cpp"},
	Licenses: []cells.NameURL{
		{
			Name: "MIT",
			URL:  "https://github.com/swift-nav/albatross/blob/master/LICENSE",
		},
	},
	Version:    "n/a",
	VersionURL: "",
	Developers: []cells.TagNameURL{
		{
			Tag:  "orange",
			Name: "Swift Navigation",
			URL:  "https://www.swiftnav.com",
		},
		{
			Tag:  "default",
			Name: "albatross contributors",
			URL:  "https://github.com/swift-nav/albatross/graphs/contributors",
		},
	},
	Docs: []cells.TagNameURL{
		{
			Tag:  "default",
			Name: "docs",
			URL:  "https://swiftnav-albatross.readthedocs.io/en/latest/",
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

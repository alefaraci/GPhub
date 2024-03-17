package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var GPR = rows.Library{
	PackageID:    "GPR",
	PackageName:  "GPR",
	PackageURL:   "https://github.com/ChristophJud/GPR",
	Reference:    "",
	ReferenceURL: "",
	Language:     []string{"Cpp"},
	Licenses: []cells.NameURL{
		{
			Name: "Apache2",
			URL:  "https://github.com/ChristophJud/GPR/blob/master/LICENSE",
		},
	},
	Version:    "",
	VersionURL: "",
	Developers: []cells.TagNameURL{
		{
			Tag:  "teal",
			Name: "University of Basel",
			URL:  "https://www.unibas.ch",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "",
			URL:  "",
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
					Tag:  "default",
					Name: "White",
				},
				{
					Tag:  "default",
					Name: "RBF",
				},
				{
					Tag:  "default",
					Name: "Periodic",
				},
				{
					Tag:  "default",
					Name: "Rational Quadratic",
				},
			},
			URL: "",
		},
	},
	Mixture: true,
	MixtureModels: []cells.TagGroup{
		{
			Group: []cells.TagName{
				{
					Tag:  "default",
					Name: "Sum",
				},
				{
					Tag:  "default",
					Name: "Product",
				},
			},
			URL: "",
		},
	},
}

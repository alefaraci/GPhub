package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var Gaussianproc = rows.Library{
	PackageID:    "gaussianproc",
	PackageName:  "gaussianproc",
	PackageURL:   "",
	Reference:    " et al. ()",
	ReferenceURL: "",
	Language:     []string{"GO"},
	Licenses: []cells.NameURL{
		{
			Name: "NA",
			URL:  "",
		},
	},
	Version:    "v0",
	VersionURL: "https://pkg.go.dev/github.com/RobinRCM/sklearn/gaussian_process?tab=versions",
	Developers: []cells.TagNameURL{
		{
			Tag:  "blue",
			Name: "",
			URL:  "",
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

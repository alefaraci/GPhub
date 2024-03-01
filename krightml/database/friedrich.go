package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var Friedrich = rows.Library{
	PackageID:    "friedrich",
	PackageName:  "friedrich",
	PackageURL:   "https://github.com/nestordemeure/friedrich?tab=readme-ov-file",
	Reference:    "n/a",
	ReferenceURL: "",
	Language:     []string{"Rust"},
	Licenses: []cells.NameURL{
		{
			Name: "Apache2",
			URL:  "https://github.com/nestordemeure/friedrich/blob/master/LICENSE",
		},
	},
	Version:    "n/a",
	VersionURL: "",
	Developers: []cells.TagNameURL{
		{
			Tag:  "default",
			Name: "friedrich contributors",
			URL:  "https://github.com/nestordemeure/friedrich/graphs/contributors",
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

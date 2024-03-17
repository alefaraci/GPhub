package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var Friedrich = rows.Library{
	PackageID:    "friedrich",
	PackageName:  "friedrich",
	PackageURL:   "https://github.com/nestordemeure/friedrich?tab=readme-ov-file",
	Reference:    "",
	ReferenceURL: "",
	Language:     []string{"Rust"},
	Licenses: []cells.NameURL{
		{
			Name: "Apache2",
			URL:  "https://github.com/nestordemeure/friedrich/blob/master/LICENSE",
		},
	},
	Version:    "",
	VersionURL: "",
	Developers: []cells.TagNameURL{
		{
			Tag:  "default",
			Name: "friedrich contributors",
			URL:  "https://github.com/nestordemeure/friedrich/graphs/contributors",
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

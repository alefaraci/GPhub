package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var Fbm = rows.Library{
	PackageID:    "fbm",
	PackageName:  "fbm",
	PackageURL:   "https://glizen.com/radfordneal/fbm.software.html",
	Reference:    "Neal (1996)",
	ReferenceURL: "https://link.springer.com/book/10.1007/978-1-4612-0745-0",
	Language:     []string{"C"},
	Licenses: []cells.NameURL{
		{
			Name: "BSL1",
			URL:  "https://gitlab.com/radfordneal/fbm/-/blob/master/README?ref_type=heads",
		},
	},
	Version:    "v2022-04-21",
	VersionURL: "https://glizen.com/radfordneal/fbm.2022-04-21.doc/Release.2022-04-21.html",
	Developers: []cells.TagNameURL{
		{
			Tag:  "blue",
			Name: "University of Toronto",
			URL:  "https://www.statistics.utoronto.ca",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "docs",
			URL:  "https://glizen.com/radfordneal/fbm.2022-04-21.doc/index.html",
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
					Tag:  "default",
					Name: "Zero",
				},
			},
			URL: "https://glizen.com/radfordneal/fbm.2022-04-21.doc/gp.html ",
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

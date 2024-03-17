package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var DACE = rows.Library{
	PackageID:    "DACE",
	PackageName:  "DACE",
	PackageURL:   "https://www.omicron.dk/dace.html",
	Reference:    "Nielsen et al. (2002)",
	ReferenceURL: "https://www.semanticscholar.org/paper/DACE-A-Matlab-Kriging-Toolbox-Nielsen-Lophaven/d11a9e296ccd522809cb7550740e89f2c7ee65af#paper-topics",
	Language:     []string{"Matlab"},
	Licenses: []cells.NameURL{
		{
			Name: "",
			URL:  "",
		},
	},
	Version:    "v2.5",
	VersionURL: "https://www.omicron.dk/dace/changelog.txt",
	Developers: []cells.TagNameURL{
		{
			Tag:  "red",
			Name: "Techincal University of Denmark (DTU)",
			URL:  "https://www.dtu.dk",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "docs",
			URL:  "https://www.omicron.dk/dace/dace.pdf",
		},
		{
			Name: "user manuals",
			URL:  "https://www.omicron.dk/dace/dace-aspects.pdf",
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

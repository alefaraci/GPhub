package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var Deepgp = rows.Library{
	PackageID:    "deepgp",
	PackageName:  "deepgp",
	PackageURL:   "https://cran.r-project.org/package=deepgp",
	Reference:    "Sauer et al. (2023)",
	ReferenceURL: "https://vtechworks.lib.vt.edu/items/9f21c4d1-2dfc-4750-9501-7e8e622b2427",
	Language:     []string{"R"},
	Licenses: []cells.NameURL{
		{
			Name: "LGPL",
			URL:  "https://cran.r-project.org/web/licenses/LGPL-3",
		},
	},
	Version:    "v1.1.1",
	VersionURL: "https://cran.r-project.org/src/contrib/deepgp_1.1.1.tar.gz",
	Developers: []cells.TagNameURL{
		{
			Tag:  "red",
			Name: "Virginia Polytechnic Institute and State University",
			URL:  "https://www.vt.edu/",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "docs",
			URL:  "https://cran.r-project.org/web/packages/deepgp/deepgp.pdf",
		},
		{
			Name: "tutorials",
			URL:  "https://cran.r-project.org/web/packages/deepgp/vignettes/deepgp.html",
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

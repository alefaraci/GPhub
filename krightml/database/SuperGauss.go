package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var SuperGauss = rows.Library{
	PackageID:    "SuperGauss",
	PackageName:  "SuperGauss",
	PackageURL:   "https://cran.r-project.org/package=SuperGauss",
	Reference:    "Ling et al. (2020)",
	ReferenceURL: "https://github.com/mlysy/SuperGauss/blob/master/doc/SuperGauss_preprint.pdf",
	Language:     []string{"R"},
	Licenses: []cells.NameURL{
		{
			Name: "GPL3",
			URL:  "https://cran.r-project.org/web/licenses/GPL-3",
		},
	},
	Version:    "v2.0.3",
	VersionURL: "https://cran.r-project.org/src/contrib/SuperGauss_2.0.3.tar.gz",
	Developers: []cells.TagNameURL{
		{
			Tag:  "yellow",
			Name: "University of Waterloo",
			URL:  "https://uwaterloo.ca",
		},
		{
			Tag:  "default",
			Name: "SuperGauss contributors",
			URL:  "https://github.com/mlysy/SuperGauss/graphs/contributors",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "docs",
			URL:  "https://cran.r-project.org/web/packages/SuperGauss/SuperGauss.pdf",
		},
		{
			Name: "tutorials",
			URL:  "https://cran.r-project.org/web/packages/SuperGauss/vignettes/SuperGauss-quicktut.html",
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

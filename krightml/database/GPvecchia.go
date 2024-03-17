package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var GPvecchia = rows.Library{
	PackageID:    "GPvecchia",
	PackageName:  "GPvecchia",
	PackageURL:   "https://cran.r-project.org/package=GPvecchia",
	Reference:    "Katzfuss et al. (2017)",
	ReferenceURL: "https://arxiv.org/abs/1708.06302",
	Language:     []string{"R"},
	Licenses: []cells.NameURL{
		{
			Name: "GPL2",
			URL:  "https://cran.r-project.org/web/licenses/GPL-2",
		},
		{
			Name: "GPL3",
			URL:  "https://cran.r-project.org/web/licenses/GPL-3",
		},
	},
	Version:    "v0.1.6",
	VersionURL: "https://cran.r-project.org/src/contrib/GPvecchia_0.1.6.tar.gz",
	Developers: []cells.TagNameURL{
		{
			Tag:  "brown",
			Name: "Texas A&M University",
			URL:  "https://www.tamu.edu",
		},
		{
			Tag:  "red",
			Name: "Cornell University",
			URL:  "https://www.cornell.edu",
		},
		{
			Tag:  "default",
			Name: "GPvecchia contributors",
			URL:  "https://github.com/katzfuss-group/GPvecchia/graphs/contributors",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "docs",
			URL:  "https://cran.r-project.org/web/packages/GPvecchia/GPvecchia.pdf",
		},
		{
			Name: "tutorials",
			URL:  "https://cran.r-project.org/web/packages/GPvecchia/vignettes/GPvecchia_vignette.html",
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

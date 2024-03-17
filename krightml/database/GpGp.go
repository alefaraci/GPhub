package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var GpGp = rows.Library{
	PackageID:    "GpGp",
	PackageName:  "GpGp",
	PackageURL:   "https://cran.r-project.org/package=GpGp",
	Reference:    "Guinness et al. (2018)",
	ReferenceURL: "https://www.tandfonline.com/doi/full/10.1080/00401706.2018.1437476",
	Language:     []string{"R"},
	Licenses: []cells.NameURL{
		{
			Name: "MIT",
			URL:  "https://cran.r-project.org/web/licenses/MIT",
		},
	},
	Version:    "v0.5.0",
	VersionURL: "https://cran.r-project.org/src/contrib/GpGp_0.5.0.tar.gz",
	Developers: []cells.TagNameURL{
		{
			Tag:  "red",
			Name: "Cornell University",
			URL:  "https://www.cornell.edu",
		},
		{
			Tag:  "default",
			Name: "GpGp contributors",
			URL:  "https://github.com/joeguinness/GpGp/graphs/contributors",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "docs",
			URL:  "https://cran.r-project.org/web/packages/GpGp/GpGp.pdf",
		},
		{
			Name: "tutorials",
			URL:  "https://www.youtube.com/watch?v=phyB4n0CDWg&t=4s",
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

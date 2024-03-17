package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var GPstuff = rows.Library{
	PackageID:    "GPstuff",
	PackageName:  "GPstuff",
	PackageURL:   "https://research.cs.aalto.fi//pml/software/gpstuff/",
	Reference:    "Vanhatalo et al. (2017)",
	ReferenceURL: "https://jmlr.csail.mit.edu/papers/v14/vanhatalo13a.html",
	Language:     []string{"R", "Matlab", "Octave"},
	Licenses: []cells.NameURL{
		{
			Name: "GPL3",
			URL:  "https://github.com/gpstuff-dev/gpstuff/blob/develop/License.txt",
		},
	},
	Version:    "v4.7",
	VersionURL: "https://github.com/gpstuff-dev/gpstuff/releases/tag/v4.7",
	Developers: []cells.TagNameURL{
		{
			Tag:  "teal",
			Name: "University of Helsinki",
			URL:  "https://www.helsinki.fi/en",
		},
		{
			Tag:  "default",
			Name: "Aalto University of Science",
			URL:  "https://www.aalto.fi/en/department-of-computer-science",
		},
		{
			Tag:  "default",
			Name: "GPstuff contributors",
			URL:  "https://github.com/gpstuff-dev/gpstuff/graphs/contributors",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "docs",
			URL:  "https://arxiv.org/pdf/1206.5754.pdf",
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

package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var Magptk = rows.Library{
	PackageID:    "magptk",
	PackageName:  "magptk",
	PackageURL:   "https://games-uchile.github.io/mogptk/",
	Reference:    "de Wolff et al. (2020)",
	ReferenceURL: "https://www.sciencedirect.com/science/article/abs/pii/S0925231220317410?via%3Dihub",
	Language:     []string{"Python"},
	Licenses: []cells.NameURL{
		{
			Name: "MIT",
			URL:  "https://github.com/GAMES-UChile/mogptk/blob/master/LICENSE",
		},
	},
	Version:    "v0.5.1",
	VersionURL: "https://github.com/GAMES-UChile/mogptk/releases/tag/v0.5.1",
	Developers: []cells.TagNameURL{
		{
			Tag:  "purple",
			Name: "GAMES Universidad de Chile",
			URL:  "http://games.cmm.uchile.cl",
		},
		{
			Tag:  "default",
			Name: "mogptk contributors",
			URL:  "https://github.com/GAMES-UChile/mogptk/graphs/contributors",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "docs",
			URL:  "https://games-uchile.github.io/mogptk/",
		},
		{
			Name: "tutorials",
			URL:  "https://games-uchile.github.io/mogptk/examples.html?q=00_Quick_Start",
		},
		{
			Name: "examples",
			URL:  "https://games-uchile.github.io/mogptk/examples.html?q=example_airline_passengers",
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

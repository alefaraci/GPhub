package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var Egobox = rows.Library{
	PackageID:    "egobox",
	PackageName:  "egobox",
	PackageURL:   "https://github.com/relf/egobox",
	Reference:    "Lafage (2022)",
	ReferenceURL: "https://joss.theoj.org/papers/10.21105/joss.04737",
	Language:     []string{"Rust"},
	Licenses: []cells.NameURL{
		{
			Name: "Apache2",
			URL:  "https://github.com/relf/egobox/blob/master/LICENSE",
		},
	},
	Version:    "v0.15.3",
	VersionURL: "https://github.com/relf/egobox/releases/tag/0.15.3",
	Developers: []cells.TagNameURL{
		{
			Tag:  "uiBlue",
			Name: "ONERA",
			URL:  "https://www.onera.fr/en",
		},
		{
			Tag:  "blue",
			Name: "University of Toulouse",
			URL:  "http://en.univ-toulouse.fr",
		},
		{
			Tag:  "default",
			Name: "egobox contributors",
			URL:  "https://github.com/relf/egobox/graphs/contributors",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "docs",
			URL:  "https://github.com/relf/egobox/tree/master/doc",
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
					Name: "Constant",
				},
				{
					Tag:  "default",
					Name: "Linear",
				},
				{
					Tag:  "default",
					Name: "Quadratic",
				},
			},
			URL: "https://github.com/relf/egobox/tree/master/gp#current-state",
		},
	},
	LengthScale: []string{""},
	Correlation: []cells.TagGroup{
		{
			Group: []cells.TagName{
				{
					Tag:  "default",
					Name: "Squared Exponential",
				},
				{
					Tag:  "default",
					Name: "Absolute Exponetial",
				},
				{
					Tag:  "default",
					Name: "Matern32",
				},
				{
					Tag:  "default",
					Name: "Matern52",
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
			URL: "https://github.com/relf/egobox/tree/master/gp#current-state",
		},
	},
}

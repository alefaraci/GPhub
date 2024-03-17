package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var SMT = rows.Library{
	PackageID:    "SMT",
	PackageName:  "SMT",
	PackageURL:   "https://smt.readthedocs.io/en/latest/index.html",
	Reference:    "Saves et al. (2024)",
	ReferenceURL: "https://www.sciencedirect.com/science/article/abs/pii/S096599782300162X?via%3Dihub",
	Language:     []string{"Python"},
	Licenses: []cells.NameURL{
		{
			Name: "BSD3",
			URL:  "https://github.com/SMTorg/smt/blob/master/LICENSE.txt",
		},
	},
	Version:    "v2.3.0",
	VersionURL: "https://github.com/SMTorg/smt/releases/tag/v2.3.0",
	Developers: []cells.TagNameURL{
		{
			Tag:  "uiBlue",
			Name: "ISAE SUPEAERO",
			URL:  "https://www.isae-supaero.fr/en/",
		},
		{
			Tag:  "blue",
			Name: "NASA",
			URL:  "https://www.nasa.gov",
		},
		{
			Tag:  "uiBlue",
			Name: "ONERA",
			URL:  "https://www.onera.fr/en",
		},
		{
			Tag:  "blue",
			Name: "University of Michigan",
			URL:  "https://umich.edu",
		},
		{
			Tag:  "blue",
			Name: "University of San Diego",
			URL:  "https://www.sandiego.edu",
		},
		{
			Tag:  "red",
			Name: "Polytechnique Montréal",
			URL:  "https://www.polymtl.ca",
		},
		{
			Tag:  "default",
			Name: "SMT contributors",
			URL:  "https://github.com/SMTorg/smt/graphs/contributors",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "docs",
			URL:  "https://smt.readthedocs.io/en/stable/",
		},
		{
			Name: "tutorials",
			URL:  "https://github.com/SMTorg/smt/tree/master/tutorial",
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
			URL: "https://smt.readthedocs.io/en/latest/_src_docs/surrogate_models/krg.html",
		},
	},
	LengthScale: []string{"Isotropic", "Anisotropic"},
	Correlation: []cells.TagGroup{
		{
			Group: []cells.TagName{
				{
					Tag:  "default",
					Name: "Power Exponential",
				},
				{
					Tag:  "default",
					Name: "Absolute Exponetial",
				},
				{
					Tag:  "default",
					Name: "Squared Exponetial",
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
			URL: "https://smt.readthedocs.io/en/latest/_src_docs/surrogate_models/krg.html",
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

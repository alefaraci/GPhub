package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var DiceKriging = rows.Library{
	PackageID:    "DiceKriging",
	PackageName:  "DiceKriging",
	PackageURL:   "https://cran.r-project.org/package=DiceKriging",
	Reference:    "Roustant et al. (2012)",
	ReferenceURL: "https://www.jstatsoft.org/article/view/v051i01",
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
	Version:    "v1.6.0",
	VersionURL: "https://cran.r-project.org/web/packages/DiceKriging/ChangeLog",
	Developers: []cells.TagNameURL{
		{
			Tag:  "red",
			Name: "INSA Toulose",
			URL:  "https://www.insa-toulouse.fr",
		},
		{
			Tag:  "purple",
			Name: "Ecole des Mines de St-Etienne",
			URL:  "http://www.emse.fr",
		},
		{
			Tag:  "red",
			Name: "Universitat Bern",
			URL:  "https://www.unibe.ch/index_eng.html",
		},
		{
			Tag:  "blue",
			Name: "Alpestat",
			URL:  "http://www.alpestat.com",
		},
	},
	Docs: []cells.TagNameURL{
		{
			Tag:  "default",
			Name: "docs",
			URL:  "https://cran.r-project.org/web/packages/DiceKriging/DiceKriging.pdf",
		},
	},
	Support: []cells.TagNameURL{
		{
			Tag:  "default",
			Name: "blog",
			URL:  "https://dicekrigingclub.github.io/www/",
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
					Name: "Polynomial",
				},
			},
			URL: "https://cran.r-project.org/web/packages/DiceKriging/DiceKriging.pdf",
		},
	},
	LengthScale: []string{"Isotropic", "Anisotropic"},
	Correlation: []cells.TagGroup{
		{
			Group: []cells.TagName{
				{
					Tag:  "default",
					Name: "RBF",
				},
				{
					Tag:  "default",
					Name: "Exponetial",
				},
				{
					Tag:  "default",
					Name: "Matern32",
				},
				{
					Tag:  "default",
					Name: "Matern52",
				},
				{
					Tag:  "default",
					Name: "Power-exponential",
				},
			},
			URL: "https://cran.r-project.org/web/packages/DiceKriging/DiceKriging.pdf",
		},
	},
	Mixture: false,
	MixtureModels: []cells.TagGroup{
		{
			Group: []cells.TagName{
				{
					Tag:  "default",
					Name: "",
				},
			},
			URL: "",
		},
	},
}

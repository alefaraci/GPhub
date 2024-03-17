package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var UQLab = rows.Library{
	PackageID:    "UQLab",
	PackageName:  "UQLab",
	PackageURL:   "https://www.uqlab.com",
	Reference:    "Marelli et al. (2014)",
	ReferenceURL: "https://ascelibrary.org/doi/10.1061/9780784413609.257",
	Language:     []string{"Matlab"},
	Licenses: []cells.NameURL{
		{
			Name: "BSD3",
			URL:  "https://www.uqlab.com/copy-of-release-notes",
		},
	},
	Version:    "v2.0.0",
	VersionURL: "https://www.uqlab.com/release-notes",
	Developers: []cells.TagNameURL{
		{
			Tag:  "default",
			Name: "RSUQ ETH Zürich",
			URL:  "https://sudret.ibk.ethz.ch/software/uqlab.html",
		},
		{
			Tag:  "default",
			Name: "UQLab contributors",
			URL:  "https://www.uqlab.com/contributors",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "docs",
			URL:  "https://www.uqlab.com/documentation",
		},
		{
			Name: "user manuals",
			URL:  "https://www.uqlab.com/user-manuals",
		},
		{
			Name: "examples",
			URL:  "https://www.uqlab.com/examples",
		},
	},
	Support: []cells.NameURL{
		{
			Name: "contact form",
			URL:  "https://www.uqlab.com/contact",
		},
		{
			Name: "forum",
			URL:  "https://uqworld.org/c/uq-with-uqlab/7",
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
					Name: "Quadratic",
				},
				{
					Tag:  "default",
					Name: "Polynomial",
				},
				{
					Tag:  "default",
					Name: "Custom",
				},
			},
			URL: "https://uqftp.ethz.ch/uqlab_doc_html/2.0.0/UserManual_Kriging.html#pf39",
		},
	},
	LengthScale: []string{"Isotropic", "Anisotropic"},
	Correlation: []cells.TagGroup{
		{
			Group: []cells.TagName{
				{
					Tag:  "default",
					Name: "Linear",
				},
				{
					Tag:  "default",
					Name: "Exponential",
				},
				{
					Tag:  "default",
					Name: "Gaussian",
				},
				{
					Tag:  "default",
					Name: "Matern32",
				},
				{
					Tag:  "default",
					Name: "Materm52",
				},
			},
			URL: "https://uqftp.ethz.ch/uqlab_doc_html/2.0.0/UserManual_Kriging.html#pf25",
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

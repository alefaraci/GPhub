package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var GPML = rows.Library{
	PackageID:    "GPML",
	PackageName:  "GPML",
	PackageURL:   "http://gaussianprocess.org/gpml/code/matlab/doc/index.html",
	Reference:    "Rasmussen et al. (2010)",
	ReferenceURL: "https://jmlr.csail.mit.edu/papers/volume11/rasmussen10a/rasmussen10a.pdf",
	Language:     []string{"Matlab", "Octave"},
	Licenses: []cells.NameURL{
		{
			Name: "FreeBSD",
			URL:  "https://gitlab.com/hnickisch/gpml-matlab/-/blob/master/Copyright?ref_type=heads",
		},
	},
	Version:    "v4.2",
	VersionURL: "https://gitlab.com/hnickisch/gpml-matlab/-/releases/v4.2+dev2",
	Developers: []cells.TagNameURL{
		{
			Tag:  "yellow",
			Name: "University of Cambridge",
			URL:  "https://www.cam.ac.uk",
		},
		{
			Tag:  "teal",
			Name: "Max Planck Institute",
			URL:  "https://www.kyb.tuebingen.mpg.de",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "docs",
			URL:  "http://gaussianprocess.org/gpml/code/matlab/doc/",
		},
		{
			Name: "user manuals",
			URL:  "http://gaussianprocess.org/gpml/code/matlab/doc/manual.pdf",
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
					Name: "Zero",
				},
				{
					Tag:  "default",
					Name: "One",
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
				{
					Tag:  "default",
					Name: "Precomputed mean",
				},
				{
					Tag:  "default",
					Name: "Predictive",
				},
				{
					Tag:  "default",
					Name: "Nearest neighbor",
				},
				{
					Tag:  "default",
					Name: "Weighted sum of projected cosines",
				},
				{
					Tag:  "default",
					Name: "Scaled",
				},
				{
					Tag:  "default",
					Name: "Product",
				},
				{
					Tag:  "default",
					Name: "Power",
				},
				{
					Tag:  "default",
					Name: "Mask",
				},
				{
					Tag:  "default",
					Name: "Difference",
				},
				{
					Tag:  "default",
					Name: "Warped",
				},
			},
			URL: "http://gaussianprocess.org/gpml/code/matlab/doc/manual.pdf",
		},
	},
	LengthScale: []string{"Isotropic", "Anisotropic"},
	Correlation: []cells.TagGroup{
		{
			Group: []cells.TagName{
				{
					Tag:  "default",
					Name: "Constant",
				},
				{
					Tag:  "default",
					Name: "LinearWhite noise",
				},
				{
					Tag:  "default",
					Name: "Picewice Polynomial",
				},
				{
					Tag:  "default",
					Name: "Matern12",
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
					Name: "Rational Quadratic",
				},
				{
					Tag:  "default",
					Name: "Squared Exponential",
				},
			},
			URL: "http://gaussianprocess.org/gpml/code/matlab/doc/manual.pdf",
		},
	},
	Mixture: true,
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

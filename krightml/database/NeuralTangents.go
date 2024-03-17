package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var NeuralTangents = rows.Library{
	PackageID:    "NeuralTangents",
	PackageName:  "Neural Tangents",
	PackageURL:   "https://iclr.cc/virtual_2020/poster_SklD9yrFPS.html",
	Reference:    "Novak et al. (2020)",
	ReferenceURL: "https://openreview.net/pdf?id=SklD9yrFPS",
	Language:     []string{"Python"},
	Licenses: []cells.NameURL{
		{
			Name: "Apache2",
			URL:  "https://github.com/google/neural-tangents/blob/main/LICENSE",
		},
	},
	Version:    "v0.6.5",
	VersionURL: "https://github.com/google/neural-tangents/releases/tag/v0.6.5",
	Developers: []cells.TagNameURL{
		{
			Tag:  "green",
			Name: "Google Brain",
			URL:  "https://research.google/teams/brain/",
		},
		{
			Tag:  "yellow",
			Name: "University of Cambridge",
			URL:  "https://www.cam.ac.uk",
		},
		{
			Tag:  "default",
			Name: "Neural Tangents contributors",
			URL:  "https://github.com/google/neural-tangents/graphs/contributors",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "docs",
			URL:  "https://neural-tangents.readthedocs.io/en/latest/#",
		},
		{
			Name: "colab cookbook",
			URL:  "https://colab.research.google.com/github/google/neural-tangents/blob/main/notebooks/neural_tangents_cookbook.ipynb",
		},
		{
			Name: "talk",
			URL:  "https://iclr.cc/virtual_2020/poster_SklD9yrFPS.html",
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

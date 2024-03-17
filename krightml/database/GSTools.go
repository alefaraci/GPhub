package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var GSTools = rows.Library{
	PackageID:    "GSTools",
	PackageName:  "GSTools",
	PackageURL:   "https://geostat-framework.org",
	Reference:    "Müller et al. (2022)",
	ReferenceURL: "https://gmd.copernicus.org/articles/15/3161/2022/",
	Language:     []string{"Python"},
	Licenses: []cells.NameURL{
		{
			Name: "LGPL",
			URL:  "https://github.com/GeoStat-Framework/GSTools/blob/main/LICENSE",
		},
	},
	Version:    "v1.5.1",
	VersionURL: "https://github.com/GeoStat-Framework/GSTools/releases/tag/v1.5.1",
	Developers: []cells.TagNameURL{
		{
			Tag:  "blue",
			Name: "UFZ",
			URL:  "https://www.ufz.de",
		},
		{
			Tag:  "teal",
			Name: "University of Potsdam",
			URL:  "https://www.uni-potsdam.de/en/",
		},
		{
			Tag:  "blue",
			Name: "CASUS",
			URL:  "https://www.casus.science",
		},
		{
			Tag:  "yellow",
			Name: " Utrecht University",
			URL:  "https://www.uu.nl/en",
		},
		{
			Tag:  "default",
			Name: "GSTools contributors",
			URL:  "https://github.com/GeoStat-Framework/GSTools/graphs/contributors",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "docs",
			URL:  "https://geostat-framework.readthedocs.io/projects/gstools/en/stable/",
		},
		{
			Name: "tutorials",
			URL:  "https://geostat-framework.readthedocs.io/projects/gstools/en/stable/tutorials.html",
		},
		{
			Name: "API",
			URL:  "https://geostat-framework.readthedocs.io/projects/gstools/en/stable/api.html",
		},
	},
	Support: []cells.NameURL{
		{
			Name: "GitHub discussions",
			URL:  "https://github.com/GeoStat-Framework/GSTools/discussions",
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

package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var PyKrige = rows.Library{
	PackageID:    "PyKrige",
	PackageName:  "PyKrige",
	PackageURL:   "https://geostat-framework.readthedocs.io/projects/pykrige/en/stable/",
	Reference:    "Müller et al. (2022)",
	ReferenceURL: "https://gmd.copernicus.org/articles/15/3161/2022/",
	Language:     []string{"Python"},
	Licenses: []cells.NameURL{
		{
			Name: "BSD3",
			URL:  "https://github.com/GeoStat-Framework/PyKrige/blob/main/LICENSE",
		},
	},
	Version:    "v1.7.1",
	VersionURL: "https://github.com/GeoStat-Framework/PyKrige/releases/tag/v1.7.1",
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
			Name: "PyKrige contributors",
			URL:  "https://github.com/GeoStat-Framework/PyKrige/graphs/contributors",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "docs",
			URL:  "https://buildmedia.readthedocs.org/media/pdf/pykrige/latest/pykrige.pdf",
		},
		{
			Name: "examples",
			URL:  "https://geostat-framework.readthedocs.io/projects/pykrige/en/stable/examples/index.html",
		},
		{
			Name: "API",
			URL:  "https://geostat-framework.readthedocs.io/projects/pykrige/en/stable/api.html",
		},
	},
	Support: []cells.NameURL{
		{
			Name: "GitHub discussions",
			URL:  "https://github.com/GeoStat-Framework/PyKrige/discussions",
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

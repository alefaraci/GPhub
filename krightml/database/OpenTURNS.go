package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var OpenTURNS = rows.Library{
	PackageID:    "OpenTURNS",
	PackageName:  "OpenTURNS",
	PackageURL:   "https://openturns.github.io/www/",
	Reference:    "Baudin et al. (2016)",
	ReferenceURL: "https://link.springer.com/referenceworkentry/10.1007/978-3-319-11259-6_64-1",
	Language:     []string{"Cpp", "Python"},
	Licenses: []cells.NameURL{
		{
			Name: "LGPL",
			URL:  "https://github.com/openturns/openturns/blob/master/LICENSE",
		},
	},
	Version:    "v1.22",
	VersionURL: "https://github.com/openturns/openturns/releases/tag/v1.22",
	Developers: []cells.TagNameURL{
		{
			Tag:  "blue",
			Name: "Airbus Group",
			URL:  "https://www.airbus.com/en",
		},
		{
			Tag:  "orange",
			Name: "EDF R&D",
			URL:  "https://www.edf.fr/en/the-edf-group/inventing-the-future-of-energy/r-d-global-expertise",
		},
		{
			Tag:  "blue",
			Name: "Phimeca Engineering",
			URL:  "https://www.phimeca.com",
		},
		{
			Tag:  "red",
			Name: "IMACS",
			URL:  "https://imacs.polytechnique.fr",
		},
		{
			Tag:  "uiBlue",
			Name: "ONERA",
			URL:  "https://www.onera.fr/en",
		},
		{
			Tag:  "default",
			Name: "OpenTURNS contributors",
			URL:  "https://github.com/openturns/openturns/graphs/contributors",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "docs",
			URL:  "http://openturns.github.io/openturns/latest/contents.html",
		},
	},
	Support: []cells.NameURL{
		{
			Name: "chat",
			URL:  "https://app.gitter.im/#/room/#openturns_community:gitter.im",
		},
		{
			Name: "forum",
			URL:  "https://openturns.discourse.group",
		},
		{
			Name: "stackoverflow",
			URL:  "https://stackoverflow.com/questions/tagged/openturns",
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

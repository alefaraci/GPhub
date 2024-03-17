package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var STAN = rows.Library{
	PackageID:    "STAN",
	PackageName:  "STAN",
	PackageURL:   "https://mc-stan.org",
	Reference:    "Stan Development Team (2017)",
	ReferenceURL: "https://zenodo.org/records/1101116",
	Language:     []string{"R", "Cpp", "Julia", "Python", "Matlab"},
	Licenses: []cells.NameURL{
		{
			Name: "BSD3",
			URL:  "https://github.com/brian-lau/MatlabStan/blob/master/LICENSE.txt",
		},
		{
			Name: "GPL3",
			URL:  "https://github.com/stan-dev/rstan/blob/develop/licenses/rstan-license.txt",
		},
		{
			Name: "MIT",
			URL:  "https://github.com/StanJulia/Stan.jl/blob/master/LICENSE.md",
		},
	},
	Version:    "v2.15.1",
	VersionURL: "https://zenodo.org/records/1101116",
	Developers: []cells.TagNameURL{
		{
			Tag:  "default",
			Name: "Stan Development Team",
			URL:  "https://github.com/orgs/stan-dev/people",
		},
		{
			Tag:  "orange",
			Name: "NumFOCUS",
			URL:  "https://numfocus.org",
		},
		{
			Tag:  "default",
			Name: "Stan contributors",
			URL:  "https://github.com/stan-dev/stan/graphs/contributors",
		},
		{
			Tag:  "default",
			Name: "MatlabStan contributors",
			URL:  "https://github.com/brian-lau/MatlabStan/graphs/contributors",
		},
		{
			Tag:  "default",
			Name: "RStan contributors",
			URL:  "https://github.com/stan-dev/rstan/graphs/contributors",
		},
		{
			Tag:  "default",
			Name: "pyStan contributors",
			URL:  "https://github.com/stan-dev/pystan/graphs/contributors",
		},
		{
			Tag:  "default",
			Name: "Stan.jl contributors",
			URL:  "https://github.com/StanJulia/Stan.jl/graphs/contributors",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "docs",
			URL:  "https://mc-stan.org/docs/stan-users-guide/gaussian-processes.html",
		},
		{
			Name: "r docs",
			URL:  "https://cran.r-project.org/web/packages/rstan/rstan.pdf",
		},
		{
			Name: "mat docs",
			URL:  "https://github.com/brian-lau/MatlabStan/wiki",
		},
		{
			Name: "py docs",
			URL:  "https://pystan.readthedocs.io/en/latest/",
		},
		{
			Name: "jl docs",
			URL:  "https://github.com/StanJulia/Stan.jl/tree/master/docs",
		},
	},
	Support: []cells.NameURL{
		{
			Name: "forum",
			URL:  "https://discourse.mc-stan.org",
		},
		{
			Name: "slack",
			URL:  "https://mc-stan.slack.com/join/shared_invite/zt-1le4ebi4m-UMtiOkJb4gcS16qz2wIYCw#/shared-invite/email",
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

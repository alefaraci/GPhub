package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var Surrogatesjl = rows.Library{
	PackageID:    "Surrogatesjl",
	PackageName:  "Surrogates.jl",
	PackageURL:   "https://docs.sciml.ai/Surrogates/stable/",
	Reference:    "",
	ReferenceURL: "",
	Language:     []string{"Julia"},
	Licenses: []cells.NameURL{
		{
			Name: "MIT",
			URL:  "https://github.com/SciML/Surrogates.jl/blob/master/LICENSE.md",
		},
	},
	Version:    "v6.9.0",
	VersionURL: "https://github.com/SciML/Surrogates.jl/releases",
	Developers: []cells.TagNameURL{
		{
			Tag:  "red",
			Name: "Chan Zuckerberg Initiative",
			URL:  "https://chanzuckerberg.com",
		},
		{
			Tag:  "default",
			Name: "Wellcome Trust",
			URL:  "https://wellcome.org",
		},
		{
			Tag:  "orange",
			Name: "Microsoft",
			URL:  "https://www.microsoft.com/en-us/research/collaboration/studies-in-pandemic-preparedness/overview/",
		},
		{
			Tag:  "default",
			Name: "Surrogates.jl contributors",
			URL:  "https://github.com/SciML/Surrogates.jl/graphs/contributors",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "docs",
			URL:  "https://docs.sciml.ai/Surrogates/stable/kriging/",
		},
	},
	Support: []cells.NameURL{
		{
			Name: "chat",
			URL:  "https://julialang.zulipchat.com/#narrow/stream/279055-sciml-bridged",
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

package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var Stheno = rows.Library{
	PackageID:    "Stheno",
	PackageName:  "Stheno",
	PackageURL:   "https://wessel.ai/stheno/docs/_build/html/index.html",
	Reference:    "Tebbutt et al. (2019)",
	ReferenceURL: "https://willtebbutt.github.io/resources/stheno_juliacon_2019.pdf",
	Language:     []string{"Julia", "Python"},
	Licenses: []cells.NameURL{
		{
			Name: "MIT",
			URL:  "https://github.com/JuliaGaussianProcesses/Stheno.jl/blob/master/LICENSE.md",
		},
	},
	Version:    "v0.8.2",
	VersionURL: "https://github.com/JuliaGaussianProcesses/Stheno.jl/releases/tag/v0.8.2",
	Developers: []cells.TagNameURL{
		{
			Tag:  "yellow",
			Name: "University of Cambridge",
			URL:  "https://www.cam.ac.uk",
		},
		{
			Tag:  "default",
			Name: "Stheno.jl contributors",
			URL:  "https://github.com/JuliaGaussianProcesses/Stheno.jl/graphs/contributors",
		},
		{
			Tag:  "default",
			Name: "Stheno py contributors",
			URL:  "https://github.com/wesselb/stheno/graphs/contributors",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "py docs",
			URL:  "https://wessel.ai/stheno/docs/_build/html/index.html",
		},
		{
			Name: "jl docs",
			URL:  "https://juliagaussianprocesses.github.io/Stheno.jl/stable/",
		},
		{
			Name: "py examples",
			URL:  "https://wessel.ai/stheno/docs/_build/html/readme.html#examples",
		},
		{
			Name: "jl examples",
			URL:  "https://juliagaussianprocesses.github.io/Stheno.jl/stable/examples_note/",
		},
		{
			Name: "py API",
			URL:  "https://wessel.ai/stheno/docs/_build/html/api.html",
		},
		{
			Name: "jl API",
			URL:  "https://juliagaussianprocesses.github.io/Stheno.jl/stable/api/",
		},
		{
			Name: "talk",
			URL:  "https://www.youtube.com/watch?v=OO3BBkGEMV8",
		},
	},
	Support: []cells.NameURL{
		{
			Name: "GitHub discussions",
			URL:  "https://github.com/wesselb/stheno/discussions",
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

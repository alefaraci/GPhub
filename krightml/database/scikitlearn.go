package database

import (
	"github.com/alefaraci/krightml/table/cells"
	"github.com/alefaraci/krightml/table/rows"
)

var Scikitlearn = rows.Library{
	PackageID:    "scikitlearn",
	PackageName:  "scikit-learn",
	PackageURL:   "https://scikit-learn.org/stable/#",
	Reference:    "Pedregosa et al. (2011)",
	ReferenceURL: "https://jmlr.csail.mit.edu/papers/v12/pedregosa11a.html",
	Language:     []string{"Python"},
	Licenses: []cells.NameURL{
		{
			Name: "BSD3",
			URL:  "https://github.com/scikit-learn/scikit-learn/blob/main/COPYING",
		},
	},
	Version:    "v1.4.1",
	VersionURL: "https://github.com/scikit-learn/scikit-learn/releases/tag/1.4.1.post1",
	Developers: []cells.TagNameURL{
		{
			Tag:  "teal",
			Name: "Community driven",
			URL:  "https://scikit-learn.org/stable/about.html#people",
		},
		{
			Tag:  "green",
			Name: "NVIDIA",
			URL:  "https://www.nvidia.com",
		},
		{
			Tag:  "red",
			Name: "INRIA",
			URL:  "https://www.inria.fr/en",
		},
		{
			Tag:  "yellow",
			Name: "Hugging Face",
			URL:  "https://huggingface.co",
		},
		{
			Tag:  "orange",
			Name: "Microsoft",
			URL:  "https://www.microsoft.com",
		},
		{
			Tag:  "default",
			Name: "Quansight Labs",
			URL:  "https://www.quansight.com/labs",
		},
		{
			Tag:  "default",
			Name: "sci-kit-learn contributors",
			URL:  "https://github.com/scikit-learn/scikit-learn/graphs/contributors",
		},
	},
	Docs: []cells.NameURL{
		{
			Name: "docs",
			URL:  "https://scikit-learn.org/stable/modules/gaussian_process.html",
		},
		{
			Name: "examples",
			URL:  "https://scikit-learn.org/stable/auto_examples/index.html#gaussian-process-for-machine-learning",
		},
		{
			Name: "tutorials",
			URL:  "https://scikit-learn.org/stable/tutorial/index.html",
		},
		{
			Name: "API",
			URL:  "https://scikit-learn.org/stable/modules/classes.html",
		},
	},
	Support: []cells.NameURL{
		{
			Name: "blog",
			URL:  "https://blog.scikit-learn.org",
		},
		{
			Name: "stackoverflow",
			URL:  "https://stackoverflow.com/questions/tagged/scikit-learn",
		},
		{
			Name: "GitHub discussions",
			URL:  "https://github.com/scikit-learn/scikit-learn/discussions",
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
			},
			URL: "https://scikit-learn.org/stable/modules/gaussian_process.html",
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

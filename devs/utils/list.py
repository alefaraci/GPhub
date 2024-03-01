# LIST OF PACKAGES INFORMATIONS

"""
EXAMPLE:
----------------
    "": {
        "URL": "",
        "Language": [""],
        "License": {
            "type": [""],
            "URL": [""],
        },
        "Reference": {
            "Authors": " et al. (2017)",
            "URL": "",
        },
        "Release": {
            "version": "v",
            "URL": "",
        },
        "Developers": [
            {
                "color": "",
                "name": "",
                "URL": "",
            },
        ],
        "Docs": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
"""

packages = {
    # ===============================================
    "DiceKriging": {
        "URL": "https://cran.r-project.org/package=DiceKriging",
        "Language": ["R"],
        "License": {
            "type": ["GPL2", "GPL3"],
            "URL": [
                "https://cran.r-project.org/web/licenses/GPL-2",
                "https://cran.r-project.org/web/licenses/GPL-3",
            ],
        },
        "Reference": {
            "Authors": "Roustant et al. (2012)",
            "URL": "https://www.jstatsoft.org/article/view/v051i01",
        },
        "Release": {
            "version": "v1.6.0",
            "URL": "https://cran.r-project.org/web/packages/DiceKriging/ChangeLog",
        },
        "Developers": [
            {
                "color": "red",
                "name": "INSA Toulose",
                "URL": "https://www.insa-toulouse.fr",
            },
            {
                "color": "purple",
                "name": "Ecole des Mines de St-Etienne",
                "URL": "http://www.emse.fr",
            },
            {
                "color": "red",
                "name": "Universitat Bern",
                "URL": "https://www.unibe.ch/index_eng.html",
            },
            {
                "color": "blue",
                "name": "Alpestat",
                "URL": "http://www.alpestat.com",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://cran.r-project.org/web/packages/DiceKriging/DiceKriging.pdf",
            },
        ],
        "Support": [
            {
                "tag": "blog",
                "URL": "https://dicekrigingclub.github.io/www/",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [
                "Zero",
                "Constant",
                "Linear",
                "Polynomial",
            ],
            "URL": "https://cran.r-project.org/web/packages/DiceKriging/DiceKriging.pdf",
        },
        "Kernel": {
            "LengthScale": [
                "Isotropic",
                "Anisotropic",
            ],
            "Families": {
                "tag": [
                    "RBF",
                    "Exponetial",
                    "Matern32",
                    "Matern52",
                    "Power-exponential",
                ],
                "URL": "https://cran.r-project.org/web/packages/DiceKriging/DiceKriging.pdf",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "egobox": {
        "URL": "https://github.com/relf/egobox",
        "Language": ["Rust"],
        "License": {
            "type": ["Apache2"],
            "URL": ["https://github.com/relf/egobox/blob/master/LICENSE"],
        },
        "Reference": {
            "Authors": "Lafage (2022)",
            "URL": "https://joss.theoj.org/papers/10.21105/joss.04737",
        },
        "Release": {
            "version": "v0.15.3",
            "URL": "https://github.com/relf/egobox/releases/tag/0.15.3",
        },
        "Developers": [
            {
                "color": "uiBlue",
                "name": "ONERA",
                "URL": "https://www.onera.fr/en",
            },
            {
                "color": "blue",
                "name": "University of Toulouse",
                "URL": "http://en.univ-toulouse.fr",
            },
            {
                "color": "default",
                "name": "egobox contributors",
                "URL": "https://github.com/relf/egobox/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://github.com/relf/egobox/tree/master/doc",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [
                "Constant",
                "Linear",
                "Quadratic",
            ],
            "URL": "https://github.com/relf/egobox/tree/master/gp#current-state",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [
                    "Squared Exponential",
                    "Absolute Exponetial",
                    "Matern32",
                    "Matern52",
                ],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "https://github.com/relf/egobox/tree/master/gp#current-state",
            },
        },
    },
    # ===============================================
    "fbm": {
        "URL": "https://glizen.com/radfordneal/fbm.software.html",
        "Language": ["C"],
        "License": {
            "type": ["BSL1"],
            "URL": ["https://gitlab.com/radfordneal/fbm/-/blob/master/README?ref_type=heads"],
        },
        "Reference": {
            "Authors": "Neal (1996)",
            "URL": "https://link.springer.com/book/10.1007/978-1-4612-0745-0",
        },
        "Release": {
            "version": "v2022-04-21",
            "URL": "https://glizen.com/radfordneal/fbm.2022-04-21.doc/Release.2022-04-21.html",
        },
        "Developers": [
            {
                "color": "blue",
                "name": "University of Toronto",
                "URL": "https://www.statistics.utoronto.ca",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://glizen.com/radfordneal/fbm.2022-04-21.doc/index.html",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": ["Zero"],
            "URL": "https://glizen.com/radfordneal/fbm.2022-04-21.doc/gp.html ",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "GPflow": {
        "URL": "https://www.gpflow.org",
        "Language": ["Python"],
        "License": {
            "type": ["Apache2"],
            "URL": ["https://github.com/GPflow/GPflow/blob/develop/LICENSE"],
        },
        "Reference": {
            "Authors": "Matthews et al. (2017)",
            "URL": "https://jmlr.org/papers/v18/16-537.html",
        },
        "Release": {
            "version": "v2.9.1",
            "URL": "https://github.com/GPflow/GPflow/releases/tag/v2.9.1",
        },
        "Developers": [
            {
                "color": "yellow",
                "name": "University of Cambridge",
                "URL": "https://www.cam.ac.uk",
            },
            {
                "color": "blue",
                "name": "University of Oxford",
                "URL": "https://www.ox.ac.uk",
            },
            {
                "color": "blue",
                "name": "Kyoto University",
                "URL": "https://www.kyoto-u.ac.jp",
            },
            {
                "color": "default",
                "name": "University of Edinburgh",
                "URL": "https://www.ed.ac.uk",
            },
            {
                "color": "purple",
                "name": "The University of Manchster",
                "URL": "https://www.manchester.ac.uk",
            },
            {
                "color": "red",
                "name": "Lancaster University",
                "URL": "https://www.lancaster.ac.uk",
            },
            {
                "color": "default",
                "name": "GPflow contributors",
                "URL": "https://github.com/GPflow/GPflow/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://gpflow.github.io/GPflow/develop/getting_started.html",
            }
        ],
        "Support": [
            {
                "tag": "slack",
                "URL": "https://gpflow.slack.com/join/shared_invite/enQtOTE5MDA0Nzg5NjA2LTYwZWI3MzhjYjNlZWI1MWExYzZjMGNhOWIwZWMzMGY0YjVkYzAyYjQ4NjgzNDUyZTgyNzcwYjAyY2QzMWRmYjE#/shared-invite/email",
            },
            {
                "tag": "GitHub discussions",
                "URL": "https://github.com/GPflow/GPflow/discussions",
            },
            {
                "tag": "stackoverflow",
                "URL": "https://stackoverflow.com/tags/gpflow",
            },
        ],
        "Framework": [
            {
                "tag": "TensorFlow",
                "URL": "https://www.tensorflow.org",
            },
        ],
        "GPU": True,
        "Trend": {
            "tag": [
                "Zero",
                "Polynomial",
                "Additive",
                "Constant",
                "Function",
                "Identity",
                "Linear",
                "Product",
                "Switched Function",
            ],
            "URL": "https://gpflow.github.io/GPflow/develop/api/gpflow/functions/index.html#gpflow.functions.MeanFunction",
        },
        "Kernel": {
            "LengthScale": ["Isotropic", "Anisotropic"],
            "Families": {
                "tag": [
                    "ArcCosine",
                    "Bias",
                    "Change Points",
                    # "Combination",
                    "Constant",
                    "Convolutional",
                    "Coregion",
                    "Cosine",
                    "Exponential",
                    "Independent Latent",
                    "Linear",
                    "Linear Coregionaliztion",
                    "Matern12",
                    "Matern32",
                    "Matern52",
                    "Multioutput",
                    "Periodic",
                    "Polynomial",
                    # "Product",
                    "RBF",
                    "Rational Quadratic",
                    "Separate Independent",
                    "Shared Independent",
                    "Squared Exponential",
                    "Static",
                    "Stationary",
                    # "Sum",
                    "White",
                ],
                "URL": "https://gpflow.github.io/GPflow/develop/api/gpflow/kernels/index.html",
            },
            "Mixture": {
                "check": True,
                "tag": ["Combination", "Product", "Sum"],
                "URL": "https://gpflow.github.io/GPflow/develop/api/gpflow/kernels/index.html",
            },
        },
    },
    # ===============================================
    "GPflux": {
        "URL": "https://secondmind-labs.github.io/GPflux/#",
        "Language": ["Python"],
        "License": {
            "type": ["Apache2"],
            "URL": ["https://github.com/secondmind-labs/GPflux/blob/develop/LICENSE"],
        },
        "Reference": {
            "Authors": "Dutordoir et al. (2021)",
            "URL": "https://arxiv.org/abs/2104.05674",
        },
        "Release": {
            "version": "v0.4.3",
            "URL": "https://github.com/secondmind-labs/GPflux/releases/tag/v0.4.3",
        },
        "Developers": [
            {
                "color": "yellow",
                "name": "University of Cambridge",
                "URL": "https://www.cam.ac.uk",
            },
            {
                "color": "purple",
                "name": "Imperial College London",
                "URL": "https://www.imperial.ac.uk",
            },
            {
                "color": "purple",
                "name": "University College London",
                "URL": "https://www.ucl.ac.uk",
            },
            {
                "color": "purple",
                "name": "Secondimind labs",
                "URL": "https://www.secondmind.ai",
            },
            {
                "color": "default",
                "name": "GPflux contributors",
                "URL": "https://github.com/secondmind-labs/GPflux/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://secondmind-labs.github.io/GPflux/#getting-started",
            },
            {
                "tag": "tutorials",
                "URL": "https://secondmind-labs.github.io/GPflux/tutorials.html",
            },
            {
                "tag": "API",
                "URL": "https://secondmind-labs.github.io/GPflux/autoapi/gpflux/index.html",
            },
        ],
        "Support": [
            {
                "tag": "slack",
                "URL": "https://secondmind-labs.slack.com/join/shared_invite/zt-ph07nuie-gMlkle__tjvXBay4FNSLkw#/shared-invite/email",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "GPML": {
        "URL": "http://gaussianprocess.org/gpml/code/matlab/doc/index.html",
        "Language": ["Matlab", "Octave"],
        "License": {
            "type": ["FreeBSD"],
            "URL": ["https://gitlab.com/hnickisch/gpml-matlab/-/blob/master/Copyright?ref_type=heads"],
        },
        "Reference": {
            "Authors": "Rasmussen et al. (2010)",
            "URL": "https://jmlr.csail.mit.edu/papers/volume11/rasmussen10a/rasmussen10a.pdf",
        },
        "Release": {
            "version": "v4.2",
            "URL": "https://gitlab.com/hnickisch/gpml-matlab/-/releases/v4.2+dev2",
        },
        "Developers": [
            {
                "color": "yellow",
                "name": "University of Cambridge",
                "URL": "https://www.cam.ac.uk",
            },
            {
                "color": "teal",
                "name": "Max Planck Institute",
                "URL": "https://www.kyb.tuebingen.mpg.de",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "http://gaussianprocess.org/gpml/code/matlab/doc/",
            },
            {
                "tag": "user manual",
                "URL": "http://gaussianprocess.org/gpml/code/matlab/doc/manual.pdf",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [
                "Zero",
                "One",
                "Constant",
                "Linear",
                "Polynomial",
                "Precomputed mean",
                "Predictive",
                "Nearest neighbor",
                "Weighted sum of projected cosines",
                "Scaled",
                "Product",
                "Power",
                "Mask",
                "Difference",
                "Warped",
            ],
            "URL": "http://gaussianprocess.org/gpml/code/matlab/doc/manual.pdf",
        },
        "Kernel": {
            "LengthScale": ["Isotropic", "Anisotropic"],
            "Families": {
                "tag": [
                    "Constant",
                    "Linear" "White noise",
                    "Picewice Polynomial",
                    "Matern12",
                    "Matern32",
                    "Matern52",
                    "Rational Quadratic",
                    "Squared Exponential",
                ],
                "URL": "http://gaussianprocess.org/gpml/code/matlab/doc/manual.pdf",
            },
            "Mixture": {
                "check": True,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "GPR": {
        "URL": "https://github.com/ChristophJud/GPR",
        "Reference": {
            "Authors": "n/a",
            "URL": "",
        },
        "Language": ["Cpp"],  # No language information provided in the snippet
        "License": {
            "type": ["Apache2"],
            "URL": ["https://github.com/ChristophJud/GPR/blob/master/LICENSE"],
        },
        "Release": {
            "version": "n/a",
            "URL": "",
        },
        "Developers": [
            {
                "color": "teal",
                "name": "University of Basel",
                "URL": "https://www.unibas.ch",
            },
        ],
        "Docs": [
            {
                "tag": "",
                "URL": "",
            }
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": ["White", "RBF", "Periodic", "Rational Quadratic"],
                "URL": "",
            },
            "Mixture": {
                "check": True,
                "tag": ["Sum", "Product"],
                "URL": "",
            },
        },
    },
    # ===============================================
    "GPstuff": {
        "URL": "https://research.cs.aalto.fi//pml/software/gpstuff/",
        "Reference": {
            "Authors": "Vanhatalo et al. (2017)",
            "URL": "https://jmlr.csail.mit.edu/papers/v14/vanhatalo13a.html",
        },
        "Language": ["R", "Matlab", "Octave"],
        "License": {
            "type": ["GPL3"],
            "URL": ["https://github.com/gpstuff-dev/gpstuff/blob/develop/License.txt"],
        },
        "Release": {
            "version": "v4.7",
            "URL": "https://github.com/gpstuff-dev/gpstuff/releases/tag/v4.7",
        },
        "Developers": [
            {
                "color": "teal",
                "name": "University of Helsinki",
                "URL": "https://www.helsinki.fi/en",
            },
            {
                "color": "default",
                "name": "Aalto University of Science",
                "URL": "https://www.aalto.fi/en/department-of-computer-science",
            },
            {
                "color": "default",
                "name": "GPstuff contributors",
                "URL": "https://github.com/gpstuff-dev/gpstuff/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://arxiv.org/pdf/1206.5754.pdf",
            }
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "GPvecchia": {
        "URL": "https://cran.r-project.org/package=GPvecchia",
        "Language": ["R"],
        "License": {
            "type": ["GPL2", "GPL3"],
            "URL": [
                "https://cran.r-project.org/web/licenses/GPL-2",
                "https://cran.r-project.org/web/licenses/GPL-3",
            ],
        },
        "Reference": {
            "Authors": "Katzfuss et al. (2017)",
            "URL": "https://arxiv.org/abs/1708.06302",
        },
        "Release": {
            "version": "v0.1.6",
            "URL": "https://cran.r-project.org/src/contrib/GPvecchia_0.1.6.tar.gz",
        },
        "Developers": [
            {
                "color": "brown",
                "name": "Texas A&M University",
                "URL": "https://www.tamu.edu",
            },
            {
                "color": "red",
                "name": "Cornell University",
                "URL": "https://www.cornell.edu",
            },
            {
                "color": "default",
                "name": "GPvecchia contributors",
                "URL": "https://github.com/katzfuss-group/GPvecchia/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://cran.r-project.org/web/packages/GPvecchia/GPvecchia.pdf",
            },
            {
                "tag": "tutorials",
                "URL": "https://cran.r-project.org/web/packages/GPvecchia/vignettes/GPvecchia_vignette.html",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "GPy": {
        "URL": "https://sheffieldml.github.io/GPy/",
        "Reference": {
            "Authors": "GPy (2012)",
            "URL": "http://github.com/SheffieldML/GPy",
        },
        "Language": ["Python"],
        "License": {
            "type": ["BSD3"],
            "URL": ["https://github.com/SheffieldML/GPy/blob/devel/LICENSE.txt"],
        },
        "Release": {
            "version": "v1.13.1",
            "URL": "https://github.com/SheffieldML/GPy/releases/tag/v1.13.1",
        },
        "Developers": [
            {
                "color": "purple",
                "name": "University of Sheffield",
                "URL": "https://www.sheffield.ac.uk/dcs/research/groups/machine-learning",
            },
            {
                "color": "default",
                "name": "GPy contributors",
                "URL": "https://github.com/SheffieldML/GPy/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://gpy.readthedocs.io/en/deploy/",
            },
            {
                "tag": "jupyter notebooks",
                "URL": "https://nbviewer.org/github/SheffieldML/notebook/blob/master/GPy/index.ipynb",
            },
        ],
        "Support": [
            {
                "tag": "mailing-list",
                "URL": "https://lists.shef.ac.uk/sympa/subscribe/gpy-users",
            },
            {
                "tag": "GitHub discussions",
                "URL": "https://github.com/SheffieldML/GPy/discussions",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "GPyTorch": {
        "URL": "https://gpytorch.ai",
        "Language": ["Python"],
        "License": {
            "type": ["MIT"],
            "URL": ["https://github.com/cornellius-gp/gpytorch/blob/master/LICENSE"],
        },
        "Reference": {
            "Authors": "Gardner et al. (2018)",
            "URL": "https://arxiv.org/abs/1809.11165",
        },
        "Release": {
            "version": "v1.11",
            "URL": "https://github.com/cornellius-gp/gpytorch/releases/tag/v1.11",
        },
        "Developers": [
            {
                "color": "red",
                "name": "Cornell University",
                "URL": "https://www.cornell.edu/",
            },
            {
                "color": "blue",
                "name": "The University of British Columbia",
                "URL": "https://www.ubc.ca",
            },
            {
                "color": "blue",
                "name": "Meta",
                "URL": "https://research.facebook.com",
            },
            {
                "color": "purple",
                "name": "New York University",
                "URL": "https://www.nyu.edu/",
            },
            {
                "color": "brown",
                "name": "University of Pennsylvania",
                "URL": "https://www.upenn.edu/",
            },
            {
                "color": "default",
                "name": "GPyTorch contributors",
                "URL": "https://github.com/cornellius-gp/gpytorch/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://docs.gpytorch.ai/en/stable/",
            },
            {
                "tag": "examples",
                "URL": "https://github.com/cornellius-gp/gpytorch/tree/master/examples/",
            },
        ],
        "Support": [
            {
                "tag": "stackoverflow",
                "URL": "https://stackoverflow.com/questions/tagged/gpytorch",
            },
            {
                "tag": "GitHub discussions",
                "URL": "https://github.com/cornellius-gp/gpytorch/discussions",
            },
        ],
        "Framework": [
            {
                "tag": "PyTorch",
                "URL": "https://pytorch.org/",
            },
        ],
        "GPU": True,
        "Trend": {
            "tag": [
                "Zero",
                "Constant",
                "Linear",
            ],
            "URL": "https://docs.gpytorch.ai/en/stable/kernels.html",
        },
        "Kernel": {
            "LengthScale": [
                "Isotropic",
                "Anisotropic",
            ],
            "Families": {
                "tag": [
                    "Cosine",
                    "Cylindrical",
                    "Linear",
                    "Matern",
                    "Periodic",
                    "Picewise Polynomial",
                    "Polynomial",
                    "RBF",
                    "RQK",
                    "Spectral Delta",
                    # "Spectral Mixture",
                    # "Additive",
                    # "Product",
                    # "Scale",
                    "Arc",
                    "Index",
                    "LCMK",
                    "Multitask",
                    "Grid",
                    "Grid Interpolation",
                    "Inducing Point",
                    "RFFK",
                ],
                "URL": "https://docs.gpytorch.ai/en/stable/kernels.html",
            },
            "Mixture": {
                "check": True,
                "tag": [
                    "Spectral Mixture",
                    "Additive",
                    "Product",
                    "Scale",
                ],
                "URL": "https://docs.gpytorch.ai/en/stable/kernels.html",
            },
        },
    },
    # ===============================================
    "OpenTURNS": {
        "URL": "https://openturns.github.io/www/",
        "Language": ["Cpp", "Python"],
        "License": {
            "type": ["LGPL"],
            "URL": ["https://github.com/openturns/openturns/blob/master/LICENSE"],
        },
        "Reference": {
            "Authors": "Baudin et al. (2016)",
            "URL": "https://link.springer.com/referenceworkentry/10.1007/978-3-319-11259-6_64-1",
        },
        "Release": {
            "version": "v1.22",
            "URL": "https://github.com/openturns/openturns/releases/tag/v1.22",
        },
        "Developers": [
            {
                "color": "blue",
                "name": "Airbus Group",
                "URL": "https://www.airbus.com/en",
            },
            {
                "color": "orange",
                "name": "EDF R&D",
                "URL": "https://www.edf.fr/en/the-edf-group/inventing-the-future-of-energy/r-d-global-expertise",
            },
            {
                "color": "blue",
                "name": "Phimeca Engineering",
                "URL": "https://www.phimeca.com",
            },
            {
                "color": "red",
                "name": "IMACS",
                "URL": "https://imacs.polytechnique.fr",
            },
            {
                "color": "uiBlue",
                "name": "ONERA",
                "URL": "https://www.onera.fr/en",
            },
            {
                "color": "default",
                "name": "OpenTURNS contributors",
                "URL": "https://github.com/openturns/openturns/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "http://openturns.github.io/openturns/latest/contents.html",
            },
        ],
        "Support": [
            {
                "tag": "chat",
                "URL": "https://app.gitter.im/#/room/#openturns_community:gitter.im",
            },
            {
                "tag": "forum",
                "URL": "https://openturns.discourse.group",
            },
            {
                "tag": "stackoverflow",
                "URL": "https://stackoverflow.com/questions/tagged/openturns",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "PyMC": {
        "URL": "https://www.pymc.io/welcome.html",
        "Language": ["Python"],
        "License": {
            "type": ["Apache2"],
            "URL": ["https://github.com/pymc-devs/pymc/blob/main/LICENSE"],
        },
        "Reference": {
            "Authors": "Abril-Pla et al. (2023)",
            "URL": "https://peerj.com/articles/cs-1516/",
        },
        "Release": {
            "version": "v5.10.4",
            "URL": "https://github.com/pymc-devs/pymc/releases/tag/v5.10.4",
        },
        "Developers": [
            {
                "color": "teal",
                "name": "ArviZ-Devs",
                "URL": "https://arviz-devs.github.io/arviz/",
            },
            {
                "color": "red",
                "name": "Boston University",
                "URL": "https://www.bu.edu",
            },
            {
                "color": "green",
                "name": "Google Research",
                "URL": "https://research.google",
            },
            {
                "color": "blue",
                "name": "University of Toronto",
                "URL": "https://www.utoronto.ca",
            },
            {
                "color": "uiBlue",
                "name": "The Hospital for Sick Children",
                "URL": "https://www.sickkids.ca",
            },
            {
                "color": "red",
                "name": "Philadelphia Phillies Baseball Operations Department",
                "URL": "https://boards.greenhouse.io/philadelphiaphilliesrddepartment",
            },
            {
                "color": "blue",
                "name": "PyMC Labs",
                "URL": "https://www.pymc-labs.com",
            },
            {
                "color": "red",
                "name": "Stony Brook University",
                "URL": "https://www.stonybrook.edu",
            },
            {
                "color": "purple",
                "name": "Universidad Nacional de San Luis",
                "URL": "https://www.unsl.edu.ar",
            },
            {
                "color": "blue",
                "name": "Forschungszentrum Jülich",
                "URL": "https://www.fz-juelich.de",
            },
            {
                "color": "blue",
                "name": "University of Oxford",
                "URL": "https://www.ox.ac.uk",
            },
            {
                "color": "orange",
                "name": "NumFOCUS",
                "URL": "https://numfocus.org",
            },
            {
                "color": "teal",
                "name": "Mistplay",
                "URL": "https://www.mistplay.com",
            },
            {
                "color": "default",
                "name": "ODSC",
                "URL": "https://odsc.com/california/?utm_source=pymc&utm_medium=referral",
            },
            {
                "color": "default",
                "name": "ADIA Lab",
                "URL": "https://www.adialab.ae",
            },
            {
                "color": "default",
                "name": "PyMC contributors",
                "URL": "https://github.com/pymc-devs/pymc/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://www.pymc.io/projects/docs/en/stable/learn.html",
            },
            {
                "tag": "examples",
                "URL": "https://www.pymc.io/projects/examples/en/latest/blog/tag/gaussian-process.html",
            },
            {
                "tag": "API",
                "URL": "https://www.pymc.io/projects/docs/en/stable/api/gp.html",
            },
        ],
        "Support": [
            {
                "tag": "forum",
                "URL": "https://discourse.pymc.io",
            },
            {
                "tag": "GitHub discussions",
                "URL": "https://github.com/pymc-devs/pymc/discussions",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "scikit-learn": {
        "URL": "https://scikit-learn.org/stable/#",
        "Language": ["Python"],
        "License": {
            "type": ["BSD3"],
            "URL": ["https://github.com/scikit-learn/scikit-learn/blob/main/COPYING"],
        },
        "Reference": {
            "Authors": "Pedregosa et al. (2011)",
            "URL": "https://jmlr.csail.mit.edu/papers/v12/pedregosa11a.html",
        },
        "Release": {
            "version": "v1.4.1",
            "URL": "https://github.com/scikit-learn/scikit-learn/releases/tag/1.4.1.post1",
        },
        "Developers": [
            {
                "color": "teal",
                "name": "Community driven",
                "URL": "https://scikit-learn.org/stable/about.html#people",
            },
            {
                "color": "green",
                "name": "NVIDIA",
                "URL": "https://www.nvidia.com",
            },
            {
                "color": "red",
                "name": "INRIA",
                "URL": "https://www.inria.fr/en",
            },
            {
                "color": "yellow",
                "name": "Hugging Face",
                "URL": "https://huggingface.co",
            },
            {
                "color": "orange",
                "name": "Microsoft",
                "URL": "https://www.microsoft.com",
            },
            {
                "color": "default",
                "name": "Quansight Labs",
                "URL": "https://www.quansight.com/labs",
            },
            {
                "color": "default",
                "name": "sci-kit-learn contributors",
                "URL": "https://github.com/scikit-learn/scikit-learn/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://scikit-learn.org/stable/modules/gaussian_process.html",
            },
            {
                "tag": "examples",
                "URL": "https://scikit-learn.org/stable/auto_examples/index.html#gaussian-process-for-machine-learning",
            },
            {
                "tag": "tutorials",
                "URL": "https://scikit-learn.org/stable/tutorial/index.html",
            },
            {
                "tag": "API",
                "URL": "https://scikit-learn.org/stable/modules/classes.html",
            },
        ],
        "Support": [
            {
                "tag": "blog",
                "URL": "https://blog.scikit-learn.org",
            },
            {
                "tag": "stackoverflow",
                "URL": "https://stackoverflow.com/questions/tagged/scikit-learn",
            },
            {
                "tag": "GitHub discussions",
                "URL": "https://github.com/scikit-learn/scikit-learn/discussions",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": ["Zero"],
            "URL": "https://scikit-learn.org/stable/modules/gaussian_process.html",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "SMT": {
        "URL": "https://smt.readthedocs.io/en/latest/index.html",
        "Language": ["Python"],
        "License": {
            "type": ["BSD3"],
            "URL": ["https://github.com/SMTorg/smt/blob/master/LICENSE.txt"],
        },
        "Reference": {
            "Authors": "Saves et al. (2024)",
            "URL": "https://www.sciencedirect.com/science/article/abs/pii/S096599782300162X?via%3Dihub",
        },
        "Release": {
            "version": "v2.3.0",
            "URL": "https://github.com/SMTorg/smt/releases/tag/v2.3.0",
        },
        "Developers": [
            {
                "color": "uiBlue",
                "name": "ISAE SUPEAERO",
                "URL": "https://www.isae-supaero.fr/en/",
            },
            {
                "color": "blue",
                "name": "NASA",
                "URL": "https://www.nasa.gov",
            },
            {
                "color": "uiBlue",
                "name": "ONERA",
                "URL": "https://www.onera.fr/en",
            },
            {
                "color": "blue",
                "name": "University of Michigan",
                "URL": "https://umich.edu",
            },
            {
                "color": "blue",
                "name": "University of San Diego",
                "URL": "https://www.sandiego.edu",
            },
            {
                "color": "red",
                "name": "Polytechnique Montréal",
                "URL": "https://www.polymtl.ca",
            },
            {
                "color": "default",
                "name": "SMT contributors",
                "URL": "https://github.com/SMTorg/smt/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://smt.readthedocs.io/en/stable/",
            },
            {
                "tag": "tutorials",
                "URL": "https://github.com/SMTorg/smt/tree/master/tutorial",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [
                "Constant",
                "Linear",
                "Quadratic",
            ],
            "URL": "https://smt.readthedocs.io/en/latest/_src_docs/surrogate_models/krg.html",
        },
        "Kernel": {
            "LengthScale": ["Isotropic", "Anisotropic"],
            "Families": {
                "tag": [
                    "Power Exponential",
                    "Absolute Exponetial",
                    "Squared Exponetial",
                    "Matern32",
                    "Matern52",
                ],
                "URL": "https://smt.readthedocs.io/en/latest/_src_docs/surrogate_models/krg.html",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "Stheno": {
        "URL": "https://wessel.ai/stheno/docs/_build/html/index.html",
        "Language": ["Julia", "Python"],
        "License": {
            "type": ["MIT"],
            "URL": ["https://github.com/JuliaGaussianProcesses/Stheno.jl/blob/master/LICENSE.md"],
        },
        "Reference": {
            "Authors": "Tebbutt et al. (2019)",
            "URL": "https://willtebbutt.github.io/resources/stheno_juliacon_2019.pdf",
        },
        "Release": {
            "version": "v0.8.2",
            "URL": "https://github.com/JuliaGaussianProcesses/Stheno.jl/releases/tag/v0.8.2",
        },
        "Developers": [
            {
                "color": "yellow",
                "name": "University of Cambridge",
                "URL": "https://www.cam.ac.uk",
            },
            {
                "color": "default",
                "name": "Stheno.jl contributors",
                "URL": "https://github.com/JuliaGaussianProcesses/Stheno.jl/graphs/contributors",
            },
            {
                "color": "default",
                "name": "Stheno py contributors",
                "URL": "https://github.com/wesselb/stheno/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "py docs",
                "URL": "https://wessel.ai/stheno/docs/_build/html/index.html",
            },
            {
                "tag": "jl docs",
                "URL": "https://juliagaussianprocesses.github.io/Stheno.jl/stable/",
            },
            {
                "tag": "py examples",
                "URL": "https://wessel.ai/stheno/docs/_build/html/readme.html#examples",
            },
            {
                "tag": "jl examples",
                "URL": "https://juliagaussianprocesses.github.io/Stheno.jl/stable/examples_note/",
            },
            {
                "tag": "py API",
                "URL": "https://wessel.ai/stheno/docs/_build/html/api.html",
            },
            {
                "tag": "jl API",
                "URL": "https://juliagaussianprocesses.github.io/Stheno.jl/stable/api/",
            },
            {
                "tag": "talk",
                "URL": "https://www.youtube.com/watch?v=OO3BBkGEMV8",
            },
        ],
        "Support": [
            {
                "tag": "GitHub discussions",
                "URL": "https://github.com/wesselb/stheno/discussions",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "UQLab": {
        "URL": "https://www.uqlab.com",
        "Language": ["Matlab"],
        "License": {
            "type": ["BSD3"],
            "URL": ["https://www.uqlab.com/copy-of-release-notes"],
        },
        "Reference": {
            "Authors": "Marelli et al. (2014)",
            "URL": "https://ascelibrary.org/doi/10.1061/9780784413609.257",
        },
        "Release": {
            "version": "v2.0.0",
            "URL": "https://www.uqlab.com/release-notes",
        },
        "Developers": [
            {
                "color": "default",
                "name": "RSUQ ETH Zürich",
                "URL": "https://sudret.ibk.ethz.ch/software/uqlab.html",
            },
            {
                "color": "default",
                "name": "UQLab contributors",
                "URL": "https://www.uqlab.com/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://www.uqlab.com/documentation",
            },
            {
                "tag": "user manuals",
                "URL": "https://www.uqlab.com/user-manuals",
            },
            {
                "tag": "examples",
                "URL": "https://www.uqlab.com/examples",
            },
        ],
        "Support": [
            {
                "tag": "contact form",
                "URL": "https://www.uqlab.com/contact",
            },
            {
                "tag": "forum",
                "URL": "https://uqworld.org/c/uq-with-uqlab/7",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [
                "Zero",
                "Constant",
                "Linear",
                "Quadratic",
                "Polynomial",
                "Custom",
            ],
            "URL": "https://uqftp.ethz.ch/uqlab_doc_html/2.0.0/UserManual_Kriging.html#pf39",
        },
        "Kernel": {
            "LengthScale": ["Isotropic", "Anisotropic"],
            "Families": {
                "tag": [
                    "Linear",
                    "Exponential",
                    "Gaussian",
                    "Matern32",
                    "Materm52",
                ],
                "URL": "https://uqftp.ethz.ch/uqlab_doc_html/2.0.0/UserManual_Kriging.html#pf25",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "UQ[py]Lab Beta": {
        "URL": "https://uqpylab.uq-cloud.io",
        "Language": ["Python"],
        "License": {
            "type": ["BSD3"],
            "URL": ["https://www.uqlab.com/copy-of-release-notes"],
        },
        "Reference": {
            "Authors": "Lataniotis et al. (2021)",
            "URL": "https://www.eccomasproceedia.org/conferences/thematic-conferences/uncecomp-2021/8033",
        },
        "Release": {
            "version": "v0.95",
            "URL": "https://uqpylab.uq-cloud.io/#beta-testing-application",
        },
        "Developers": [
            {
                "color": "default",
                "name": "RSUQ ETH Zürich",
                "URL": "https://sudret.ibk.ethz.ch/software/uqpylab.html",
            },
            {
                "color": "default",
                "name": "UQ[py]Lab contributors",
                "URL": "https://uqpylab.uq-cloud.io/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://uqpylab.uq-cloud.io/getting-started",
            },
            {
                "tag": "user manuals",
                "URL": "https://uqpylab.uq-cloud.io/documentation",
            },
            {
                "tag": "examples",
                "URL": "https://uqpylab.uq-cloud.io/examples",
            },
        ],
        "Support": [
            {
                "tag": "contact form",
                "URL": "https://www.uqlab.com/contact",
            },
            {
                "tag": "forum",
                "URL": "https://uqworld.org/c/uq-with-uqlab/7",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [
                "Zero",
                "Constant",
                "Linear",
                "Quadratic",
                "Polynomial",
                "Custom",
            ],
            "URL": "https://storage.googleapis.com/uqpylab-doc-html/UserManual_Kriging.html#[58,%22XYZ%22,71.434,547.221,null]",
        },
        "Kernel": {
            "LengthScale": ["Isotropic", "Anisotropic"],
            "Families": {
                "tag": [
                    "Linear",
                    "Exponential",
                    "Gaussian",
                    "Matern32",
                    "Materm52",
                ],
                "URL": "https://storage.googleapis.com/uqpylab-doc-html/UserManual_Kriging.html#[59,%22XYZ%22,85.039,437.866,null]",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "STAN": {
        "URL": "https://mc-stan.org",
        "Language": ["R", "Cpp", "Julia", "Python", "Matlab"],
        "License": {
            "type": ["BSD3", "GPL3", "MIT"],
            "URL": [
                "https://github.com/brian-lau/MatlabStan/blob/master/LICENSE.txt",
                "https://github.com/stan-dev/rstan/blob/develop/licenses/rstan-license.txt",
                "https://github.com/StanJulia/Stan.jl/blob/master/LICENSE.md",
            ],
        },
        "Reference": {
            "Authors": "Stan Development Team (2017)",
            "URL": "https://zenodo.org/records/1101116",
        },
        "Release": {
            "version": "v2.15.1",
            "URL": "https://zenodo.org/records/1101116",
        },
        "Developers": [
            {
                "color": "default",
                "name": "Stan Development Team",
                "URL": "https://github.com/orgs/stan-dev/people",
            },
            {
                "color": "orange",
                "name": "NumFOCUS",
                "URL": "https://numfocus.org",
            },
            {
                "color": "default",
                "name": "Stan contributors",
                "URL": "https://github.com/stan-dev/stan/graphs/contributors",
            },
            {
                "color": "default",
                "name": "MatlabStan contributors",
                "URL": "https://github.com/brian-lau/MatlabStan/graphs/contributors",
            },
            {
                "color": "default",
                "name": "RStan contributors",
                "URL": "https://github.com/stan-dev/rstan/graphs/contributors",
            },
            {
                "color": "default",
                "name": "pyStan contributors",
                "URL": "https://github.com/stan-dev/pystan/graphs/contributors",
            },
            {
                "color": "default",
                "name": "Stan.jl contributors",
                "URL": "https://github.com/StanJulia/Stan.jl/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://mc-stan.org/docs/stan-users-guide/gaussian-processes.html",
            },
            {
                "tag": "r docs",
                "URL": "https://cran.r-project.org/web/packages/rstan/rstan.pdf",
            },
            {
                "tag": "mat docs",
                "URL": "https://github.com/brian-lau/MatlabStan/wiki",
            },
            {
                "tag": "py docs",
                "URL": "https://pystan.readthedocs.io/en/latest/",
            },
            {
                "tag": "jl docs",
                "URL": "https://github.com/StanJulia/Stan.jl/tree/master/docs",
            },
        ],
        "Support": [
            {
                "tag": "forum",
                "URL": "https://discourse.mc-stan.org",
            },
            {
                "tag": "slack",
                "URL": "https://mc-stan.slack.com/join/shared_invite/zt-1le4ebi4m-UMtiOkJb4gcS16qz2wIYCw#/shared-invite/email",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "pyGPs": {
        "URL": "https://github.com/marionmari/pyGPs",
        "Language": ["Python"],
        "License": {
            "type": ["FreeBSD"],
            "URL": ["https://github.com/marionmari/pyGPs/blob/master/COPYRIGHT.txt"],
        },
        "Reference": {
            "Authors": "Neumann et al. (2015)",
            "URL": "https://jmlr.org/papers/v16/neumann15a.html",
        },
        "Release": {
            "version": "v1.3.5",
            "URL": "https://github.com/marionmari/pyGPs/releases/tag/v1.3.5",
        },
        "Developers": [
            {
                "color": "red",
                "name": "Washington University",
                "URL": "https://wustl.edu",
            },
            {
                "color": "teal",
                "name": "Fraunhofer IAIS",
                "URL": "https://www.iais.fraunhofer.de/en.html",
            },
            {
                "color": "green",
                "name": "TU Dortmund",
                "URL": "https://www.tu-dortmund.de/en/",
            },
            {
                "color": "yellow",
                "name": "Sproutling",
                "URL": "https://www.crunchbase.com/organization/sproutling",
            },
            {
                "color": "default",
                "name": "pyGPs contributors",
                "URL": "https://github.com/marionmari/pyGPs/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://www.cse.wustl.edu/~m.neumann/pyGPs_doc/",
            },
            {
                "tag": "examples",
                "URL": "https://www.cse.wustl.edu/~m.neumann/pyGPs_doc/Examples.html",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "celerite": {
        "URL": "https://celerite.readthedocs.io/en/stable/",
        "Language": ["Cpp", "Julia", "Python"],
        "License": {
            "type": ["MIT"],
            "URL": ["https://github.com/dfm/celerite/blob/main/LICENSE"],
        },
        "Reference": {
            "Authors": "Foreman-Mackey et al. (2017)",
            "URL": "https://iopscience.iop.org/article/10.3847/1538-3881/aa9332",
        },
        "Release": {
            "version": "v0.4.2",
            "URL": "https://github.com/dfm/celerite/releases/tag/v0.4.2",
        },
        "Developers": [
            {
                "color": "purple",
                "name": "University of Washington",
                "URL": "https://www.washington.edu",
            },
            {
                "color": "uiBlue",
                "name": "Flatiron Institute",
                "URL": "https://www.simonsfoundation.org/flatiron/",
            },
            {
                "color": "teal",
                "name": "Indian Institute of Science",
                "URL": "https://www.iisc.ac.in",
            },
            {
                "color": "blue",
                "name": "Columbia University",
                "URL": "https://www.columbia.edu",
            },
            {
                "color": "default",
                "name": "celertie contributors",
                "URL": "https://github.com/dfm/celerite/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://celerite.readthedocs.io/en/stable/",
            },
            {
                "tag": "API",
                "URL": "https://celerite.readthedocs.io/en/stable/cpp/api/",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "celerite2": {
        "URL": "https://celerite2.readthedocs.io/en/latest/tutorials/first/",
        "Language": ["Cpp", "Python"],
        "License": {
            "type": ["MIT"],
            "URL": ["https://github.com/exoplanet-dev/celerite2/blob/main/LICENSE"],
        },
        "Reference": {
            "Authors": "Gordon et al. (2020)",
            "URL": "https://iopscience.iop.org/article/10.3847/1538-3881/abbc16",
        },
        "Release": {
            "version": "v0.3.0",
            "URL": "https://github.com/exoplanet-dev/celerite2/releases/tag/v0.3.0",
        },
        "Developers": [
            {
                "color": "purple",
                "name": "University of Washington",
                "URL": "https://www.washington.edu",
            },
            {
                "color": "uiBlue",
                "name": "Flatiron Institute",
                "URL": "https://www.simonsfoundation.org/flatiron/",
            },
            {
                "color": "default",
                "name": "celertie2 contributors",
                "URL": "https://github.com/exoplanet-dev/celerite2/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://celerite2.readthedocs.io/en/latest/",
            },
            {
                "tag": "tutorials",
                "URL": "https://celerite2.readthedocs.io/en/latest/tutorials/first/",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "george": {
        "URL": "https://george.readthedocs.io/en/latest/",
        "Language": ["Python"],
        "License": {
            "type": ["MIT"],
            "URL": ["https://github.com/dfm/george/blob/main/LICENSE"],
        },
        "Reference": {
            "Authors": "Ambikasaran et al. (2015)",
            "URL": "https://ieeexplore.ieee.org/document/7130620",
        },
        "Release": {
            "version": "v0.4.1",
            "URL": "https://github.com/dfm/george/releases/tag/v0.4.1",
        },
        "Developers": [
            {
                "color": "purple",
                "name": "New York University",
                "URL": "https://www.nyu.edu",
            },
            {
                "color": "blue",
                "name": "Simons Foundation",
                "URL": "https://www.simonsfoundation.org/",
            },
            {
                "color": "default",
                "name": "george contributors",
                "URL": "https://github.com/dfm/george/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://george.readthedocs.io/en/latest/user/",
            },
            {
                "tag": "tutorials",
                "URL": "https://george.readthedocs.io/en/latest/tutorials/",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "Neural Tangents": {
        "URL": "https://iclr.cc/virtual_2020/poster_SklD9yrFPS.html",
        "Language": ["Python"],
        "License": {
            "type": ["Apache2"],
            "URL": ["https://github.com/google/neural-tangents/blob/main/LICENSE"],
        },
        "Reference": {
            "Authors": "Novak et al. (2020)",
            "URL": "https://openreview.net/pdf?id=SklD9yrFPS",
        },
        "Release": {
            "version": "v0.6.5",
            "URL": "https://github.com/google/neural-tangents/releases/tag/v0.6.5",
        },
        "Developers": [
            {
                "color": "green",
                "name": "Google Brain",
                "URL": "https://research.google/teams/brain/",
            },
            {
                "color": "yellow",
                "name": "University of Cambridge",
                "URL": "https://www.cam.ac.uk",
            },
            {
                "color": "default",
                "name": "Neural Tangents contributors",
                "URL": "https://github.com/google/neural-tangents/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://neural-tangents.readthedocs.io/en/latest/#",
            },
            {
                "tag": "colab cookbook",
                "URL": "https://colab.research.google.com/github/google/neural-tangents/blob/main/notebooks/neural_tangents_cookbook.ipynb",
            },
            {
                "tag": "talk",
                "URL": "https://iclr.cc/virtual_2020/poster_SklD9yrFPS.html",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "DACE": {
        "URL": "https://www.omicron.dk/dace.html",
        "Language": ["Matlab"],
        "License": {
            "type": ["NA"],
            "URL": [""],
        },
        "Reference": {
            "Authors": "Nielsen et al. (2002)",
            "URL": "https://www.semanticscholar.org/paper/DACE-A-Matlab-Kriging-Toolbox-Nielsen-Lophaven/d11a9e296ccd522809cb7550740e89f2c7ee65af#paper-topics",
        },
        "Release": {
            "version": "v2.5",
            "URL": "https://www.omicron.dk/dace/changelog.txt",
        },
        "Developers": [
            {
                "color": "red",
                "name": "Techincal University of Denmark (DTU)",
                "URL": "https://www.dtu.dk",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://www.omicron.dk/dace/dace.pdf",
            },
            {
                "tag": "user manuals",
                "URL": "https://www.omicron.dk/dace/dace-aspects.pdf",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "GpGp": {
        "URL": "https://cran.r-project.org/package=GpGp",
        "Language": ["R"],
        "License": {
            "type": ["MIT"],
            "URL": ["https://cran.r-project.org/web/licenses/MIT"],
        },
        "Reference": {
            "Authors": "Guinness et al. (2018)",
            "URL": "https://www.tandfonline.com/doi/full/10.1080/00401706.2018.1437476",
        },
        "Release": {
            "version": "v0.5.0",
            "URL": "https://cran.r-project.org/src/contrib/GpGp_0.5.0.tar.gz",
        },
        "Developers": [
            {
                "color": "red",
                "name": "Cornell University",
                "URL": "https://www.cornell.edu",
            },
            {
                "color": "default",
                "name": "GpGp contributors",
                "URL": "https://github.com/joeguinness/GpGp/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://cran.r-project.org/web/packages/GpGp/GpGp.pdf",
            },
            {
                "tag": "tutorials",
                "URL": "https://www.youtube.com/watch?v=phyB4n0CDWg&t=4s",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "SuperGauss": {
        "URL": "https://cran.r-project.org/package=SuperGauss",
        "Language": ["R"],
        "License": {
            "type": ["GPL3"],
            "URL": ["https://cran.r-project.org/web/licenses/GPL-3"],
        },
        "Reference": {
            "Authors": "Ling et al. (2020)",
            "URL": "https://github.com/mlysy/SuperGauss/blob/master/doc/SuperGauss_preprint.pdf",
        },
        "Release": {
            "version": "v2.0.3",
            "URL": "https://cran.r-project.org/src/contrib/SuperGauss_2.0.3.tar.gz",
        },
        "Developers": [
            {
                "color": "yellow",
                "name": "University of Waterloo",
                "URL": "https://uwaterloo.ca",
            },
            {
                "color": "default",
                "name": "SuperGauss contributors",
                "URL": "https://github.com/mlysy/SuperGauss/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://cran.r-project.org/web/packages/SuperGauss/SuperGauss.pdf",
            },
            {
                "tag": "tutorials",
                "URL": "https://cran.r-project.org/web/packages/SuperGauss/vignettes/SuperGauss-quicktut.html",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "STK": {
        "URL": "https://github.com/stk-kriging/stk",
        "Language": ["Matlab", "Octave"],
        "License": {
            "type": ["GPL3"],
            "URL": ["https://github.com/stk-kriging/stk/blob/master/COPYING"],
        },
        "Reference": {
            "Authors": "Bect et al. (2023)",
            "URL": "https://github.com/stk-kriging/stk/",
        },
        "Release": {
            "version": "v2.8.1",
            "URL": "https://github.com/stk-kriging/stk/releases/tag/2.8.1",
        },
        "Developers": [
            {
                "color": "red",
                "name": "CentraleSupélec",
                "URL": "https://www.centralesupelec.fr",
            },
            {
                "color": "default",
                "name": "STK contributors",
                "URL": "https://github.com/stk-kriging/stk/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://stk-kriging.github.io/release/latest/doc/html/index.html",
            },
            {
                "tag": "examples",
                "URL": "https://github.com/stk-kriging/stk/tree/master/examples",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "GSTools": {
        "URL": "https://geostat-framework.org",
        "Language": ["Python"],
        "License": {
            "type": ["LGPL"],
            "URL": ["https://github.com/GeoStat-Framework/GSTools/blob/main/LICENSE"],
        },
        "Reference": {
            "Authors": "Müller et al. (2022)",
            "URL": "https://gmd.copernicus.org/articles/15/3161/2022/",
        },
        "Release": {
            "version": "v1.5.1",
            "URL": "https://github.com/GeoStat-Framework/GSTools/releases/tag/v1.5.1",
        },
        "Developers": [
            {
                "color": "blue",
                "name": "UFZ",
                "URL": "https://www.ufz.de",
            },
            {
                "color": "teal",
                "name": "University of Potsdam",
                "URL": "https://www.uni-potsdam.de/en/",
            },
            {
                "color": "blue",
                "name": "CASUS",
                "URL": "https://www.casus.science",
            },
            {
                "color": "yellow",
                "name": " Utrecht University",
                "URL": "https://www.uu.nl/en",
            },
            {
                "color": "default",
                "name": "GSTools contributors",
                "URL": "https://github.com/GeoStat-Framework/GSTools/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://geostat-framework.readthedocs.io/projects/gstools/en/stable/",
            },
            {
                "tag": "tutorials",
                "URL": "https://geostat-framework.readthedocs.io/projects/gstools/en/stable/tutorials.html",
            },
            {
                "tag": "API",
                "URL": "https://geostat-framework.readthedocs.io/projects/gstools/en/stable/api.html",
            },
        ],
        "Support": [
            {
                "tag": "GitHub discussions",
                "URL": "https://github.com/GeoStat-Framework/GSTools/discussions",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "PyKrige": {
        "URL": "https://geostat-framework.readthedocs.io/projects/pykrige/en/stable/",
        "Language": ["Python"],
        "License": {
            "type": ["BSD3"],
            "URL": ["https://github.com/GeoStat-Framework/PyKrige/blob/main/LICENSE"],
        },
        "Reference": {
            "Authors": "Müller et al. (2022)",
            "URL": "https://gmd.copernicus.org/articles/15/3161/2022/",
        },
        "Release": {
            "version": "v1.7.1",
            "URL": "https://github.com/GeoStat-Framework/PyKrige/releases/tag/v1.7.1",
        },
        "Developers": [
            {
                "color": "blue",
                "name": "UFZ",
                "URL": "https://www.ufz.de",
            },
            {
                "color": "teal",
                "name": "University of Potsdam",
                "URL": "https://www.uni-potsdam.de/en/",
            },
            {
                "color": "blue",
                "name": "CASUS",
                "URL": "https://www.casus.science",
            },
            {
                "color": "yellow",
                "name": " Utrecht University",
                "URL": "https://www.uu.nl/en",
            },
            {
                "color": "default",
                "name": "PyKrige contributors",
                "URL": "https://github.com/GeoStat-Framework/PyKrige/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://buildmedia.readthedocs.org/media/pdf/pykrige/latest/pykrige.pdf",
            },
            {
                "tag": "examples",
                "URL": "https://geostat-framework.readthedocs.io/projects/pykrige/en/stable/examples/index.html",
            },
            {
                "tag": "API",
                "URL": "https://geostat-framework.readthedocs.io/projects/pykrige/en/stable/api.html",
            },
        ],
        "Support": [
            {
                "tag": "GitHub discussions",
                "URL": "https://github.com/GeoStat-Framework/PyKrige/discussions",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "GPJax": {
        "URL": "https://docs.jaxgaussianprocesses.com",
        "Language": ["Python"],
        "License": {
            "type": ["Apache2"],
            "URL": ["https://github.com/JaxGaussianProcesses/GPJax/blob/main/LICENSE"],
        },
        "Reference": {
            "Authors": "Pinder et al. (2022)",
            "URL": "https://joss.theoj.org/papers/10.21105/joss.04455#",
        },
        "Release": {
            "version": "v0.8.0",
            "URL": "https://github.com/JaxGaussianProcesses/GPJax/releases/tag/v0.8.0",
        },
        "Developers": [
            {
                "color": "red",
                "name": "Lancaster University",
                "URL": "https://www.lancaster.ac.uk",
            },
            {
                "color": "default",
                "name": "GPJax contributors",
                "URL": "https://github.com/JaxGaussianProcesses/GPJax/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://docs.jaxgaussianprocesses.com",
            },
            {
                "tag": "tutorials",
                "URL": "https://docs.jaxgaussianprocesses.com/examples/regression/",
            },
        ],
        "Support": [
            {
                "tag": "GitHub discussions",
                "URL": "https://github.com/orgs/JaxGaussianProcesses/discussions",
            },
        ],
        "Framework": [
            {
                "tag": "JAX",
                "URL": "https://jax.readthedocs.io/en/latest/#",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "UQpy": {
        "URL": "https://sites.google.com/site/jhusurg/UQpy",
        "Language": ["Python"],
        "License": {
            "type": ["MIT"],
            "URL": ["https://github.com/SURGroup/UQpy/blob/master/LICENSE"],
        },
        "Reference": {
            "Authors": "Olivier et al. (2020)",
            "URL": "https://www.sciencedirect.com/science/article/abs/pii/S1877750320305056",
        },
        "Release": {
            "version": "v4.1.5",
            "URL": "https://github.com/SURGroup/UQpy/releases/tag/v4.1.5",
        },
        "Developers": [
            {
                "color": "blue",
                "name": "Johns Hopkins University",
                "URL": "https://sites.google.com/site/jhusurg/home?authuser=0",
            },
            {
                "color": "default",
                "name": "UQpy contributors",
                "URL": "https://github.com/SURGroup/UQpy/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://uqpyproject.readthedocs.io/en/latest/",
            },
        ],
        "Support": [
            {
                "tag": "GitHub discussions",
                "URL": "https://github.com/SURGroup/UQpy/discussions",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "MUQ": {
        "URL": "https://mituq.bitbucket.io/source/_site/",
        "Language": ["Cpp", "Python"],
        "License": {
            "type": ["BSD3"],
            "URL": ["https://bitbucket.org/mituq/muq2/src/master/LICENSE"],
        },
        "Reference": {
            "Authors": "Parno et al. (2021)",
            "URL": "https://doi.org/10.21105/joss.03076",
        },
        "Release": {
            "version": "v0.4.3",
            "URL": "https://mituq.bitbucket.io/source/_site/latest/index.html",
        },
        "Developers": [
            {
                "color": "red",
                "name": "Massachusetts Institute of Technology",
                "URL": "https://www.mit.edu",
            },
            {
                "color": "green",
                "name": "Dartmouth College",
                "URL": "https://math.dartmouth.edu",
            },
            {
                "color": "purple",
                "name": "New York University",
                "URL": "https://www.nyu.edu",
            },
            {
                "color": "re",
                "name": "Heidelberg University",
                "URL": "https://www.uni-heidelberg.de",
            },
            {
                "color": "blue",
                "name": "National Science Foundation",
                "URL": "https://www.nsf.gov",
            },
            {
                "color": "green",
                "name": "US Department of Energy",
                "URL": "https://www.energy.gov",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://mituq.bitbucket.io/source/_site/latest/index.html",
            },
            {
                "tag": "examples",
                "URL": "https://mituq.bitbucket.io/source/_site/examples.html",
            },
            {
                "tag": "py examples",
                "URL": "https://bitbucket.org/mituq/muq2-examples/src/master/",
            },
        ],
        "Support": [
            {
                "tag": "slack",
                "URL": "https://mituq.bitbucket.io/source/_site/index.html",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "tinygp": {
        "URL": "https://tinygp.readthedocs.io/en/stable/",
        "Language": ["Python"],
        "License": {
            "type": ["MIT"],
            "URL": ["https://github.com/dfm/tinygp/blob/main/LICENSE"],
        },
        "Reference": {
            "Authors": "Foreman-Mackey et al. (2024)",
            "URL": "https://zenodo.org/records/10463641",
        },
        "Release": {
            "version": "v0.3.0",
            "URL": "https://github.com/dfm/tinygp/releases/tag/v0.3.0",
        },
        "Developers": [
            {
                "color": "blue",
                "name": "Simons Foundation",
                "URL": "https://www.simonsfoundation.org",
            },
            {
                "color": "default",
                "name": "tinygp contributors",
                "URL": "https://github.com/dfm/tinygp/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://tinygp.readthedocs.io/en/stable/guide.html",
            },
            {
                "tag": "tutorials",
                "URL": "https://tinygp.readthedocs.io/en/stable/tutorials.html",
            },
            {
                "tag": "API",
                "URL": "https://tinygp.readthedocs.io/en/stable/api/index.html",
            },
        ],
        "Support": [
            {
                "tag": "GitHub discussions",
                "URL": "https://github.com/dfm/tinygp/discussions",
            },
        ],
        "Framework": [
            {
                "tag": "JAX",
                "URL": "https://jax.readthedocs.io/en/latest/#",
            },
        ],
        "GPU": True,
        "Trend": {
            "tag": ["Custom"],
            "URL": "https://tinygp.readthedocs.io/en/stable/api/summary/tinygp.means.Mean.html",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [
                    "Conditioned",
                    "Custom",
                    # "Sum",
                    # "Product",
                    "Constant",
                    # "DotProduct",
                    "Polynomial",
                    "Exponetial",
                    "RBF",
                    "Matern32",
                    "Matern52",
                    "Cosine",
                    "Exponential Sine Squared",
                    "Rational Quadratic",
                ],
                "URL": "https://tinygp.readthedocs.io/en/stable/api/kernels.html",
            },
            "Mixture": {
                "check": True,
                "tag": [
                    "Sum",
                    "Product",
                    "DotProduct",
                ],
                "URL": "https://tinygp.readthedocs.io/en/stable/api/kernels.html",
            },
        },
    },
    # ===============================================
    "PYRO": {
        "URL": "https://pyro.ai",
        "Language": ["Python"],
        "License": {
            "type": ["Apache2"],
            "URL": ["https://github.com/pyro-ppl/pyro/blob/dev/LICENSE.md"],
        },
        "Reference": {
            "Authors": "Bingham et al. (2019)",
            "URL": "http://jmlr.org/papers/v20/18-403.html",
        },
        "Release": {
            "version": "v1.9.0",
            "URL": "https://github.com/pyro-ppl/pyro/releases/tag/1.9.0",
        },
        "Developers": [
            {
                "color": "default",
                "name": "Uber AI",
                "URL": "https://eng.uber.com/uber-ai/",
            },
            {
                "color": "red",
                "name": "Stanford University",
                "URL": "https://www.stanford.edu",
            },
            {
                "color": "blue",
                "name": "Broad Institute",
                "URL": "https://www.broadinstitute.org",
            },
            {
                "color": "default",
                "name": "Linux Foundation",
                "URL": "https://www.linuxfoundation.org",
            },
            {
                "color": "default",
                "name": "PYRO contributors",
                "URL": "https://github.com/pyro-ppl/pyro/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://pyro.ai/examples/gp.html",
            },
            {
                "tag": "examples",
                "URL": "https://pyro.ai/examples/",
            },
        ],
        "Support": [
            {
                "tag": "forum",
                "URL": "http://forum.pyro.ai/",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "AbstractGPs.jl": {
        "URL": "https://juliagaussianprocesses.github.io/AbstractGPs.jl/dev/",
        "Language": ["Julia"],
        "License": {
            "type": ["MIT"],
            "URL": ["https://github.com/JuliaGaussianProcesses/AbstractGPs.jl/blob/master/LICENSE"],
        },
        "Reference": {
            "Authors": "n/a",
            "URL": "",
        },
        "Release": {
            "version": "v0.5.19",
            "URL": "https://github.com/JuliaGaussianProcesses/AbstractGPs.jl/releases/tag/v0.5.19",
        },
        "Developers": [
            {
                "color": "default",
                "name": "AbstractGPs.jl contributors",
                "URL": "https://github.com/JuliaGaussianProcesses/AbstractGPs.jl/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://juliagaussianprocesses.github.io/AbstractGPs.jl/dev/api/",
            },
            {
                "tag": "examples",
                "URL": "https://juliagaussianprocesses.github.io/AbstractGPs.jl/dev/concrete_features/",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "GaussianProcesses.jl": {
        "URL": "https://stor-i.github.io/GaussianProcesses.jl/latest/",
        "Language": ["Julia"],
        "License": {
            "type": ["MIT"],
            "URL": ["https://github.com/STOR-i/GaussianProcesses.jl/blob/master/LICENSE.md"],
        },
        "Reference": {
            "Authors": "Fairbrother et al. (2022)",
            "URL": "https://www.jstatsoft.org/article/view/v102i01",
        },
        "Release": {
            "version": "v0.12.5",
            "URL": "https://github.com/STOR-i/GaussianProcesses.jl/releases/tag/v0.12.5",
        },
        "Developers": [
            {
                "color": "red",
                "name": "Lancaster University",
                "URL": "https://www.lancaster.ac.uk/stor-i/",
            },
            {
                "color": "red",
                "name": "EPFL",
                "URL": "https://www.epfl.ch/en/",
            },
            {
                "color": "default",
                "name": "GaussianProcesses.jl contributors",
                "URL": "https://github.com/STOR-i/GaussianProcesses.jl/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://stor-i.github.io/GaussianProcesses.jl/latest/",
            },
            {
                "tag": "tutorials",
                "URL": "https://stor-i.github.io/GaussianProcesses.jl/latest/classification_example/",
            },
            {
                "tag": "jupyter notebooks",
                "URL": "https://github.com/STOR-i/GaussianProcesses.jl/tree/master/notebooks",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "Surrogates.jl": {
        "URL": "https://docs.sciml.ai/Surrogates/stable/",
        "Language": ["Julia"],
        "License": {
            "type": ["MIT"],
            "URL": ["https://github.com/SciML/Surrogates.jl/blob/master/LICENSE.md"],
        },
        "Reference": {
            "Authors": "n/a",
            "URL": "",
        },
        "Release": {
            "version": "v6.9.0",
            "URL": "https://github.com/SciML/Surrogates.jl/releases",
        },
        "Developers": [
            {
                "color": "red",
                "name": "Chan Zuckerberg Initiative",
                "URL": "https://chanzuckerberg.com",
            },
            {
                "color": "default",
                "name": "Wellcome Trust",
                "URL": "https://wellcome.org",
            },
            {
                "color": "orange",
                "name": "Microsoft",
                "URL": "https://www.microsoft.com/en-us/research/collaboration/studies-in-pandemic-preparedness/overview/",
            },
            {
                "color": "default",
                "name": "Surrogates.jl contributors",
                "URL": "https://github.com/SciML/Surrogates.jl/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://docs.sciml.ai/Surrogates/stable/kriging/",
            },
        ],
        "Support": [
            {
                "tag": "chat",
                "URL": "https://julialang.zulipchat.com/#narrow/stream/279055-sciml-bridged",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "AutoGP.jl": {
        "URL": "https://probsys.github.io/AutoGP.jl/stable/",
        "Language": ["Julia"],
        "License": {
            "type": ["Apache2"],
            "URL": ["https://github.com/probsys/AutoGP.jl/blob/main/LICENSE.txt"],
        },
        "Reference": {
            "Authors": "Saad et al. (2023)",
            "URL": "https://arxiv.org/abs/2307.09607",
        },
        "Release": {
            "version": "n/a",
            "URL": "",
        },
        "Developers": [
            {
                "color": "red",
                "name": "Carnegie Mellon University",
                "URL": "https://www.cmu.edu/",
            },
            {
                "color": "green",
                "name": "Google Research",
                "URL": "https://research.google/",
            },
            {
                "color": "purple",
                "name": "Massachusetts Institute of Technology",
                "URL": "https://www.mit.edu/",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://probsys.github.io/AutoGP.jl/stable/gp.html",
            },
            {
                "tag": "tutorials",
                "URL": "https://probsys.github.io/AutoGP.jl/stable/tutorials/overview.html",
            },
            {
                "tag": "API",
                "URL": "https://probsys.github.io/AutoGP.jl/stable/api.html",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "AutoGP": {
        "URL": "https://arxiv.org/abs/1610.05392",
        "Language": ["Python"],
        "License": {
            "type": ["Apache2"],
            "URL": ["https://github.com/ebonilla/AutoGP/blob/master/LICENSE"],
        },
        "Reference": {
            "Authors": "Krauth et al. (2017)",
            "URL": "https://arxiv.org/abs/1610.05392",
        },
        "Release": {
            "version": "n/a",
            "URL": "",
        },
        "Developers": [
            {
                "color": "yellow",
                "name": "The University of New South Wales",
                "URL": "https://www.unsw.edu.au/",
            },
            {
                "color": "blue",
                "name": "EURECOM",
                "URL": "https://www.eurecom.fr/",
            },
            {
                "color": "default",
                "name": "AutoGP contributors",
                "URL": "https://github.com/ebonilla/AutoGP/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "albatross": {
        "URL": "https://swiftnav-albatross.readthedocs.io/en/latest/",
        "Language": ["Cpp"],
        "License": {
            "type": ["MIT"],
            "URL": ["https://github.com/swift-nav/albatross/blob/master/LICENSE"],
        },
        "Reference": {
            "Authors": "n/a",
            "URL": "",
        },
        "Release": {
            "version": "n/a",
            "URL": "",
        },
        "Developers": [
            {
                "color": "orange",
                "name": "Swift Navigation",
                "URL": "https://www.swiftnav.com",
            },
            {
                "color": "default",
                "name": "albatross contributors",
                "URL": "https://github.com/swift-nav/albatross/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://swiftnav-albatross.readthedocs.io/en/latest/",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "libgp": {
        "URL": "https://github.com/mblum/libgp",
        "Language": ["Cpp"],
        "License": {
            "type": ["BSD3"],
            "URL": ["https://github.com/mblum/libgp/blob/master/COPYING"],
        },
        "Reference": {
            "Authors": "",
            "URL": "",
        },
        "Release": {
            "version": "v0.1.4",
            "URL": "https://github.com/mblum/libgp/blob/master/README.md#release-notes",
        },
        "Developers": [
            {
                "color": "blue",
                "name": "",
                "URL": "",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://github.com/mblum/libgp/tree/master/doxygen",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "magptk": {
        "URL": "https://games-uchile.github.io/mogptk/",
        "Language": ["Python"],
        "License": {
            "type": ["MIT"],
            "URL": ["https://github.com/GAMES-UChile/mogptk/blob/master/LICENSE"],
        },
        "Reference": {
            "Authors": "de Wolff et al. (2020)",
            "URL": "https://www.sciencedirect.com/science/article/abs/pii/S0925231220317410?via%3Dihub",
        },
        "Release": {
            "version": "v0.5.1",
            "URL": "https://github.com/GAMES-UChile/mogptk/releases/tag/v0.5.1",
        },
        "Developers": [
            {
                "color": "purple",
                "name": "GAMES Universidad de Chile",
                "URL": "http://games.cmm.uchile.cl",
            },
            {
                "color": "default",
                "name": "mogptk contributors",
                "URL": "https://github.com/GAMES-UChile/mogptk/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://games-uchile.github.io/mogptk/",
            },
            {
                "tag": "tutorials",
                "URL": "https://games-uchile.github.io/mogptk/examples.html?q=00_Quick_Start",
            },
            {
                "tag": "examples",
                "URL": "https://games-uchile.github.io/mogptk/examples.html?q=example_airline_passengers",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "deepgp": {
        "URL": "https://cran.r-project.org/package=deepgp",
        "Language": ["R"],
        "License": {
            "type": ["LGPL"],
            "URL": ["https://cran.r-project.org/web/licenses/LGPL-3"],
        },
        "Reference": {
            "Authors": "Sauer et al. (2023)",
            "URL": "https://vtechworks.lib.vt.edu/items/9f21c4d1-2dfc-4750-9501-7e8e622b2427",
        },
        "Release": {
            "version": "v1.1.1",
            "URL": "https://cran.r-project.org/src/contrib/deepgp_1.1.1.tar.gz",
        },
        "Developers": [
            {
                "color": "red",
                "name": "Virginia Polytechnic Institute and State University",
                "URL": "https://www.vt.edu/",
            },
        ],
        "Docs": [
            {
                "tag": "docs",
                "URL": "https://cran.r-project.org/web/packages/deepgp/deepgp.pdf",
            },
            {
                "tag": "tutorials",
                "URL": "https://cran.r-project.org/web/packages/deepgp/vignettes/deepgp.html",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "Keras-GP": {
        "URL": "https://github.com/alshedivat/keras-gp",
        "Language": ["Python"],
        "License": {
            "type": ["MIT"],
            "URL": ["https://github.com/alshedivat/keras-gp/blob/master/LICENSE"],
        },
        "Reference": {
            "Authors": "Al-Shedivat et al. (2017)",
            "URL": "https://jmlr.org/papers/v18/16-498.html",
        },
        "Release": {
            "version": "v0.3.2",
            "URL": "https://github.com/alshedivat/keras-gp/releases/tag/0.3.2",
        },
        "Developers": [
            {
                "color": "red",
                "name": "Carnegie Mellon University",
                "URL": "https://www.cmu.edu/",
            },
            {
                "color": "red",
                "name": "Cornell University",
                "URL": "https://www.cornell.edu/",
            },
            {
                "color": "default",
                "name": "Keras-GP contributors",
                "URL": "https://github.com/alshedivat/keras-gp/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "examples",
                "URL": "https://github.com/alshedivat/keras-gp/tree/master/examples",
            },
            {
                "tag": "tutorials",
                "URL": "https://github.com/alshedivat/keras-gp/tree/master/tutorials",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "gaussianproc": {
        "URL": "",
        "Language": ["GO"],
        "License": {
            "type": ["NA"],
            "URL": [""],
        },
        "Reference": {
            "Authors": " et al. ()",
            "URL": "",
        },
        "Release": {
            "version": "v0",
            "URL": "https://pkg.go.dev/github.com/RobinRCM/sklearn/gaussian_process?tab=versions",
        },
        "Developers": [
            {
                "color": "blue",
                "name": "",
                "URL": "",
            },
        ],
        "Docs": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "friedrich": {
        "URL": "https://github.com/nestordemeure/friedrich?tab=readme-ov-file",
        "Language": ["Rust"],
        "License": {
            "type": ["Apache2"],
            "URL": ["https://github.com/nestordemeure/friedrich/blob/master/LICENSE"],
        },
        "Reference": {
            "Authors": "n/a",
            "URL": "",
        },
        "Release": {
            "version": "n/a",
            "URL": "",
        },
        "Developers": [
            {
                "color": "default",
                "name": "friedrich contributors",
                "URL": "https://github.com/nestordemeure/friedrich/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "go-kriging": {
        "URL": "https://github.com/lvisei/go-kriging",
        "Language": ["GO"],
        "License": {
            "type": ["MIT"],
            "URL": ["https://github.com/lvisei/go-kriging/blob/main/LICENSE"],
        },
        "Reference": {
            "Authors": "n/a",
            "URL": "",
        },
        "Release": {
            "version": "v0.0.1-alpha.15",
            "URL": "https://github.com/lvisei/go-kriging/releases/tag/v0.0.1-alpha.15",
        },
        "Developers": [
            {
                "color": "blue",
                "name": "",
                "URL": "",
            },
        ],
        "Docs": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    "TemporalGP.jl": {
        "URL": "https://github.com/JuliaGaussianProcesses/TemporalGPs.jl",
        "Language": ["Julia"],
        "License": {
            "type": ["MIT"],
            "URL": ["https://github.com/JuliaGaussianProcesses/TemporalGPs.jl/blob/master/LICENSE"],
        },
        "Reference": {
            "Authors": "Tebbutt et al. (2021)",
            "URL": "https://proceedings.mlr.press/v161/tebbutt21a.html",
        },
        "Release": {
            "version": "v0.6.8",
            "URL": "https://github.com/JuliaGaussianProcesses/TemporalGPs.jl/releases/tag/v0.6.8",
        },
        "Developers": [
            {
                "color": "yellow",
                "name": "University of Cambridge",
                "URL": "https://www.cam.ac.uk/",
            },
            {
                "color": "default",
                "name": "Aalto University",
                "URL": "https://www.aalto.fi/en",
            },
            {
                "color": "default",
                "name": "TemporalGPs.jl contributors",
                "URL": "https://github.com/JuliaGaussianProcesses/TemporalGPs.jl/graphs/contributors",
            },
        ],
        "Docs": [
            {
                "tag": "examples",
                "URL": "https://github.com/JuliaGaussianProcesses/TemporalGPs.jl/tree/master/examples",
            },
            {
                "tag": "talk",
                "URL": "https://www.youtube.com/watch?v=dysmEpX1QoE",
            },
        ],
        "Support": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "Framework": [
            {
                "tag": "",
                "URL": "",
            },
        ],
        "GPU": False,
        "Trend": {
            "tag": [""],
            "URL": "",
        },
        "Kernel": {
            "LengthScale": [""],
            "Families": {
                "tag": [""],
                "URL": "",
            },
            "Mixture": {
                "check": False,
                "tag": [""],
                "URL": "",
            },
        },
    },
    # ===============================================
    # NEW ENTRY
    # ===============================================
}

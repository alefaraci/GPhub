# LIST MISSING PACKAGES
from typing_extensions import LiteralString


package_name = (
    "gptk",
    "PyMC-Learn",
    "JuliaGaussianProcesses.jl",
    "Kriging.jl",
    "BayesNetwton",
    "OpenCossan",
    "GPc",
    "BayesianOptimization",
    "BayesianOptimization.jl",
    "PyDeepGP",
    "DeepGP",
    "go-bayesopt",
    "gaussianprocess",
    "goptuna-bayesopt",
    "goptuna-bayesopt",
    "FastGaussianProcess.jl",
    "gp.regression",
    "gpR",
    "GPRust",
    "MultiGP",
    "UQTK",
    "Dakota",
    "Trieste",
    "Raven-inl.gov",
    "Persalys",
    "GPmat",
    "goGP",
    "GPmp",
    "GPEXP",
    "ooDACE",
    "AugmentedGaussianProcess.jl",
    "GeoStats.jl",
    "BayesianLinearRegressors.jl",
    "ApproxiateGPs.jl",
    "JuliaGaussianProcesses.jl",
    "gpax",
    "itergp",
    "pyinterpolate",
    "FRK",
    "fdagstat",
    "KRIG",
    "Gaussian Process Libary",  # (GP)
    "CppGPs",
    "libKriging",
    "pylibKriging",
    "rlibKriging",
    "mlibkriging",
)

for package in package_name:
    print(
        f"""
    # ===============================================
    "{package}": {{
        "URL": "",
        "Language": [""],
        "License": {{
            "type": [""],
            "URL": [""],
        }},
        "Reference": {{
            "Authors": " et al. ()",
            "URL": "",
        }},
        "Release": {{
            "version": "v",
            "URL": "",
            }},
        "Developers": [
            {{
                "color": "",
                "name": "",
                "URL": "",
            }},
        ],
        "Docs": [
            {{
                "tag": "",
                "URL": "",
            }},
        ],
        "Support": [
            {{
                "tag": "",
                "URL": "",
            }},
        ],
        "Framework": [
            {{
                "tag": "",
                "URL": "",
            }},
        ],
        "GPU": "",
        "Trend": [""],
        "Kernel": {{
            "LengthScale": [""],
            "Families": [""],
            "Mixture": "",
            "Mixture Models": [""],
        }},
    }},
    """
    )

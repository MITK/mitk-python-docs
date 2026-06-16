import mitk

project = "mitk"
author = "German Cancer Research Center (DKFZ)"
release = mitk.__version__

extensions = [
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
]

html_theme = "alabaster"

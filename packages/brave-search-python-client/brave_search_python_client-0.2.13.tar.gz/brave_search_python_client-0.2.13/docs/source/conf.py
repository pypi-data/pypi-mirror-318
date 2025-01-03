# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "brave-search-python-client"
copyright = "2025, Helmut Hoffer von Ankershoffen"
author = "Helmut Hoffer von Ankershoffen"
release = "0.2.13"
github_username = "helmut-hoffer-von-ankershoffen"
github_repository = "brave-search-python-client"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
    "sphinx-pydantic",
    "sphinxcontrib.autodoc_pydantic",
    "enum_tools.autoenum",
    "sphinx_copybutton",
    "sphinx.ext.coverage",
    "sphinx_mdinclude",
    "sphinxext.opengraph",
    "sphinx_inline_tabs",
    "sphinx_toolbox",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]
html_logo = "../../brave.png"
html_theme_options = {
    "announcement": (
        '<a target="_blank" href="https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client">GitHub</a> - '
        '<a target="_blank" href="https://pypi.org/project/brave-search-python-client/">PyPI</a> - '
        '<a target="_blank" href="https://hub.docker.com/r/helmuthva/brave-search-python-client/tags">Docker</a> - '
        '<a target="_blank" href="https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_brave-search-python-client">SonarQube</a> - '
        '<a target="_blank" href="https://app.codecov.io/gh/helmut-hoffer-von-ankershoffen/brave-search-python-client">Codecov</a>'
    )
}

# -*- coding: utf-8 -*-
import datetime
import re

import f5_sphinx_theme

# -- Project information -----------------------------------------------------

project = "F5 Control-Plane Security Onion Lab Guide"
author = "F5 Networks"

start_year = "2017"
current_year = datetime.date.today().strftime("%Y")
copyright_year = (
    start_year if start_year == current_year else f"{start_year}-{current_year}"
)
copyright = f"{copyright_year}, {author}"

# The short X.Y version
version = "1.0"
# The full version, including alpha/beta/rc tags
release = "1.0"

# -- General configuration ---------------------------------------------------

master_doc = "index"
language = "en"

extensions = [
    # Keep this minimal for RTD reliability
    "sphinx.ext.todo",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
    "sphinx.ext.coverage",
    "sphinx.ext.ifconfig",
    "sphinx.ext.doctest",
]

# Avoid duplicate section label warnings across multiple files
autosectionlabel_prefix_document = True

templates_path = ["_templates"]

source_suffix = {
    ".rst": "restructuredtext",
}

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    ".github",
]

pygments_style = "sphinx"

todo_include_todos = True
todo_emit_warnings = True

# Optional substitutions you had earlier
rst_epilog = """
.. |platform| replace:: Docker
"""

# -- Options for HTML output -------------------------------------------------

html_theme = "f5_sphinx_theme"
html_theme_path = [f5_sphinx_theme.get_html_theme_path()]

html_theme_options = {
    "next_prev_link": True,
    "version_selector": True,
    "base_url": "/",
    "sidebar_toc_maxdepth": "2",
    "hide_right_menu": True,
}

html_sidebars = {
    "**": [
        "searchbox.html",
        "localtoc.html",
        "globaltoc.html",
        "relations.html",
    ]
}

html_context = {
    "version_meta_path": "versions.json",
    "project_safe": re.sub(r"[^A-Za-z0-9]+", "", project),
}

html_static_path = ["_static"]

html_title = project
html_short_title = "Home"
html_last_updated_fmt = ""

html_show_sourcelink = True
html_show_sphinx = False
html_show_copyright = True

# -- Options for HTMLHelp output --------------------------------------------

htmlhelp_basename = "team_lab_rtd_docs"

# -- Options for linkcheck ---------------------------------------------------

linkcheck_retries = 2
linkcheck_timeout = 5
linkcheck_anchors = False

# -*- coding: utf-8 -*-

import datetime
import re
import f5_sphinx_theme

# -- Project information -----------------------------------------------------

project = "F5 Control-Plane Security Onion Lab Guide"
author = "F5 Networks"

start_year = "2025"
current_year = datetime.date.today().strftime("%Y")
if start_year == current_year:
    copyright_year = start_year
else:
    copyright_year = f"{start_year}-{current_year}"

copyright = f"{copyright_year}, F5 Networks"

version = "1.0"
release = "1.0.0"

language = "en"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
    "sphinx.ext.ifconfig",
    "sphinx.ext.doctest",
    "recommonmark",
]

templates_path = ["_templates"]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

master_doc = "index"

exclude_patterns = [
    "_build",
    ".DS_Store",
    "Thumbs.db",
    ".github",
]

pygments_style = "sphinx"
todo_include_todos = True

# -- HTML output -------------------------------------------------------------

html_theme = "f5_sphinx_theme"
html_theme_path = f5_sphinx_theme.get_html_theme_path()

html_title = project
html_short_title = "Home"

html_static_path = ["_static"]

html_sidebars = {
    "**": [
        "searchbox.html",
        "localtoc.html",
        "globaltoc.html",
    ]
}

html_theme_options = {
    "site_name": project,
    "next_prev_link": True,
    "hide_right_menu": False,          # show "On this page"
    "hide_right_menu_home": True,      # hide only on homepage
    "sidebar_toc_maxdepth": 2,
    "base_url": "/",
    "show_project": True,
}

html_show_sphinx = False
html_show_copyright = True
html_last_updated_fmt = "%Y-%m-%d %H:%M:%S"

# -- GitHub integration (Edit on GitHub) ------------------------------------

html_context = {
    "display_github": True,
    "github_user": "Pierre0824",
    "github_repo": "team-lab-rtd",
    "github_version": "main",
    "conf_py_path": "/site/docs/",
}

# -- Autosectionlabel --------------------------------------------------------

autosectionlabel_prefix_document = True

# -- Todo options ------------------------------------------------------------

todo_emit_warnings = True

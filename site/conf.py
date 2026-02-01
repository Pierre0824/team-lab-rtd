# -*- coding: utf-8 -*-
import datetime
import re

# ---- Project metadata ----
project = 'F5 Control-Plane Security Onion Lab Guide'
author = 'F5 Networks'

start_year = '2017'
current_year = datetime.date.today().strftime('%Y')
copyright_year = start_year if start_year == current_year else f'{start_year}-{current_year}'
copyright = f'{copyright_year}, {author}'

version = '1.0'
release = '1.0'

master_doc = 'index'
language = 'en'

# ---- Extensions ----
extensions = [
    'sphinxjp.themes.basicstrap',
    'sphinx.ext.todo',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.doctest',
    'cloud_sptheme.ext.table_styling',
    'recommonmark',
]

todo_include_todos = True
todo_emit_warnings = True

# ---- Source parsing ----
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = [
    '_build',
    'drafts',
    'Thumbs.db',
    '.DS_Store',
    '.github',
]

pygments_style = 'sphinx'

rst_epilog = """
.. |platform| replace:: Docker
"""

# ---- HTML theme ----
html_theme = 'f5_sphinx_theme'

# Theme repo is at: site/f5-sphinx-theme
# This path is relative to THIS conf.py file: site/docs/conf.py
html_theme_path = ['../f5-sphinx-theme']

html_theme_options = {
    'next_prev_link': True,
    'version_selector': True,
    'base_url': '/',
    'sidebar_toc_maxdepth': "2",
    'hide_right_menu': True,
}

html_sidebars = {
    '**': ['searchbox.html', 'localtoc.html', 'globaltoc.html', 'relations.html']
}

html_context = {
    'version_meta_path': 'versions.json',
    'project_safe': re.sub('[^A-Za-z0-9]+', '', project)
}

html_static_path = ['_static']

html_title = project
html_short_title = 'Home'
html_show_sourcelink = True
html_show_sphinx = False
html_show_copyright = True

# ---- Linkcheck ----
linkcheck_retries = 2
linkcheck_timeout = 5
linkcheck_anchors = False

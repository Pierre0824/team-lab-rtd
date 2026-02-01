# -*- coding: utf-8 -*-
import datetime
import re

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

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.doctest',
    'recommonmark',
]

todo_include_todos = True
todo_emit_warnings = True

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'

html_theme = 'f5_sphinx_theme'
html_theme_path = ['../f5-sphinx-theme']

html_theme_options = {
    'next_prev_link': True,
    'sidebar_toc_maxdepth': "2",
    'hide_right_menu': True,
}

html_sidebars = {'**': ['searchbox.html', 'localtoc.html', 'globaltoc.html']}
html_static_path = ['_static']
html_title = project
html_short_title = 'Home'
html_show_sphinx = False
html_show_sourcelink = True
html_show_copyright = True

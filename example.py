#!/usr/bin/env python

"""Markdown Grid Extension demo"""

import codecs
import markdown
import mdx_grid

def save(file_name, text):
    with codecs.open(file_name, mode="w", encoding="utf8") as f:
        f.write(text)

def load(file_name):
    with codecs.open(file_name, mode="r", encoding="utf8") as f:
        return f.read()

text = load("example.md")

# Case #1: Using existing extension instance with custom configuration
conf = {}
gridext = mdx_grid.GridExtension(configs=conf)
md = markdown.Markdown(extensions=[gridext])
save("example_custom.html", md.convert(text))

# Case #2: Adding extension by name
md = markdown.Markdown(extensions=['grid'])
save("example_defaults.html", md.convert(text))
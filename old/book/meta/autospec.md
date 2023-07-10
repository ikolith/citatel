## Current State

The game is stored in a series of markdown and yaml files. Python scripts automate typesetting, some document generation (including printable cards), and some content generation (rolling for the health of NPCs,  etc).

Curly brackets "{}" in text are used to call out sections that can be automated and entities that exist in the .yamls.

The usual syntax (```[text](path)```, etc.) is used to link between markdown files.

Structure is not stored in a unified way right now. The location of files in the ```doc/``` directory config files like ```navigation.yaml``` determine the site structure, while the order in which generated .tex files are imported into the main book.tex file determine the structure of the book. 

The actual editing is often done in obsidian markdown, but this basically shouldn't matter for the purposes of automation, etc.

## Problems (Not including things that have not been built)

.md->.tex tables is fucked. 

.md links do not become latex page numbers.

## Goals

Start from .md, publish site and print books with minimal fuckery, better handling of custom python-script-markup in .mds.

The links between different mds should resolve to page numbers in latex.

## Next Steps?

In the end, there should be a two shell scripts, one for building the website, one for building the book. They should both use custom Python preprocessing.

In addition to the relatively simple curly templating of the sort {die-roll entity (die-roll??)}, there should be a more robust templating syntax that will just pass the contained text to argparse. Maybe this will be: 
`{$ enlist -fi weapons -fx basic}` or similar...
Worth noting here that enlist would basically never be used for this on its own, rather a new CLI command needs to be written to allow the user to run a filter to return a custom-sorted format-specified set of entities, similar to what is done in update.py, but more specifically md_updater() and similar.

Wile made a set of regex replaces that might fix the ol' longtable fuckery problem.

## Notes

Static sites will likely continue requiring or using .yaml-syntax frontmatter at the beginning of .mds. Might as well use this to our advantage(??).
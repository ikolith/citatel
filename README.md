# citatel

## Abstract

The site lives at https://ikolith.com/.

This is the repo, it includes all of the files used to generate the site with Quarto, all of the tooling and Python scripts, and all of the data.

#TODO

This is a brief list things that must be done, and must be coordinated (otherwise someone would just do them!)

* Currently, run_site.sh *only* does what is needed to generate the files needed to view on this site, using quarto preview. Specifically, this means old, now-erroneous generated files are not deleted, which clutters up the git history and the site search function. Quarto render deletes the old files before rendering all, but this takes too long to want to put it in run_site.sh each time, imo. If there was some way for quarto to process documents in parallel (this seems technically possible, but there is no setting for it in quarto yet. See https://github.com/quarto-dev/quarto-cli/discussions/2749 ) maybe it would be fast enough. However, as it stands, it should be a git hook maybe? I'm not sure if our git hooks do anything right now. I am escalating this to THE HIGHEST AUTHORTIY to review.

## Documentation by file-listing, 2023-01-21

Here is a brief overview of the layout of this project, as it stand now, which hopefully will be of help.

### Useful for content users & creators

* README.md - This file.
* book/ - This is the most important folder. Pretty much all of the actual game content is in this folder.
* assets/ - Website/book assets (media files, ie non-text), including images (just the favicon so far at time of writing)
* citutils/ - Python module for manipulating game content data for 
* cli.py - A command-line program to run queries on the game data and whatnot.
* data/ - Creature and item yaml files and rendered handouts.
* docs/ - Technically useful because it has the rendered html versions of the markdowns, but honestly it's probably bad that this folder isn't gitignored. But github doesn't work with quarto in any other way. So whatever.
* output/ - Using the cli tool sends output here by default.

### Useful for maintainers

* _quarto.yaml - This is the quarto configuration file. It may potentially be useful to modify this iff you need to modify how the website or book are generated.
* apt_setup.sh - This is a shell script (bash) that installs the requirements to run the website locally, on systems with the apt package manager.
* archive_unincorporated/ - Stuff from the old version of the site that didn't get sorted into the new version of the site, yet. Eventually, it should be sorted out or deleted. At which point the folder will be gone and this line of documentation should be removed.
* bot.py - Runs a discord bot that can run these utilities.
* git_hooks/ - currently this just enforces python formatting or something.
* license.md - The license of this project, in all its glory.
* run_site.sh - Run the website (locally).
* update.py - Render cards for weapons from their source texts, I guess.

### Trash-tier

* 404.qmd - This is the 404 page for the website. It has to be in the top level due to quarto's inherent limitations. Note: it has anagrams in it, which are "pretty bad".
* CNAME - This file just has to be here to tell github what the address of the static site should be.
* custom-dark.scss - SASS file.
* custom-light.scss - SASS file.
* index.qmd - Same deal as 404, but for the front page of the website.
* mypy.ini - config for mypy, the python type-checker we use. Just tries to ignore missing imports, that's the only setting we care about right now.
* requirements.txt - Let pip know what this project needs, because apparently the big import statements at the beginning of every python program weren't fucking clear enough.

#### "Hidden" ("dot") files
* .gitignore - This file lists things that git does not track. It may potentially be useful to modify this iff you are doing something in this folder that generates files you don't want to track, but you do want to make commits to the git history.
* .nojekyll - This file apparently needs to be here to tell github not to use jekyll as the engine for this static site.

##### Git-ignored
* .env - This provides the secret key to the Discord bot. You will only have one of these if you make one yourself using your bot key that you get from Discord.
* .git/ - This is the git history. There is no need to manually touch this folder; using git commands and tools should be enough.
* .quarto/ - I guess quarto probably uses this for something. Gitignored, but you will generate it in the course of running the setup script for the site. It just stores dependencies, probably. No need to touch it manually!
* .venv/ - This folder is gitignored, but you will generate it in the course of running the setup script for the site. It just stores python dependencies. No need to touch it manually!
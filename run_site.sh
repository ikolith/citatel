. .venv/bin/activate
cp git_hooks/* .git/hooks/ #This is not necessary to run the site, but it is extremely useful to have this git hook copying step happen at some point, basically constantly, and there's no more-relevant script than this one to put it in.
#quarto render #A call to render is unneeded, as preview calls render implicitly for the pages that need to be updated, it seems.
quarto preview

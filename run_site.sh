cp git_hooks/* .git/hooks/ #This is not necessary to run the site, but it is extremely useful to have this git hook copying step happen at some point, basically constantly, and there's no more-relevant script than this one to put it in.
if [ "$1" == "--dont" ] ; then #The usefulness of this option may be an indication that the current architecture is bad.
  exit
fi
. .venv/bin/activate
if [ "$1" != "--quick" ] ; then
  quarto render #A call to render is needed to clean up any residual now-erroneous files that might be left in there, but once running preview should keep things mostly up to date
fi
quarto preview

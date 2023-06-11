cp git_hooks/* .git/hooks/ #This is not necessary to run the site, but it is extremely useful to have this git hook copying step happen at some point, basically constantly, and there's no more-relevant script than this one to put it in.

help () { # wow, a bourne shell function!
  echo "$0 requires exactly one argument, one of: dont book site full help what
  dont: Exit this script immediately, merely after behind-the-scenes setup operations like copying git hooks (indeed, that's presently the only thing that is done).
  book: Generate a pdf book of the sourcebook.
  site: Generate the html for a website of the sourcebook and serve it locally. This option has tried to optimize for being as fast as possible, and may leave erroneous build artifacts around.
  full: Delete all build artifacts and regenerate everything (book and site). Do this before committing so that you don't have any erroneous files left over. This option will also serve the website.
  help: Print this help message and exit with status 0. This behavior is also triggered by invalid arguments, in which case the program will exit with status 1.
  what: Print “Huh?” and exit with status 2. This is an easter egg feature."
}

if [ "$1" == "" ] || [ "$#" -ne 1 ] ; then #early (non-comprehensive) check for invalid input
  help
  exit 1
fi
if [ "$1" == "help" ] ; then #check for valid help usage
  help
  exit #note that we exit peaceably
fi
if [ "$1" == "dont" ] ; then #The usefulness of this option may be an indication that the current architecture is bad.
  exit
fi

if [ "$1" == "book" ] ; then
  . .venv/bin/activate #TODO: do we need this line in the book workflow?
  quarto render --profile pdf
  #TODO: does the book have a preview option...?
  quarto preview --profile pdf #TODO: again, test this
fi
if [ "$1" == "site" ] ; then
  . .venv/bin/activate
  quarto preview
fi
if [ "$1" == "full" ] ; then
  . .venv/bin/activate
  quarto render #A call to render is needed to clean up any residual now-erroneous files that might be left in there, but once running preview should keep things mostly up to date
  quarto render --profile pdf
  quarto preview
fi

if [ "$1" == "what" ] ; then
  echo Huh?
  exit 2
fi

help; exit 1 #I guess the input was invalid if we got here.
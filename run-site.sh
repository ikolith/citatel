# This script file runs the repo in the sense of making the static site available on localhost. This includes installing dependencies on systems where we've thought about how to do that. Parts of this script are probably redundant with the GitHub Pages static site publishing GitHub Actions workflow, but this script is for doing it locally, not on github.
# This script is intended to run in any shell language (sh, batch, bash, powershell, csh, zsh, fish, etc, etc) and just do a bunch of harmless errors along the way.

cd docs/
echo Attempting to run server.
echo The following program may forget to tell you that you have to open http://127.0.0.1:4000/ once it is done printing things.
echo You may stop the program using Ctrl-c
if [ `bundle exec jekyll serve` ]; then #try quick(er) start # I would also try using  --incremental but I'm not confident in it.
  echo Hypothetically, code here should run after a successfully installed webserver finishes, but I think the ^C you have to send to the server to stop it also kills this Bash script before we can run anything here, hence this echoed text does not print and the exit command is irrelevant.
  exit
fi

echo The server failed, now trying to install the dependencies and then run, in case that is the problem. You may be prompted for your password multiple times during this process. You may also see many harmless errors flash by.

#Dependencies
echo #sudo apt update && sudo apt upgrade #this isn't in the script because (1) takes extra time (2) could break something with upgrades. However, you may wish to run it sometimes.
dpkg -l ruby-bundler jekyll ruby-dev make g++ || sudo apt install ruby-bundler jekyll ruby-dev make g++

#may be redundant
#sudo gem install bundler
bundle install
bundle exec jekyll serve


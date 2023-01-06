green_T=`echo -e "\e[32mT\e[0m"` #the \e[32m illuminates (via being green) the first letter, sort of, in terminals that support that ansi code, which is most.
inverted_T=`echo -e "\e[7mT\e[0m"` #the \e[7m illuminates (via color inversion) the first letter, sort of, in terminals that support that ansi code, which is most.
fraktur_T=`echo -e "\e[20mT\e[0m"` #the \e[20m illuminates (via fraktur) the first letter, sort of, in terminals that support that ansi code, which is almost none.
illuminated_T=`echo -e "\e[7;20mT\e[0m"` #Ideally, the illumination would be fraktur and inverted, probably, but alas I do not have a terminal on which to test such things, as mine does not support fraktur.

read -p "${illuminated_T}his is a quick and dirty setup script. It installs quarto via wget and apt; installs python3 & python3.10-venv via apt, creates and activates a venv, installs python packages, then checks if you have a latex engine (if you don't, it tries to install texlive-full). Are you sure you want to run this script? (y if yes)." -n 1 -r
echo # move further output to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
  echo "Checking quarto."
  if ! command -v quarto &> /dev/null
  then
    echo "Installing quarto" && wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.2.280/quarto-1.2.280-linux-amd64.deb && sudo apt install ./quarto-1.2.280-linux-amd64.deb && rm ./quarto-1.2.280-linux-amd64.deb
  else
    echo "You already seem to have quarto, so I won't try to install it again."
  fi
  echo "Installing python3 and python3.10-venv."
  sudo apt install -y quarto python3 python3.10-venv
  echo "Making and activing venv."
  python3 -m venv .venv
  source .venv/bin/activate
  echo "Installing required python packages."
  pip install -r requirements.txt
  cd citutils;pip install --editable .;cd ..
  if ! command -v pdflatex &> /dev/null
  then
    sudo apt install -y texlive-full
  else
    echo "You already seem to have a latex engine, so texlive-full won't be installed. If you run into issues with tex, try installing texlive-full."
  fi
else
echo "Exiting without doing anything."
fi

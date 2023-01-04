read -p "this is a quick and dirty setup script.
it creates and activates a venv, installs python packages, then checks if you have a latex engine.
if you don't it tries to install texlive-full.
are you sure you want to run this? (y if yes)." -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo "making and activing venv..."
    python3 -m venv .venv
    source .venv/bin/activate
    echo "installing required python packages"
    pip install -r requirements.txt
    cd citutils;pip install --editable .;cd ..
    if ! command -v pdflatex &> /dev/null
    then
        sudo apt-get install texlive-full
    else
        echo "you already seem to have a latex engine, so texlive-full won't be installed.
    if you run into issues with tex, try texlive-full."
    fi
else
echo "exiting without doing anything"
fi
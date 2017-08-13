If you don't have pip:

1. python get-pip.py

To run in virtualenv:

1. pip install virtualenvwrapper --user
2. mkvirtualenv MyApp
3. set the environment like so:
	alias python=python3.6
	export WORKON_HOME=$HOME/.virtualenvs
	export PROJECT_HOME=$HOME/code
	export VIRTUALENVWRAPPER_PYTHON="$(which python3.6)"
	source /usr/local/bin/virtualenvwrapper.sh
4. cd MyApp && workon .

Then:

1. pip install -r requirements.txt  --user
2. pip install . --user
3. go

If you make changes and want to reflect them on the system:

1. pip install . --user --upgrade
2. go

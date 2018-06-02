To install:

If you don't have pip:

1. python get-pip.py

Then:

1. virtualenv .env
2. source .env/bin/activate
3. pip install -r requirements.txt  --user
4. python setup.py build or python setup.py install or python setup.py develop
5. pip list | grep -i myapp
6. go

You can also use pip to call setup.py and install the package for you:

1. pip install .

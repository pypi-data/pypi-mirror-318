# project-name

_______________________________________________________________________________

Project description...

### Create and activate virtual environment.

```commandline
pip install --upgrade pip virtualenv
virtualenv --python=python3.11 .venv
source .venv/bin/activate
```

### Install required libraries.

```commandline
pip install '.[test]'
```

### Check tests and coverage...

```commandline
python manager.py run-tests
python manager.py run-coverage
```

pip install twine build
python -m build
twine upload -u {{user}} -p {{password}} dist/*

twine upload -u __token__ -p pypi-AgEIcHlwaS5vcmcCJDVlYjVjMTI1LWJmOTItNGRjNy1iOWIzLWY1OGEwZWYwMmE2MgACKlszLCJhNDQ0YThkMS02NjVlLTRjMjgtOTE4YS0xYmEzNTRlNzEwNjEiXQAABiBEEMzIUq3nom6ZGinWRQyp31lCwlQyTGFuB3_eLSp6iA dist/*

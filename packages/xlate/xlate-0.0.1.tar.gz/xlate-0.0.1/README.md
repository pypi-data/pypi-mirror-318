# xlate-api

## Updating the PyPi Package
Pypi package link for xlate is [here](https://pypi.org/project/xlate/).

1. Increment the version number.
2. Install twine `pip install --upgrade twine` if you haven't already.
3. Build Distribution: Generate distribution files using `python setup.py sdist bdist_wheel`
4. If you don't already have your twine + pypi credentials setup, follow the instructions here.
5. Finally, run `twine upload dist/*`.
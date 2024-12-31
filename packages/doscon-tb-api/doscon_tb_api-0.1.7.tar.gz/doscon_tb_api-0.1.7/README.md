# tb_api
Library for connecting to thingsboard to perform API actions. 

# How to use
TODO


# TESTS
requires<br>
pytest==7.4.4<br>
pytest-cov==4.1.0<br>

## To run tests
pytest

## How to build
pip install setuptools wheel (first time)<br>

Remove previous dist and update version number in setup.py<br>
python setup.py sdist bdist_wheel<br>

### upload to pipy
pip install twine (first time)<br>

twine upload dist/*<br>
enter username \_\_token\_\_ and api token as password.
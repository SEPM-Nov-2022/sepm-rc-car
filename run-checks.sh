# run bandit

# TODO: To remove the line below in future as redundant given the environment.yml file. For now, had to install 'bandit'
#  here too as on Mac it is not recognised even if installed via the environment.yml file.
pip3 install bandit

bandit --ini .bandit -r > bandit.txt

# run pylint
pylint --extension-pkg-whitelist=pygame $(git ls-files '*.py') > pylint.txt

# run coverage
pytest --cov-report term-missing --cov=rc_car --cov-config=.coveragerc tests
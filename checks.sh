# run bandit

# TODO: To remove the line below in future as redundant given the environment.yml file. For now, had to install 'bandit'
#  here too as on Mac it is not recognised even if installed via the environment.yml file.
pip3 install bandit

bandit --ini .bandit -r > bandit.txt

# run pylint
pylint --extension-pkg-whitelist=pygame rc_car/*.py features/steps/*.py --disable=E0401,E0611,E1101,W0212 > pylint.txt

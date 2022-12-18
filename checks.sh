# run bandit
pip3 install bandit
bandit --ini .bandit -r > bandit.txt

# run pylint
pip3 install pylint
pylint *.py > pylint.txt
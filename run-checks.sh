# run 'bandit' to scan for the first scan of security vulnerabilities

bandit --ini .bandit -r > bandit.txt

# run complementary library ('safety') to further scan for security vulnerabilities

safety check -o text > safety_sec_scan.txt

# run 'pylint' for code quality checks
pylint --extension-pkg-whitelist=pygame $(git ls-files '*.py') > pylint.txt

# run 'pytest' and 'pytest-cov' for reporting test coverage
pytest --cov-report term-missing --cov=rc_car --cov-config=.coveragerc tests
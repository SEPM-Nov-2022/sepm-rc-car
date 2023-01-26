# run 'bandit' to scan for security vulnerabilities (none identified on Jan 25th, 2023)

bandit --ini .bandit -r > bandit.txt

# run complementary library ('safety') to scan for security vulnerabilities (11 identified on Jan 25th, 2023)

safety check -o text > safety_sec_scan.txt

# run 'pylint' for code quality checks
pylint --extension-pkg-whitelist=pygame $(git ls-files '*.py') > pylint.txt

# run 'pytest' and 'pytest-cov' for reporting test coverage
pytest --cov-report term-missing --cov=rc_car --cov-config=.coveragerc tests
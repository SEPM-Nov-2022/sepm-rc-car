# build reports dir
REPORT="reports"
rm -fr $REPORT 2>/dev/null
mkdir $REPORT

# run 'bandit' to scan for the first scan of security vulnerabilities
bandit --ini .bandit -r > $REPORT/bandit.txt

# run complementary library ('safety') to further scan for security vulnerabilities
for x in $(git ls-files '*.py');do
    python3 -m safety check -o text --file $x >> $REPORT/safety_sec_scan.txt
done

# run 'pylint' for code quality checks
pylint --extension-pkg-whitelist=pygame $(git ls-files '*.py') --disable=W0212 > $REPORT/pylint.txt

# run pyflakes
python3 -m pyflakes $(git ls-files '*.py') > $REPORT/pyflakes.txt

# run 'pytest' and 'pytest-cov' for reporting test coverage
pytest --cov-report term-missing --cov=rc_car --cov-config=.coveragerc tests > $REPORT/pytest-cov.txt

# run pycodestyle
python3 -m pycodestyle $(git ls-files '*.py') > $REPORT/pycodestyle.txt
# Transcript on testing
Testing is a key and iterative component of software engineering projects that adhere to the Agile methodology and 
spans across the entire software development lifecycle (SDLC) (Gaikwad _et al_., 2017) on the following environments:
- development, used to create the functionalities of the application, and related unit tests to verify their correct behaviour,
- testing, leveraged for running automated tests to guarantee the expected behaviour of the functionalities developed 
against the product requirements,
- user acceptance testing, with focus on the key users outlined in the design document, i.e., 'child', 'guardian', and 
'producer',
- production, simulating a live environment where further users may use the application differently, thus covering a 
broader set of scenarios.

Thus, testing involves various phases, such as:
- requirements testing (Nielsen & Nielsen, 2019), 
- functional testing to ensure the application runs as expected, 
- unit testing to verify the behaviour of the individual components of the application, 
- security testing to identify any security vulnerabilities in the project's dependencies and mitigate them (if any), and 
- quality checks to ensure a consistent and production-grade code quality.

## Key testing technologies
The following technologies were leveraged for testing:
- `Gherkin` for requirements testing, 
- `pytest` and `pytest-cov` for unit testing, including reporting test coverage in percentage and any missing/uncovered lines,
- `bandit` and `safety` for security checks, assessing vulnerabilities in the dependencies to determine whether 
adding them to the project, thus enabling security by design (Kreitz, 2019), and
- `pylint` for linting based on code quality checks.

## Unit tests
Unit tests, which tests the logic of the key components in the application in a white-box manner (Xie _et al_., 2016), have been added 
inside the `tests` folder, which follows the structure of the `rc_car` directory of the source codes. 
Once outside the `tests` folder, i.e., in the top-level directory, unit tests can be run via `pytest` and `pytest-cov` 
and a comprehensive test coverage report with test coverage in percentage and missing/uncovered lines can be obtained.

## GitHub Actions for CI/CD
GitHub Actions were used for CI/CD (Klotins _et al_., 2022), thus bringing all above-mentioned testing stages together in a single automated 
pipeline, which also ensures the visibility of their results on related reports, as it is fully integrated within GitHub, 
and it is run at every push, including merges into the `main` branch of the repository following an approval and a 
merge of any pull requests (PRs).

## References
- Gaikwad, V., Joeg, P., & Joshi, S. (2017) AgileRE: Agile requirements management tool. In _Proceedings of the Computational Methods in Systems and Software_ (pp. 236-249). Springer, Cham.
- Klotins, E., Gorschek, T., Sundelin, K., & Falk, E. (2022) Towards cost-benefit evaluation for continuous software engineering activities. _Empirical Software Engineering_ 27(6): 157.
- Kreitz, M. (2019) Security by design in software engineering. _ACM SIGSOFT Software Engineering Notes_ 44(3): 23-23.
- Nielsen, L., & Nielsen, L. (2019) Making Your Personas Live. _Personas-User Focused Design_ 161-170.
- Xie, T., Tillmann, N., & Lakshman, P. (2016) Advances in unit testing: theory and practice. In _Proceedings of the 38th international conference on software engineering companion_, 904-905.

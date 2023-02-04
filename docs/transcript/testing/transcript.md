# Code

## The core

The three main elements of the simulation are the remote controller, the car, and the analytics mock server.

The class `Remote` models the remote control: it connects to the car, sends the commands, and manages the analytics. It simulates the mobile app responsible for car control and analytics.

The class `Car` models the RC car: it translates inputs into actions moving the car in the simulation area. It encapsulates the data relative to motion and the battery. The battery system has some complexity that deserved a separate class, `Battery`, to properly separate the dynamics of driving from the logic of consuming energy.

To create a more realistic model, the class `Game` contains all the logic of the simulation, such as most of the `PyGame` functionalities, the game's main loop, and all the elements concerning graphics and audio. The class `Game` simulates the world where the car lives. For example, the `Game`'s function `check walls` is a `Callable` used by `Car` to detect collisions. Similarly, the functions `notify` and `play audio` are `Callables` used by the class `Car` and the class `Remote` to interact with the world by sending messages or sounds.

The class `Car` implements the action that can be performed by a car such as steering and accelerating. All the interaction with a car goes through the method `command`. The only other public methods are `get_battery_level` to provide info about the `battery`, and `handshake remote` to confirm the connection when there is enough charge.

The class `Remote` receives the inputs from the simulation (the class `Game`) and forwards them to the car. It is also responsible for the storage of analytics.

The analytics are managed by the class `Analytics` which stores the data locally and synchronises with the remote server periodically.

The class `AnalyticsStorage` is a separate component to make it easier to mock the I/O during the tests.

An Analytics Mock Server is available for testing. It is a simple Flask-based web application echoing the messages in the shell.

## Overview of the remaining scripts

- The script `Constants` contains all the constants to simplify the maintenance.
- `Logger` configures the application's logging system
- `Utils` contains a utility method that returns the configuration in `environment.yml`
- `RC Car Launcher` is nothing more than the simulation's entry point.

## Running the tests
There are the following shell scripts:
- `run-tests.sh`: executes all the unit tests.
- `run-cucumber.sh`: executes all the bdd tests.
- `run-checks.sh`: generates the reports from the linters.

The reports are available in the folder `reports`.

## Analytics

The project included a remote `Analytics` server able to store data from multiple cars, if not multiple types of toys. For the development, the team created a mock server mimicking the real one in order to test the functionalities.

The `Analytics Mock Server` is a simple `Flask` application. Its only function is to expose a `REST endpoint` and echo the received message in the logs. The class `Remote` stores locally the analytics and periodically synchronize with the remote server. The class `Analytics` stores the session's data in the folder `analytics` creating one file per session. The class `Analytics` continuously updates the file and deletes it if the synchronization is successful.

# Testing
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

## Impact of testing on coding

The main challenge is testing components performing IO, like those interacting with `Pygame`. Some components, like the `Analytics` class, are designed to separate the logic from the IO dependency that is injected separately. The test can inject a mocked object and intercept the calls to verify that the logic components triggers the right IO operations.

## Key testing technologies
The following technologies were leveraged for testing:
- `Gherkin` for requirements testing, 
- `pytest` and `pytest-cov` for unit testing, including reporting test coverage in percentage and any missing/uncovered lines,
- `bandit` and `safety` for security checks, assessing vulnerabilities in the dependencies to determine whether 
adding them to the project, thus enabling security by design (Kreitz, 2019), and
- `pylint`, `pycodestyle` and `pyflakes` for linting based on code quality checks.

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

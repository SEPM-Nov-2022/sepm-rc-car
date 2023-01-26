# sepm-rc-car

## Description
This repository implements a game to control a race car developed using the `pygame` library in Python, as a part of 
the module on 'Software Engineering Project Management' at the University of Essex.

## Repository structure

```
.
├── assets                                # Directory containing app-related images and audio files
│
├── docs                                  # Directory with app-related docs and the team's meeting notes
│
├── features                              # Directory detailing the features and their associated scenarios
│
├── src                                   # Directory containing the source codes for a race car game
│   └── rc_car                            # The main directory
│     ├── car_model                       # Directory with definition of car model and related audio effects and constants
│     ├── constants.py                    # The race car game's main constants
│     ├── game.py                         # The race car game's main functionalities
│     └── rc_car_launcher.py              # The race car game launcher
│
├── .bandit
├── .coveragerc
├── .gitignore
├── checks.sh
├── environment.yml
├── LICENSE.md
├── pyproject.toml
├── README.md
├── run.sh
├── run-cucumber.sh
├── setup.cfg
└── setup.py
```

## Installation

* Update conda

Update conda by executing the following command:

`conda update -n base -c defaults conda`

* Create the virtual environment

Create a conda virtual environment named `rc_car` and install the required dependencies/libraries
(listed in the `environment.yml` file) by executing the following command: 

`conda env create --name rc_car --file environment.yml`

* Activate and deactivate the conda environment

To activate this environment, execute the following command:

`conda activate rc_car`

To deactivate the environment, execute the following command:

`conda deactivate`

To install the project as a package in non-editable (standard) mode:

`pip install .`

To install the project as a package in editable (development) mode:

`pip install -e .`

## Run

launch `./run.sh`

## Quality checks

Launch `./checks.sh`, then verify `banding.txt` for security and `pylint.txt` for linting

Note: some `pygame`-related errors [may be impossible to fix](https://stackoverflow.com/questions/57116879/how-to-fix-pygame-module-has-no-member-k-right).

e.g.:
```
py:3:0: E0611: No name 'K_UP' in module 'pygame.constants' (no-name-in-module)
car.py:3:0: E0611: No name 'K_DOWN' in module 'pygame.constants' (no-name-in-module)
car.py:3:0: E0611: No name 'K_RIGHT' in module 'pygame.constants' (no-name-in-module)
car.py:3:0: E0611: No name 'K_LEFT' in module 'pygame.constants' (no-name-in-module)
car.py:3:0: E0611: No name 'K_SPACE' in module 'pygame.constants' (no-name-in-module)
car.py:4:0: E0611: No name 'Vector2' in module 'pygame.math'
game.py:19:8: E1101: Module 'pygame' has no 'init' member (no-member)
game.py:33:33: E1101: Module 'pygame' has no 'QUIT' member (no-member)
game.py:40:8: E1101: Module 'pygame' has no 'quit' member (no-member)
```

## Unit tests
Unit tests have been implemented under the `tests` folder, which follows the structure of the `rc_car` directory of 
the source codes.

Once outside the `tests` folder, i.e., in the top-level directory, unit tests can be run via `pytest` and a comprehensive 
test coverage report with test coverage in percentage (92% as of Jan 21st, 2023) and missing lines can be obtained by 
executing the following command:

`pytest --cov-report term-missing --cov=rc_car --cov-config=.coveragerc tests`

The test coverage, along with linting/quality checks, are run automatically via GitHub Actions for CI/CD as per 
the pipeline defined at `.github/workflows/pylint_pytest_git_actions.yml`. Thus, the linting and test coverage 
reports are conveniently and transparently available in the builds directly on GitHub.


## References
- App Of The Day. (n.d.) Race It! - 2D Racing Game. [online] Available from: https://appoftheday.downloadastro.com/app/race-it-2d-racing-game/ [Accessed 12 Jan. 2023].
- Fine, C., & Rush, E. (2018) Why does all the girls have to buy pink stuff? The ethics and science of the gendered toy marketing debate. _Journal of Business Ethics_ 149(4): 769-784.
- Freepik. (n.d.) Free Vector | Profile icons pack in hand drawn style. [online] Available from: https://www.freepik.com/free-vector/profile-icons-pack-hand-drawn-style_18156023.htm [Accessed 22 Jan. 2023].
- Gaikwad, V., Joeg, P., & Joshi, S. (2017) AgileRE: Agile requirements management tool. In _Proceedings of the Computational Methods in Systems and Software_ (pp. 236-249). Springer, Cham.
- Howe, O. R. (2022) Hitting the barriers–Women in Formula 1 and W series racing. _European Journal of Women's Studies_ 13505068221094204.
- Klotins, E., Gorschek, T., Sundelin, K., & Falk, E. (2022) Towards cost-benefit evaluation for continuous software engineering activities. _Empirical Software Engineering_ 27(6): 157.
- Kreitz, M. (2019) Security by design in software engineering. _ACM SIGSOFT Software Engineering Notes_ 44(3): 23-23.
- Manaog, M. L. (2022) Environment-related logging. [online] GitHub. Available from: https://github.com/emesdav/team-separation-of-duties/commit/475a442070105949974e8df12a2fcd261dfa45b7 [Accessed 12 Jan. 2023]
- Mitchell-Malm, Scott (2021) “Hamilton Commission Reveals Stark F1 Diversity Findings”. _The Race.com_. Available from: https://the-race.com/formula-1/hamilton-commission-reveals-stark-f1-diversity-findings/.) [Accessed 22 Jan. 2023].
- Morgan, R. and Scarlett, Y. (2021) Accelerating Change: Improving Representation of Black People in UK Motorsport. [online] _The Hamilton Commission_. Available at: https://www.hamiltoncommission.org/the-report.
- Nielsen, L., & Nielsen, L. (2019) Making Your Personas Live. _Personas-User Focused Design_ 161-170.
- Piquero, A. R., Piquero, N. L., & Riddell, J. R. (2021) Do (sex) crimes increase during the United States Formula 1 grand prix?. _Journal of Experimental Criminology_ 17(1): 87-108.
- Reid, M. B., & Lightfoot, J. T. (2019) The physiology of auto racing: a brief review. _Medicine and science in sports and exercise_ 1-15.
- Warwick, M. (2023) Why are there no women at the top of motorsport?. _BBC Sport_. [online] Available from: https://www.bbc.com/sport/motorsport/64338226 [Accessed 21 Jan. 2023].
- Xie, T., Tillmann, N., & Lakshman, P. (2016) Advances in unit testing: theory and practice. In _Proceedings of the 38th international conference on software engineering companion_, 904-905.
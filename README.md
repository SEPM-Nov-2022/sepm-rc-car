# sepm-rc-car

## Description
This repository implements a game to control a race car developed using the `pygame` library in Python, as a part of 
the module on 'Software Engineering Project Management' at the University of Essex.

## Repository structure

```
.
├── .github                               # Directory containing app-related GitHub Actions for CI/CD
│
├── assets                                # Directory containing app-related images and audio files
│
├── audit_server                          # Directory containing app-related audit server
│
├── docs                                  # Directory with app-related docs, presentation transcripts, and the team's meeting notes
│
├── features                              # Directory detailing the features and their associated scenarios
│
├── rc_car                                # Directory containing the source codes for a race car game
│     │
│     ├── analytics.py                    # The race car game's analytics, including those for storage
│     ├── audio_effect.py                 # The race car game's audio effects (horn and low battery)
│     ├── battery.py                      # The race car game's battery class, and key attributes and methods
│     ├── car.py                          # The race car game's car class, and key attributes and methods
│     ├── constants.py                    # The race car game's main constants
│     ├── game.py                         # The race car game's main functionalities
│     ├── logger.py                       # The race car game's centralised custom logger
│     ├── menu_item.py                    # The race car game's for menu for changing user's profile picture
│     ├── rc_car_launcher.py              # The race car game's launcher
│     ├── remote.py                       # The race car game's remote controller
│     └── utils.py                        # Key utility-based functions
│
├── .bandit
├── .coveragerc
├── .gitignore
├── environment.yml
├── LICENSE.md
├── README.md
├── run.sh                                # To run game launcher and audit server
├── run-checks.sh
├── run-cucumber.sh
├── run-tests.sh
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

## Run the game

Launch `./run.sh`

## Security and code quality checks

Launch `./checks.sh`, then verify:
- `banding.txt` and `safety_sec_scan.txt` for security, and 
- `pylint.txt` for linting

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

## GitHub Actions for CI/CD
The test coverage, along with linting/quality checks, are run automatically via GitHub Actions for CI/CD as per 
the pipeline defined at `.github/workflows/github_actions.yml`. Thus, the linting, test coverage 
reports, and security scans are conveniently and transparently available in the builds directly on GitHub.

## References
- Gaikwad, V., Joeg, P., & Joshi, S. (2017) AgileRE: Agile requirements management tool. In Proceedings of the Computational Methods in Systems and Software (pp. 236-249). Springer, Cham.
- Howe, O. R. (2022) Hitting the barriers–Women in Formula 1 and W series racing. European Journal of Women's Studies 13505068221094204.
- Klotins, E., Gorschek, T., Sundelin, K., & Falk, E. (2022) Towards cost-benefit evaluation for continuous software engineering activities. Empirical Software Engineering 27(6): 157.
- Kreitz, M. (2019) Security by design in software engineering. ACM SIGSOFT Software Engineering Notes 44(3): 23-23.
- Mitchell-Malm, Scott (2021) “Hamilton Commission Reveals Stark F1 Diversity Findings”. The Race.com. Available from: https://the-race.com/formula-1/hamilton-commission-reveals-stark-f1-diversity-findings/.) [Accessed 22 Jan. 2023].
- Nasir, M. (2006). A Survey of Software Estimation Techniques and Project Planning Practices. [online] IEEE Xplore. doi:10.1109/SNPD-SAWN.2006.11.
- Nielsen, L., & Nielsen, L. (2019) Making Your Personas Live. Personas-User Focused Design 161-170.
- Phillips, D. (2018). Python 3 Object-Oriented Programming. 3rd Edition. [Insert Publisher Location]: Packt Publishing.
- Pygame. (2022). [online] Available at: https://www.pygame.org/.
- Reid, M. B., & Lightfoot, J. T. (2019) The physiology of auto racing: a brief review. Medicine and science in sports and exercise 1-15.
- Svilarov, A. (2019). Race It! - 2D Racing Game. Available from: https://appoftheday.downloadastro.com/app/race-it-2d-racing-game/ [Accessed 12 Jan. 2023].
- Xie, T., Tillmann, N., & Lakshman, P. (2016) Advances in unit testing: theory and practice. In Proceedings of the 38th international conference on software engineering companion, 904-905.

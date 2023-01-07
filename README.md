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

launch `./checks.sh` then verify `banding.txt` for security and `pylint.txt` for linting

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
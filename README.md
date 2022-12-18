# sepm-rc-car

## Installation

launch `./setup.sh`

## Run

launch `./run.sh`

## Quality checks

launch `./checks.sh` then verify `banding.txt` and `pylint.txt`

Note: pygame errors [may be impossible to fix](https://stackoverflow.com/questions/57116879/how-to-fix-pygame-module-has-no-member-k-right)

e.g.
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
# Games
Installing Free Python Games is simple with pip:

$ python -m pip install freegames
Free Python Games supports a command-line interface (CLI). Help for the CLI is available using:

$ python -m freegames --help
The CLI supports three commands: list, copy, and show. For a list of all games run:

$ python -m freegames list
Any of the listed games may be played by executing the Python module from the command-line. To reference the Python module, combine “freegames” with the name of the game. For example, to play the “snake” game run:

$ python -m freegames.snake
Games can be modified by copying their source code. The copy command will create a Python file in your local directory which you can edit. For example, to copy and play the “snake” game run:

$ python -m freegames copy snake
$ python snake.py
Python includes a built-in text editor named IDLE which can also execute Python code. To launch the editor and make changes to the “snake” game run:

$ r
You can also access documentation in the interpreter with Python’s built-in help function:

>>> import freegames
>>> help(freegames)

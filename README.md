![Logo](https://github.com/Martinliporace/holbertonschool-AirBnB_clone/blob/master/hbnb.png?raw=true)

# AirBnB clone - The console

# First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone.

This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

# Console

The console is a command line interpreter that permits management of the backend of HolbertonBnB.

# Using the Console
* The HolbertonBnB console can be run both interactively and non-interactively. To run the console in non-interactive mode, pipe any command(s) into an execution of the file console.py at the command line.

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):

EOF  all  count  create  destroy  help  quit  show  update

(hbnb)

$

* Alternatively, to use the HolbertonBnB console in interactive mode, run the file console.py by itself:

$ ./console.py

* While running in interactive mode, the console displays a prompt for input:

$ ./console.py
(hbnb)

* To quit the console, enter the command quit, or input an EOF signal (ctrl-D).

$ ./console.py
(hbnb) quit
$

$ ./console.py
(hbnb) EOF
$

# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

# General
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

# Requirements
# Python Scripts
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.8.*)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

# Python Unit Tests
* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* All your test files should be inside a folder tests
* You have to use the unittest module
* All your test files should be python files (extension: .py)
* All your test files and folders should start by test_
* Your file organization in the tests folder should be the same as your project
e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
* All your tests should be executed by using this command: python3 -m unittest discover tests
* You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case

# Testing
Unittests for the HolbertonBnB project are defined in the tests folder.

**Intercom Take Home Test
**This repository contains the code for the Intercom Take Home Test in which we invite guests within 100km of the Dublin offices to an event.

Have chosen Python 3.6 since it is a quick language to write, is well-supported, is well understood by most devs, and performance isn't critical. Something like this could be run in AWS Lambda which works well with Python.

Output is written to ./output.txt.

Assumptions
Since this is meant to be run in production, the environment will be well known. If it was meant to be distributed amongst Intercom staff then we would have to modify for different versions of Python and OS's.

Assumptions:

will be run in Ubuntu 18.04.
64 bit machine, accuracy should be enough to avoid using the numeric version to calculate great circle distance.
Earth's diameter is 6371km.
Assumed there will be a Person model.
Have hardcoded the Dublin office coordinates and distance threshold in a const file, could have also accepted them as program arguments.
Throwing a custom IntercomExecption on any error cases
Have used decimal.Decimal for better floating point accuracy.
Directory Structure
intercom_test/ - parent directory

├── models/ - where all your models go
│ ├── __init__.py
│ └── person.py - model for the Intercom person
├── res/ - contains resources
│ ├── in.txt - input file containing users
│ └── out.txt - output of the program containing invited guests
├── tests/ - tests
│ ├── __init__.py
│ ├── test_mathsUtils.py - tests for maths utility functions
│ ├── test_inviteUtils.py - tests for invitation events code
│ └── test_fileUtils.py - tests for file utility functions
├── utils/ - any utility functions
│ ├── __init__.py
│ ├── mathsUtils.py - file for any maths related utility functions
│ └── fileUtils.py - file for any file related utility functions
  └── inviteUtils.py - file for any invitation related utility functions
  └── const - variables that don't change run to run


├── .gitignore
├── main.py - main file for job server
├── requirements.txt - requirements for Python
└── README.md - this file
Pre-requisites
Ubuntu 18.04
Python 3.6
To check you have this, enter the following into your command line:

$ python3 --version
If you do not see something like Python 3.6.8 then you will need to install it and return here afterwards.

Installation
In the parent directory (intercom_test), run:

$ pip3 install -r requirements.txt
To Run
$ python3 main.py
To Test
In the parent directory, run:

$ py.test

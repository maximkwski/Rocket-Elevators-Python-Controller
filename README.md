# Rocket-Elevators-Python-Controller
This program simulates the work of Elevator.  In our case we have a Column that holds two elevators. 
And when we run our program, depends on the scenario, what our code does is finds best of two elevators  to pick user up and send to requested floor, when user request floor from the inside of elevator.
Depends on locations of elevators and if elvator's status (if it's being used or if it's on "idle") and users location and requested destination program will send the right elevator to requested floor. 
Scenarios are included in test file, that runs our program and check if it works correctly. 

To make sure that Program does work correctly, we have a test file. 
To run the test we need we have to make sure we have everything installed and ready:

### Installation

First, depending on your python version, make sure to install the Package Installer for Python (PIP) if needed:
https://pip.pypa.io/en/stable/installing/

Next, install Pytest:
https://docs.pytest.org/en/6.2.x/getting-started.html

### Running the tests

To launch the tests:

`pytest`

With a fully completed project, you should get an output like:
![Screenshot from 2021-06-15 13-13-13](https://user-images.githubusercontent.com/28630658/122095645-a41fa000-cddb-11eb-9322-81a766cce4bb.png)

You can also get more details about each test by adding the `-v` flag: 
`pytest -v` 

which should give something like: 
![Screenshot from 2021-06-15 13-13-33](https://user-images.githubusercontent.com/28630658/122095759-c74a4f80-cddb-11eb-999d-dfe35dbe7d18.png)
The test file can be left in your final project but no scenarios should be present in your code. The grader will run tests similar to the ones provided.

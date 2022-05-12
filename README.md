# Osango Academy for Test Automation exercise 2 
### Robot Framework Code: 
*In order to show a little of my understanding when it comes to Robot framework and with the purpose to develop more of this one* 
*I'll be describing a the code that was created for this exercise work* 
### Robot Framework File:
In the first exercise we have the filed named _rf_jose.robot_ , this file contains the test cases that are to be checked for the 
exercise to be succesfully completed. 

```python
*** Settings ***

# First section in the structure of a robot framework file, here we will include and/or import the libraries 
# or classes needed to perform our test.

*** Variable  ***

# The variable section is where we will store all the global variables, Scalar, list &/or Dictionary.
# since there are no global variables needed or used for this test case it is left empty and without
# being declared 

*** Test Cases ***

#  In this section of the code we are able to create the test cases that will be needed, indentention is key when creating test cases, 
# the first line for each test case does not require indentation and is used to describe the test taking place. 
# for the following lines where the test case is developed, indentation will be needed as well as the correct place where local
# variables can be declared, in this case the best example will be:

    ${out} = "keyword" "arguments to be passed for processing. 

# the scope of the variable ends at the beginning of the next test case or the next section of the robot framework code. 

*** Keywords ***

# with keywords it should be selfexplanatory, like with test cases the first line of each keyword is without indentation 
# and is done to create a description of the the keyword itself. 
# it is here where methods/functions like arguments will be declared and evaluated it. the same rule applies for the
# use of variables as it did within the test cases sections, at least with regards to the scope. 

# Another important feature of robot framework that should be noticed here is the use of *[Arguments]* 
# in this exercise we can see a named argument syntax within the keywords section, and making use of the imported library
# *cmds_jose.py*
```

### Python Library/Class

In this section of the documentation I'll go over the two python libraries or classes that are used as the testing object for this exercise. 
The name of this two files is *cmds_jose.py* and *rps-server_jose.py*.

#### -- cmds_jose.py

From the very beginning in this file we can see something that is common in all programming language, that being
a place for declearing and importing classes or libraries, the class that is imported first is the ***requests*** library
in a most simple description what ***requests*** library does is abstracting the complexities of making request behind a simple
API, that way you can focus on interacting with sercies and consuming data of any application. 

The second library being imported into this document is the ***re*** library which refers to the Regular expression operations library. 

The class itself is what I would consider and mini API that serves as an interface and that allows comunication between the server and 
the automated test, this one also serves as delimitator between the different stages of a transition circuit, process or table. I'm not 
what term to use in this case. 

In my opinion the most important piece of code in this is the function *send_cmds* as it is the one that recieve the arguments from the robot test 
file and is the one that allows for the transition of states within the server state machine.
the command *SetPower* allows to set the current value of the state and the command *GetPower* returns the state in which we are currently located. Onto the next file then!

#### -- rps-server_jose.py

This file is what we will be testing, it represents a Remote Power Supply, RPS, as we do not have a RPS hardware, we used this one to simulate
one. In this case the RPS has a http server and users would be able to send commands to turn it on/off by using the http request, this 
on/off options function as two different state. In order to run the RPS server we will use Flask.
Flask is a web framework, a python module that let's you create web applications and unlike Django framework it is easier to get started with
as it doesn't have a great learning curve. 

***It is important to mention that Flask has been installed in a virutal environment separate from the file where this project is located,*** 
***this is important to consider as it is known that a system wide package installation may cause conflicts.***

That being address we can continue with describing what every piece of code within the file does:
the first portion of the code:

```python
from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
```
This piece of code, just like it was explained for ***cmds_jose.py*** file imports the Flask into python and also imports the ***request*** 
library. 
***flask_httpauth*** is a Flask extension that attempts to simplifi the use of HTTP authentication by using Flask Routes, the specific 
library being imported is ***HTTPBasicAuth***, for more indept information for the usage of this library you go [here](https://flask-httpauth.readthedocs.io/en/latest/)





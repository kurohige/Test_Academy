# Osango Academy for Test Automation exercise 2 
### Robot Framework Code: 
*In order to show a little of my understanding when it comes to Robot framework and with the purpose to develop more of this one* 
*I'll be describing a the code that was created for this exercise work* 
#### Robot Framework:
In the first exercise we have the filed named _rf_jose.robot_ , this file contains the test cases that are to be checked for the 
exercise to be succesfully completed. 
```
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
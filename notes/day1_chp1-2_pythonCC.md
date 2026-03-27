#Running python3 in terminal
use command: python3
then type any line of command and it will run
use cntrl-z to escape session

#Basic Python
A file ending with .py indicates a file is a python file
Editor then runs file through python interpreter 

#Variables
Every variable is associated with a value which is connected 
Can reassign the value of a variable with the = operator 
variable names can only have letters, numbers and underscores and cannot start with a number
-Variables are labels you can assign to values

#Error reading
“Traceback (most recent call last):
➊    File "hello_world.py", line 2, in <module>
➋      print(mesage)
➌ NameError: name 'mesage' is not defined”
1 tells us the line of the error
2 tells us the exact line written
3 gives info on the type of error

#Strings
A string is a series of characters 
Anything inside quotes is considered a string in python
You can use single or double quotes as long as it is consistent
A method is an action python can preform on a piece of data: 
.upper() - all to uppercase 
.lower() - all to lowercase
.title() - all to title case
f-strings or formatted strings replace variable names with their data in a string
    f"{var1} is {val2}"
to add a tab use \t
to add a newline use \n
use .rstrip() to remove extra whitespace at the end of a string
.lstrip() for beginning of string
and just .strip() to remove both

#Numbers
can +, -, *, / numbers in python
** for exponents
dividing any 2 numbers in python gives a float
you can group digits with _ to make numbers more readable 1_000_000
multiple assignment is x, y, z = 0, 0, 0 needs the correct amount of values to assign
Python programers use all caps variables to indicate a constant since there is no built in type




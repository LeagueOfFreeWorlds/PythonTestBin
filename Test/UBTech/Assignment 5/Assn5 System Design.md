# Assn5 System Design:
## Requirements:
Create a program that stores user names physically on the hard drive, such that it can be retrieved in the future by other users as part of a database of names.
## System analysis:
The program will prompt the user to enter their name upon initialization of the program. Once the user has entered both their first and last names, the program will save the name,
and proceed to display a menu of options for the user. The menu output will use numerical selection in order for the user to select a menu option of their choice.
## System Design:
Step 1: Program will prompt user to enter their first and last name (first, last), separated by a comma so that it can easily be assigned to a list or tuple.
Step 2: Program will take user's name, store it in an array, and then save it to a .txt or .md file that the program can later retrieve.
Step 3: Once the program has successfully entered the user's name into a retrievable file, it will then display a menu for which the user can choose from.
Step 4: Menu options will include reading the list of names that have been assigned. When the user has entered a number corresponding to the desired value, the program will provide a
        desired output.
            Example:
                1. Enter another name.
                2. See the list of names that have been added.
                3. Quit.
Step 5: The program will have to read, write, and continue running so long as the user wishes, until they decide to quit.
## Implementation (Time to code :) ). We'll be using Python in this instance.

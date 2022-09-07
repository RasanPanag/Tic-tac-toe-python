# Code Created by: Rasandeep Singh Panag


## General Concept
There will be two player in a game. Two signs represent each player. The generals signs
used in the game are "X" and "O". Finally, there will be a board with 9 boxes.

- First, one user (either "X" or "O") will place their sign in one of the available empty boxes.  
- Next, the second user will place their sign in remaining boxes  
- The game will end in winning if one of the player has placed their respective signs three consecutive time in straight line row-wise, column-wise or diagonally. Or Else, it is draw, if all boxes are filled.  


## Pseudocode
- Function to check if the board is filled or not. Iterated over the board and return false if the board contains an empty signs or else return true.  
- Function to check if the player has won or not. Check for all the rows, columns and two diagonals    
- Function to show the board multiple times to user when they are playing.
- Function to create a board using 2-d array and initialize each element as empty by using a hyphen "-"  
- Function to start the game: Select random first turn and write infinite loop that breaks when game is over.  
- Get input from the user to enter the row and column number.  
- Check whether the current player won the game or  not.  
- If current has player has win then print win message and break the loop.
- Else check if the the board is filled or not: if it is filled, then print draw message and break the loop  
In the end, show the user final view of the board.  

## Python features used:
- **Functions**: it is block of code which only runs when it is called.     
- **For Loops**: They are used for iteration over a sequence.    
- **If Else Loop**: Use the logical conditions from mathematics for e.g. equals, not equals, less than etc.     
- **Lists**: They are use to store multiple item in a single variable.     
- **2-d Arrays**: indexed by two subscripts, one for the row and one for column.    
- **Recursion**: it is way that defined function call itself.    
- **Map**: This function executes a specified function for each item in a iterable. The item is sent to the function as a parameter.  
- **Split**: This method is used to split a string into list  
- **Booleans**: represents one of two values true or false   
- **Arithmetic Operators**: Used for common mathematical operation for e.g: "+", "-" etc.  
- **Assignment Operators**: Used to assign values to the variables for e.g. "=", "+=" etc.    
- **Comparison Operators**: Used to compare two values for e.g. "==", "!=" etc.  

## Other relevant information:
- All the python code is **main.py** file   
- All the images of code running is in **images of code running** folder  

## References:
https://www.w3schools.com/python/   

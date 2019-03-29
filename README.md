# checkerboard-of-Eight-digitals
  ### achieve function with A* algorithm in python, UI with tkinter package to draw

# py file function:
## 1 full_arrage.py: the eight digitals code problem is that ,you can give a random sequence consisted of 1,2,3,4,5,6,7,8,0,
and the char '0' is stands for the space position in the 3*3 checkerboard.
in order to get a random seqence, i firstly generated all the posible sequence.
and the seqences are stored in the  full_arrange.json file 

## 2 get_even_sequence.py is to get the even sequence from the full_arrange.json file ,and store them to even_sequence_result.json
   because the fianl status is [[1,2,3],[4,5,6],[7,8,0]] ,
   which is represent in the code with the one dimension list[1,2,3,4,5,6,7,8,0],
   which is an even sequence,in this sequence,the char '0' is not computed in the add rank and even rank.
   
## 3 A_star.py is the main algorithm to get the status move to the final status,
the route result is stored in the route_result.json,
the py's input is firstly stored to the eight.txt

## 4 tkinter_UI ,which is the UI part of my project,use tkinter package to as the board,and have a dynamic effect of the route status move in the UI
you can input your expected sequence in the input field,but you need to click the "confirm input" button to check whether 
the input is valid.
Also you can click the Run to random generate a valid start sequence to see its effect.

# Hint
# the fianl status is [[1,2,3],[4,5,6],[7,8,0]] in the 3*3 checkerboard

** Thanks !
good luck to everyone! **

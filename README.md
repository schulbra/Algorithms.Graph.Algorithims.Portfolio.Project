# Algorithms.Graph.Algorithims.Portfolio.Project
Puzzle.py solves the below problem:

Q. You are given a 2-D puzzle of size MxN, that has:   
   - N rows and M column (N>=3 ; M >= 3; M and N can be different).      
   - Each cell in the puzzle is either empty or has a barrier.
   - An empty cell is marked by: 
       ‘-’ (hyphen) 
     and the one with a barrier is marked by: 
       ‘#’ (num)  
       
   - Sample Input Puzzle Board:    
    [[-,-,-,-,-],
     [-,-,#,-,-],
     [-,-,-,-,-],
     [#,-,#,#,-],
     [-,#,-,-,-]]    
     
   - You are given two coordinates from the puzzle:
       (a,b),  
       (x,y)     
     You are currently located at (a,b) and want to reach (x,y).   
     You can move only in the following directions:
         L: left cell from the curr cell    
         R: right cell from the curr cell    
         U: move upwards to cell above the curr cell    
         D: move down  to cell from the curr cell 
     You can move to only an empty cell and cannot move to a cell with a barrier in it.  
     
   - Your goal is to find the minimum number of cells that you have to cover to reach the 
     destination cell (not including start/destinsation cells)   
     The coordinates (1,1) = first cell; 
                     (1,2) = second cell in the first row.
                      
   - If there is not possible path from  source to desdtination return: "None"     


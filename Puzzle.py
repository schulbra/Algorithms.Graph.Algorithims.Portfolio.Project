# -----------------------------------------------------------------------------|
# Name: Brandon Schultz
# Date: 7-30-21
# Assignment: Graph Algorithms
# Question 5   -   Apply BFS/DFS/MST to solve a problem (Portfolio Project Problem): 

'''
- You are given a 2-D puzzle of size MxN, that has:
  - N rows and M column (N>=3 ; M >= 3; M and N can be different). 
    - Each cell in the puzzle is either empty or has a barrier.  An empty cell is marked by:
      ‘-’ (hyphen) and the one with a barrier is marked by ‘#’. 

- You are given two coordinates from the puzzle:
   (a,b) and (x,y). 
    -You are currently located at (a,b) and want to reach (x,y). 

- You can move only in the following directions:
  L: left cell from the curr cell 
  R: right cell from the curr cell 
  U: move upwards to cell above the curr cell 
  D: move down  to cell from the curr cell 
    -You can move to only an empty cell and cannot move to a cell with a barrier in it. 

- Your goal is to find the minimum number of cells that you have to cover to reach the destination cell (not including start/destinsation cells)
  - The coordinates (1,1) = first cell; 
                    (1,2) = second cell in the first row. 
  - If there is not possible path from  source to desdtination return:
    - None. 
  
- Sample Input Puzzle Board: 
  - [[-,-,-,-,-],[-,-,#,-,-],[-,-,-,-,-],[#,-,#,#,-],[-#,-,-,-]]
  
'''
#
# Sources:
# - https://brilliant.org/wiki/depth-first-search-dfs/
# - https://xlinux.nist.gov/dads/HTML/depthfirst.html
# - https://www.w3schools.com/python/ref_func_len.asp
# - https://www.cs.utexas.edu/%7EEWD/transcriptions/EWD08xx/EWD831.html
# -----------------------------------------------------------------------------|

#|-----------------------------------------------------------------------------|
# Funtion for finding min number of cells that you have to travel strating from # the first cell coordinate (1,1) to reach the  # destination cell coordinate
# (1,2).
# Uses depth first approach to build accumulation of valid paths (result)
# before printing path of min value.
# -----------------------------------------------------------------------------|
def solve_puzzle(Board, Source, Destination, activePath, traversedCells):
    # Current path traveled is returned once destination and active cell coordinates match. 
    if Source == Destination:
        return [activePath]
    result  = []  #  holds all possible paths where min path is selected from

    activeCellX, activeCellY = Source[0],Source[1]
    #L: move to left cell from the current cell
    #R: move to right cell from the current cell
    #U: move to upper cell from the current cell
    #D: move to the lower cell from the current cell
    for destCellX, destCellY, destCellZ in [(1, 0, 'D'),(0, 1, 'R'),(-1, 0, 'U'),(0, -1, 'L')]:

      # Movement options for traveling from origin coordinate to detinations
      #x,y corodinates of next Source, or where what were tracking could potentially move in regards to moving in general direction of Destination coordinates without taking into account invalid cells
      nextActiveCellX = activeCellX + destCellX
      nextActiveCellY = activeCellY + destCellY
      
      # Movement validation. The first if statement ensures that the next movement is within bounds of the given Board in main() and checks that the spot being moved to, and considered the new Source/tracked consists only of the "-" character.
      '''
       N-rows = len(Board) = 5
       M-columns = len(Board[0]) = 5

      Board =[["-", "-", "-", "-", "-"],
                    ["-", "-", "#", "-", "-"],
                    ["-", "-", "-", "-", "-"],
                    ["#", "-", "#", "#", "-"],
                    ["-", "#", "-", "-", "-"]]
            
      '''
      if 0 <= nextActiveCellX < len(Board) and 0 <= nextActiveCellY < len(Board[0]) and Board[nextActiveCellX][nextActiveCellY] == "-":

            # Validates cell coordinates of next Source position by first determining if potential movement option's coordinates are repeats.
            if (nextActiveCellX,nextActiveCellY) not in traversedCells:

                # If not repeats, via not being vals within traversedCells,add them to traversedCells and make position next Source by traversing to coordinate vals of cell added to traversedCells
                traversedCells.add((nextActiveCellX,nextActiveCellY))
                temp = solve_puzzle (Board , (nextActiveCellX,
                nextActiveCellY), Destination, activePath + destCellZ,traversedCells)

                # Backtracking step  used in depth first approach solution for question. Once all paths to/from destination/origin coordinates have been accumulated a min path is determined, and displayed to user.
                if temp:
                    result += temp
                traversedCells.discard((nextActiveCellX,nextActiveCellY))

    return result

def main():
    Board =[["-", "-", "-", "-", "-"], # M-columns
                  ["-", "-", "#", "-", "-"], # =
                  ["-", "-", "-", "-", "-"], # len(Board[0])
                  ["#", "-", "#", "#", "-"], # =
                  ["-", "#", "-", "-", "-"]] # 5 
            # N-rows = len(Board) = 5

    result = solve_puzzle(Board,(0,2),(2,2),"",set()) # -1 for starting at 0
    if result:
        result.sort(key = lambda x:len(x))
        print("|-------------------------------------------------------|")
        print(" Example 1: (a,b) : (1,3) ; (x,y): (3,3)  ")
        print(" -Total Moves: ",len(result[0])-1)
        print(" -Direction(s) of Moves: ",result[0])
        print("  (1,3) →(1,2) → (2,2) → (3,2)→(3,3)")
        print(" ")

    else:
        print(None)

    result = solve_puzzle(Board,(0,0),(4,4),"",set())
    if result:
        result.sort(key = lambda x:len(x))
        print("|-------------------------------------------------------|")
        print(" Example 2: (a,b): (1,1) ; (x,y): (5,5)   ")
        print(" -Total Moves: ",len(result[0])-1)
        print(" -Direction(s) of Moves: ",result[0])
        print("  (1,1) →(2,1)→(3,1)→(3,2)→(3,3)→(3,4)→(3,5)→(4,5)→(5,5)")
        print(" ")
        print("|-------------------------------------------------------|")
        

    else:
        print("|-------------------------------------------------------|")
        print(None)

    # Example 3: (a,b) : (1,1); (x,y): (5,1)
    result = solve_puzzle(Board,(0,0),(4,0),"",set())
    if result:
        result.sort(key = lambda x:len(x))
        print(len(result[0])-1)
        print(result[0])
    else:
        print(None)

if __name__ == "__main__":
    main()

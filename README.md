# Knight's tour problem
Knight tour problem solved by backtrack algorithm. Visualizing with Pygame.

### Output on 8X8 Board
<p align="center">
  <video src="https://github.com/phantomf4321/Knight-tour-problem-pygame/assets/83742735/d185ca1c-045c-4d1c-8d20-336a81781b25" width="500px"></video>
</p>

### Chess board at the end
```
| 0 | | 59 | | 38 | | 33 | | 30 | | 17 | | 8 | | 63 | 
-----------------------------------------------------
| 37 | | 34 | | 31 | | 60 | | 9 | | 62 | | 29 | | 16 | 
-----------------------------------------------------
| 58 | | 1 | | 36 | | 39 | | 32 | | 27 | | 18 | | 7 | 
-----------------------------------------------------
| 35 | | 48 | | 41 | | 26 | | 61 | | 10 | | 15 | | 28 | 
-----------------------------------------------------
| 42 | | 57 | | 2 | | 49 | | 40 | | 23 | | 6 | | 19 | 
-----------------------------------------------------
| 47 | | 50 | | 45 | | 54 | | 25 | | 20 | | 11 | | 14 | 
-----------------------------------------------------
| 56 | | 43 | | 52 | | 3 | | 22 | | 13 | | 24 | | 5 | 
-----------------------------------------------------
| 51 | | 46 | | 55 | | 44 | | 53 | | 4 | | 21 | | 12 | 
-----------------------------------------------------
```
### How to run
```
pip install pygame
python3 main.py
```

### What is Knight's Tour Problem?
Just for a reminder, the knight is a piece in chess that usually looks like a horse and moves in an L-shaped pattern. This means it will first move two squares in one direction and then one square in a perpendicular direction.

The Knight's Tour problem is about finding a sequence of moves for the knight on a chessboard such that it visits every square on the board exactly one time. It is a type of Hamiltonian path problem in graph theory, where the squares represent the vertices and the knight's moves represent the edges of the graph.

This problem has fascinated many mathematicians for centuries, but the solutions they found were very difficult. The simple solution will be to find every conceivable configuration and selecting the best one is one technique to solve this problem. But that will take a load of time.

One popular solution to solve the Knight's tour problem is Warnsdorff's rule, which involves choosing the next move that leads to a square with the fewest available moves. There is also a backtracking approach. 

 But first moving to all that, let's take a quick understanding of the Hamiltonian path problem.


### Hamiltonian Path Problem

The Hamiltonian path problem is a well-known problem in graph theory that asks whether a given graph contains a path that visits every vertex exactly once.


### Knight's Tour Backtracking Algorithm

There are various ways to solve the Knight's Tour Problem. In the programming world, Backtracking can be one answer. You can learn the basics of Backtracking here with some other popular problems.
The backtracking algorithm works by exploring all possible moves for the knight, starting from a given square, and backtracking to try different moves if it reaches a dead end.

Here's the basic outline of the backtracking algorithm to solve the Knight's tour problem:

- Choose a starting square for the knight on the chessboard.
- Mark the starting square as visited.
- For each valid move from the current square, make the move and recursively repeat the process for the new square.
- If all squares on the chessboard have been visited, we have found a solution. Otherwise, undo the last move and try a different move.
- If all moves have been tried from the current square and we have not found a solution, backtrack to the previous square and try a different move from there.
- If we have backtracked to the starting square and tried all possible moves without finding a solution, there is no solution to the problem.
- A path that visits every vertex exactly once is called a Hamiltonian path, and a graph that contains a Hamiltonian path is called a Hamiltonian graph.

#### Check cell (x, y) is not OOB and value is not visited already
```
        def isSafe(x, y):#checked
            # Check cell (x, y) is not OOB and value is not visited already
            if 0 <= x < N and 0 <= y < N and board[x][y] == -1:
                return True
            return False
```

#### Backtrack
```
        def backtrack(cur_x, cur_y, moveCount):
            # 1) Base case: If all moves are done
            if moveCount >= N*N:
                return True

            # 2) Breath: --> Consider all possible moves
            for i in range(8):
                next_x = cur_x + move_x[i]
                next_y = cur_y + move_y[i]

                #print("next x{} and next y{}".format(next_x, next_y))

                # 3) Check if this move can be taken
                if isSafe(next_x, next_y):
                    # 4) Take this move
                    board[next_x][next_y] = moveCount

                    # 5) Check if this move leads to a solution from all recur moves
                    if backtrack(next_x, next_y, moveCount+1):
                        return True

                    # 6) This move didn't work, Backtrack...
                    board[next_x][next_y] = -1

            return False    # No move from all 8 possible worked, so Backtrack previous move and re-try
```
### Time & Space Complexity for Backtracking

The backtracking algorithm used to solve the Knight's Tour problem has an exponential time complexity. The number of possible paths for the knight grows very quickly as the size of the chessboard increases, which means that the time taken to explore all possible paths grows exponentially.

The exact time complexity of the Knight's Tour Backtracking algorithm is O(8^(n^2)), where n is the size of the chessboard. This is because each move has a maximum of 8 possible directions, and we have to explore all possible moves until we find a solution.

The space complexity of the backtracking algorithm is O(n^2), where n is the size of the chessboard. So, we can say that the backtracking algorithm is efficient for smaller chessboards.
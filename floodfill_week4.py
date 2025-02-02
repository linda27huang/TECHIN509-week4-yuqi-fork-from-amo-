#this is the change that yuqi made!
#yuqi checked the code and found there was no bug!
print('amo is cute!')

#!/usr/bin/env python
# coding: utf-8

# In[5]:


from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]
 
board2 = [
    ".........##...........",
    "......###..#####......",
    "......#.....####......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#......#########..",
    "....##############....",  
] 

def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """

    # Implement your code here.
    m = len(input_board)  
    n = len(input_board[0])

    if x >= m or y >= n:
        return []

    output_board = input_board[:]

    def dfs(x_x: int, y_y: int):
        if output_board[x_x][y_y] == old:
            output_board[x_x] = output_board[x_x][:y_y] + new + output_board[x_x][y_y + 1:]

            if x_x < m - 1:  # check the boundary
                dfs(x_x + 1, y_y)

            if y_y < n - 1:
                dfs(x_x, y_y + 1)

            if x_x > 0:
                dfs(x_x - 1, y_y)

            if y_y > 0:
                dfs(x_x, y_y - 1)

        else:
            return

    dfs(x, y)
    return output_board


modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

modified_board2 = flood_fill(input_board=board2, old=".", new="~", x=5, y=12)

for b in modified_board2:
    print(b)

# In[ ]:





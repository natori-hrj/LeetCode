from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def num_to_position(num):
            num -= 1
            row = n - 1 - num // n
            
            if (n - 1 - row) % 2 == 0:
                col = num % n
            else:
                col = n - 1 - num % n
            
            return row, col
        
        def get_destination(num):
            row, col = num_to_position(num)
            if board[row][col] != -1:
                return board[row][col]
            return num
        
        target = n * n
        queue = deque([(1, 0)])
        visited = set([1])
        
        while queue:
            curr_pos, dice_rolls = queue.popleft()
            
            if curr_pos == target:
                return dice_rolls
            
            for dice in range(1, 7):
                next_pos = curr_pos + dice
                
                if next_pos > target:
                    break
                
                final_pos = get_destination(next_pos)
                
                if final_pos not in visited:
                    visited.add(final_pos)
                    queue.append((final_pos, dice_rolls + 1))
        
        return -1
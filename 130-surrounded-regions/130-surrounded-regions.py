class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        stack = []
        marked = set()
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if r in [0, len(board) - 1] or c in [0, len(board[0]) - 1]:
                    if board[r][c] == "O":
                        marked.add((r,c))
                        stack.append((r,c))
        
        for r in [0, len(board) - 1]:
            for c in [0, len(board[0]) - 1]:
                if board[r][c] == "O":
                    marked.add((r,c))
                    stack.append((r,c))
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while stack:
            r, c = stack.pop()
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if row >= 0 and row < len(board) and col >= 0 and col < len(board[0]):
                    if board[row][col] == "O" and (row, col) not in marked:
                        marked.add((row, col))
                        stack.append((row, col))
                        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O" and (r, c) not in marked:
                    board[r][c] = "X"
                        
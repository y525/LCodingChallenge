import collections
class Solution:
    def NumIsland(self, grid):
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        island = 0
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(row, col):
            q = collections.deque()
            visited.add((row, col))
            q.append((row, col))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(rows) and \
                       c in range(cols) and \
                       (r, c) not in visited and \
                       grid[r][c] == "1":
                        q.append((r, c))
                        visited.add((r, c))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    island += 1
                    bfs(row, col)

        return island
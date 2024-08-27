# breath-first-search
class Solution:
    def hasPath(self, maze, start, destination):
        if start == destination:
            return True
        rows, cols = len(maze), len(maze[0])
        visited = [[0]* cols for _ in range(rows)]
        q = collections.deque()
        q.append((start[0], start[1]))
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            cur = q.popleft()
            if cur[0] == destination[0] and cur[1] == destination[1]:
                return True
            for dr, dc in directions:
                row, col = cur[0]+dr, cur[1]+dc
                while row in range(rows) and \
                      col in range(cols) and \
                      maze[row][col] == 0:
                      row += dr
                      col += dc
                row_to_x = row-dr
                col_to_y = col-dc
                if (row_to_x, col_to_y) not in visited:
                    visited.add(row_to_x, col_to_y)
                    q.append((row_to_x, col_to_y))
        return False



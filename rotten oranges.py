class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q, fresh = deque(), 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        if not fresh: return 0

        days, rot = 0, 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr,dc in [(0,-1),(-1,0),(0,1),(1,0)]:
                    if (0 <= r+dr < rows) and (0 <= c+dc < cols):
                        if grid[r+dr][c+dc] == 1:
                            rot += 1
                            grid[r+dr][c+dc] = 2
                            q.append((r+dr,c+dc))
            days += 1

        if fresh > rot:
            return -1
        return days-1        

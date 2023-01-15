from typing import List, Tuple


class Solution:
    def has_path(self, maze: List[List[int]], start: Tuple[int, int], destination: Tuple[int, int]) -> bool:
        maze = self.wrap_maze(maze)
        start = (start[0] + 1, start[1] + 1)
        destination = (destination[0] + 1, destination[1] + 1)

        visited = [[0] * len(maze[0]) for _ in range(len(maze))]
        return self.dfs(maze, start[0], start[1], destination, visited)

    def dfs(self, maze, i, j, destination, visited):
        if (i, j) == destination:
            return True

        visited[i][j] = 1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for direction in directions:
            x, y = i, j
            while maze[x][y] == 0:
                x = x + direction[0]
                y = y + direction[1]
            x = x - direction[0]
            y = y - direction[1]

            if not visited[x][y]:
                if self.dfs(maze, x, y, destination, visited):
                    return True

        return False

    def wrap_maze(self, maze: List[List[int]]) -> List[List[int]]:
        maze = [[1] + row + [1] for row in maze]
        maze = [[1] * len(maze[0])] + maze + [[1] * len(maze[0])]
        return maze


if __name__ == "__main__":
    # fmt: off
    maze_ = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]
    ]
    # fmt: on
    example1 = {
        "maze": maze_,
        "start": (0, 4),
        "destination": (4, 4),
    }
    print(Solution().has_path(**example1), "(should be True)")

    example2 = {
        "maze": maze_,
        "start": (0, 4),
        "destination": (3, 2),
    }
    print(Solution().has_path(**example2), "(should be False)")



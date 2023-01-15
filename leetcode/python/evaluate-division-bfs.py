from typing import List
from collections import defaultdict, deque


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # graph
        divisions = defaultdict(dict)
        for (n, d), value in zip(equations, values):
            divisions[n][d] = value
            divisions[d][n] = 1.0 / value

        def bfs(start, end):
            queue = deque()
            seen = set()

            if start in divisions:
                queue.append((start, 1))  # from s to this node, weight is 1
                seen.add(start)

            while queue:
                nxt, weight = queue.popleft()
                if nxt == end:
                    return weight
                for adjacent, adjacent_weight in divisions[nxt].items():
                    if adjacent not in seen:
                        queue.append((adjacent, weight * adjacent_weight))
                        seen.add(adjacent)
            return -1

        answers = []
        for numerator, denominator in queries:
            answers.append(bfs(numerator, denominator))

        return answers

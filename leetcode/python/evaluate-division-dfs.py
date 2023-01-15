from typing import List
from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        divisions = defaultdict(dict)
        for (n, d), value in zip(equations, values):
            divisions[n][d] = value
            divisions[d][n] = 1.0 / value

        def dfs(visited, result, numerator, denominator):

            if divisions[numerator].get(denominator):
                return result * divisions[numerator][denominator]

            visited.add(numerator)

            for new_denominator in divisions[numerator]:
                if new_denominator not in visited:
                    value = dfs(visited, result * divisions[numerator][new_denominator], new_denominator, denominator)
                    if value > 0:
                        return value

            return -1

        answers = []
        for query in queries:
            answers.append(dfs(set(), 1.0, query[0], query[1]))

        return answers

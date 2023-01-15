from collections import defaultdict

class Solution:

    def maxDistanceFromNode(self, n, node_edges, node) -> Tuple[int, int]:
        self.maxD = 0
        self.maxNode = None

        self.visited = [0 for x in range(n)]
        
        def DFS(node, l_to_root):
            self.visited[node] = 1

            if l_to_root > self.maxD:
                
                self.maxD = l_to_root
                self.maxNode = node
            
            for child in node_edges[node]:
                if self.visited[child] == 1:
                    continue
                DFS(child, l_to_root+1)

        DFS(node, 0)
        return self.maxD, self.maxNode

    def pathNodes(self, n, node_edges, x: int, y: int) -> List[int]:
        self.visited = [0 for x in range(n)]

        def DFS(x, y, stack):
            if x == y:
                return stack + [x]

            self.visited[x] = 1
            for child in node_edges[x]:
                if self.visited[child] == 1:
                    continue
                result = DFS(child, y, stack + [x])

                if result:
                    return result

        return DFS(x, y, [])

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n < 3:
            return list(range(n))

        node_edges = defaultdict(list)

        for (v1, v2) in edges:
            node_edges[v1].append(v2)
            node_edges[v2].append(v1)

        _, diametre_v1 = self.maxDistanceFromNode(n, node_edges, 0)


        _, diametre_v2 = self.maxDistanceFromNode(n, node_edges, diametre_v1)


        stack = self.pathNodes(n, node_edges, diametre_v1, diametre_v2)
        l = len(stack)
        print(stack, l//2, l//2+2)
        if l % 2 == 0:
            return stack[l//2 - 1: l//2 + 1]
        else:
            return [stack[l//2]]
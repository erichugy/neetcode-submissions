from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False

        adj_list = defaultdict(set)
        for node, dest in edges:
            adj_list[node].add(dest)
            adj_list[dest].add(node)

        # dfs the rest for acyclic and 
        path = set()
        def dfs(root, parent):
            if root in path: # if cycle
                return False
            
            path.add(root)
            for outgoing in adj_list[root]:
                if outgoing == parent:
                    continue
                if not dfs(outgoing, root):
                    return False
            return True

        return dfs(0,-1) and len(path) == n

        


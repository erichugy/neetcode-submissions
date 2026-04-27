from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0 and n == 1:
            return True


        adj_list = defaultdict(set)
        nodes = set()
        for node, dest in edges:
            # print(n)
            # print(dest)
            # if n == dest: 
            #     return False
            adj_list[node].add(dest)
            adj_list[dest].add(node)
            nodes.add(node)
            nodes.add(dest)

        # dfs the rest for acyclic and 
        path = set()
        edges_taken = set()
        def dfs(root):
            if root in path: # if cycle
                return False
            
            path.add(root)
            for outgoing in adj_list[root]:
                edge = (root, outgoing) if root < outgoing else (outgoing, root)
                if edge in edges_taken: continue
                edges_taken.add(edge)

                if not dfs(outgoing):
                    return False
            
            return True

        return dfs(edges[0][0]) and len(path) == n

        


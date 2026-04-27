class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        # nodes = adj.keys()
        counter = 0
        seen = set()

        for root in adj.keys():
            if root not in seen:
                #bfs
                q = [root]
                while q:
                    curr = q.pop(0)
                    if curr in seen: continue
                    seen.add(curr)

                    for next_node in adj[curr]:
                        q.append(next_node)
                counter += 1
        
        return counter + (n - len(seen))

            




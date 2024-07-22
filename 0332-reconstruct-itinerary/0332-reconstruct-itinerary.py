class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = {}
        for src, dest in tickets:
            cur_dests = adj_list.get(src, [])
            cur_dests.append(dest)
            adj_list[src] = cur_dests
        
        for src, dests in adj_list.items():
            new_dests = deque(sorted(dests))
            adj_list[src] = new_dests
        
        res = []
        def dfs(airport):
            cur_dests = adj_list.get(airport, deque())
            while cur_dests:
                nex = cur_dests.popleft()
                dfs(nex)
            res.append(airport)
        dfs("JFK")
        return res[::-1]



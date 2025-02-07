class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_counts = defaultdict(int)
        colors = defaultdict(int)
        result = []

        for idx, new_color in queries:
            cur_color = colors[idx]
            if cur_color:
                color_counts[cur_color] -= 1
                if not color_counts[cur_color]:
                    del color_counts[cur_color]
            
            color_counts[new_color] += 1
            colors[idx] = new_color
            result.append(len(color_counts))
        
        return result


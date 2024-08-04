class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj_list = defaultdict(list)
        for emails in accounts:
            name = emails[0]
            first_email = emails[1]

            for idx in range(2, len(emails)):
                email = emails[idx]
                adj_list[email].append(first_email)
                adj_list[first_email].append(email)
        
        result = []
        visited = set()
        for emails in accounts:
            first_email = emails[1]
            name = emails[0]
            if first_email not in visited:
                visited.add(first_email)
                cur_result = [""]
                stack = [first_email]
                while stack:
                    cur_email = stack.pop()
                    cur_result.append(cur_email)
                    neighbors = adj_list[cur_email]
                    for neighbor in neighbors:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)
                cur_result.sort()
                cur_result[0] = name
                result.append(cur_result)
        
        return result



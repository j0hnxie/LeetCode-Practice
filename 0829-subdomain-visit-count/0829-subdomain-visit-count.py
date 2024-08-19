class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = defaultdict(int)
        for query in cpdomains:
            count, domain = query.split(" ")
            sub_domains = domain.split(".")
            count = int(count)

            n = len(sub_domains)
            cur = ""
            for idx in range(n - 1, -1, -1):
                cur = sub_domains[idx] + "." + cur
                domains[cur] += count
            
        result = [str(value) + " " + key[:-1] for key, value in domains.items()]
        return result

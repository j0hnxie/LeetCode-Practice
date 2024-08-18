class Solution:
    def nthUglyNumber(self, n: int) -> int:
        generators = [2, 3, 5]
        factors = [deque([2]), deque([3]), deque([5])]
        visited = set([1, 2, 3, 5])

        res = [1]
        pq = [(2, 0), (3, 1), (5, 2)]
        heapq.heapify(pq)
        while len(res) < n:
            value, idx = heapq.heappop(pq)
            res.append(value)

            if value * 2 not in visited:
                factors[0].append(value * 2)
                visited.add(value * 2)

            if value * 3 not in visited:
                factors[1].append(value * 3)
                visited.add(value * 3)

            if value * 5 not in visited:
                factors[2].append(value * 5)
                visited.add(value * 5)

            factors[idx].popleft()
            heapq.heappush(pq, (factors[idx][0], idx))

        return res[-1]
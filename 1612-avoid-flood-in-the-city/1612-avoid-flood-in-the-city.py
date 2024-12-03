class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [1] * n
        full_set = {}
        dry_queue = []

        for idx, lake in enumerate(rains):
            if lake > 0:
                if lake in full_set:
                    if len(dry_queue) == 0 or dry_queue[-1] < full_set[lake]:
                        return []
                    else:
                        dry_idx = bisect.bisect_left(dry_queue, full_set[lake])
                        ans_idx = dry_queue[dry_idx]
                        ans[ans_idx] = lake
                        dry_queue.pop(dry_idx)
                full_set[lake] = idx
                ans[idx] = -1
            else:
                dry_queue.append(idx)

        return ans

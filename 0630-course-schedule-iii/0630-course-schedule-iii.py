class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses, key=lambda x: x[1])
        
        pq = []
        curTime = 0
        for dur, last in courses:
            if curTime + dur > last:
                if pq and dur < -pq[0]:
                    curTime += pq[0] + dur
                    heapq.heappushpop(pq, -dur)
            else:
                heapq.heappush(pq, -dur)
                curTime += dur
            # print(pq)
            # print(pq)
                
        return len(pq)
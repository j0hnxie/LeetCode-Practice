class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        num_counts = {} 

        for answer in answers:
            temp_count = num_counts.get(answer + 1, 0) + 1
            num_counts[answer + 1] = temp_count
        
        res = 0
        print(num_counts)
        for num, count in num_counts.items():
            groups = math.ceil(count / num)
            res += groups * num
            # res += count % num
        
        return res
        


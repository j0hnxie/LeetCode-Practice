class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mixed_list = [(cur_position, cur_speed) for cur_position, cur_speed in zip(position, speed)]
        sorted_list = sorted(mixed_list, reverse=True)

        fleets = 0
        last_end = float('-inf')
        for position, speed in sorted_list:
            dist = target - position
            hrs = dist / speed

            if hrs > last_end:
                fleets += 1
                last_end = max(last_end, hrs)
        
        return fleets
        
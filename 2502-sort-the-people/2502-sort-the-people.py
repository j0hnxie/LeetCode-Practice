class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sort_list = sorted([(heights[idx], names[idx]) for idx in range(len(names))], reverse=True)
        return [person[1] for person in sort_list]
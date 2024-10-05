class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [""] * n
        for idx in range(1, n + 1):
            if idx % 3 == 0 and idx % 5 == 0:
                answer[idx - 1] = "FizzBuzz"
            elif idx % 3 == 0:
                answer[idx - 1] = "Fizz"
            elif idx % 5 == 0:
                answer[idx - 1] = "Buzz"
            else:
                answer[idx - 1] = str(idx)
        return answer
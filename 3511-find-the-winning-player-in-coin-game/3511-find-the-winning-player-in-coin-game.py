class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        y //= 4
        rounds = min(x, y)
        return "Alice" if rounds % 2 else "Bob"
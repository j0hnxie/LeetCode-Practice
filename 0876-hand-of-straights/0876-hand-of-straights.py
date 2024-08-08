class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize:
            return False

        if groupSize == 1:
            return True

        counter = defaultdict(int)
        for card in hand:
            counter[card] += 1
        
        cards = sorted([(card, count) for card, count in counter.items()])
        n = len(cards)
        for idx in range(n - groupSize + 1):
            (card, count) = cards[idx]
            if not count:
                continue

            for offset in range(groupSize):
                new_card = (cards[idx + offset][0], cards[idx + offset][1] - count)
                cards[idx + offset] = new_card
                if cards[idx + offset][1] < 0 or cards[idx + offset][0] != card + offset:
                    return False

        for offset in range(groupSize):
            if cards[-offset][1]:
                return False

        return True

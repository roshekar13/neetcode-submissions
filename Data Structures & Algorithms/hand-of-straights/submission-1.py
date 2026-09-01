from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if not hand or groupSize == 0 or len(hand) % groupSize != 0: return False

        my_dict = Counter(hand)
        for card in sorted(my_dict):
            count = my_dict[card]
            # skip dict items already accounted for
            if count == 0: continue
            target = card
            for i in range(groupSize):
                # check if enough left to make groups
                if my_dict[target] < count: return False
                # decrement count, increment target
                my_dict[target] -= count
                target += 1

        return True



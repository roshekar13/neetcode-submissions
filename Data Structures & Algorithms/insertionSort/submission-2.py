# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        length = len(pairs)
        states = []
        for i in range(length):
            j = i - 1
            while j >= 0 and pairs[j].key > pairs[j+1].key:
                pairs[j],pairs[j+1] = pairs[j+1],pairs[j]
                j -= 1
            states.append(pairs.copy())
        return states
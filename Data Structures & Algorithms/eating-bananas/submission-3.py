class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def get_time(array,rate):
            total = 0
            for i in array:
                buff=0
                if i%rate != 0:
                    buff = 1
                total += (i//rate + buff)
            return total

        low = 1
        high = max(piles)
        res = high

        while low <= high:
            mid = (low+high)//2
            print(mid)
            time = get_time(piles,mid)
            print(time)
            if time <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res
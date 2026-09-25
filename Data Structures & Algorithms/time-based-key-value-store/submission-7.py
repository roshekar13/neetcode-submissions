class TimeMap:

    def __init__(self):
        self.cache = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key] = self.cache.get(key,[])+[(timestamp,value)]
        #print('foo')
        #print(self.cache)
        

    def get(self, key: str, timestamp: int) -> str:
        #print(self.cache,timestamp)
        # bin search through array associated with key
        if key not in self.cache:
            #print('this')
            return ""
        target = self.cache[key]
        if target[0][0] > timestamp: return ""
        if target[-1][0] < timestamp: return target[-1][1]
        if len(target) == 1: return target[0][1] if target[0][0] <= timestamp else ""

        low,high = 0,len(target)
        while True:
            mid = (low+high)//2
            #print(low,mid,high)
            if target[mid][0] == timestamp:
                #print(target[mid],timestamp)
                #print(mid,'this')
                return target[mid][1]
            elif target[mid][0] > timestamp:
                high = mid
                if not(low<high): return target[mid-1][1]
            else:
                low = mid+1
                if not (low<high): return target[mid][1]
        #print(low,mid,high)
        #print(mid,target[mid],timestamp
        return -1
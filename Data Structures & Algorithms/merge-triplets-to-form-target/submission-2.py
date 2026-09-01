class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if not triplets: return False
        if target in triplets: return True

        # painpoint: smallest integer from the target
        #minIdx = 0
        #for i in range(len(target)):
        #    if target[i] < target[minIdx]: minIdx = i
        
        #triplets = sorted(triplets, key=lambda x: x[minIdx])

        x3,y3,z3 = 0,0,0
        for trips in triplets:
            # ignore if overshoots target on any trips
            if trips[0] > target[0] or trips[1] > target[1] or trips[2] > target[2]: continue

            # update
            x3 = max(x3, trips[0])
            y3 = max(y3, trips[1])
            z3 = max(z3, trips[2])
        
        return [x3,y3,z3] == target

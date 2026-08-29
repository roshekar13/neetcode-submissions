class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = []
        for i in range(len(position)): combined.append([position[i],speed[i]])

        combined.sort()
        
        max_time = float('-inf')
        fleets = 0
        while combined:
            latest = combined.pop()
            time = (target-latest[0])/latest[1]
            if time > max_time:
                fleets += 1
                max_time = time

        return fleets

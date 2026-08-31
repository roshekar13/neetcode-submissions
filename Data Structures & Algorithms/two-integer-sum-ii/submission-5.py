class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        one = 0
        two = len(numbers) - 1
        while numbers[one] + numbers[two] != target and one < two:
            if numbers[one] + numbers[two] > target:
                two -= 1
            else:
                one += 1
        if numbers[one] + numbers[two] == target:
            return [one+1,two+1]
        else:
            return[0,0] # Should not reach if valid solution is present
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arranged = []
        unique_set = set()
        for num in nums:
            if num not in unique_set:
                unique_set.add(num)
        unique_nums = list(unique_set)

        max_count = 0
        for num in unique_nums:
            if num - 1 not in unique_set:
                count = 1
                #can mark the beginning of a seq
                flag = True
                while flag:
                    if num + 1 in unique_set:
                        count += 1
                        num += 1
                    else:
                        flag = False
                if count > max_count:
                    max_count = count
        
        return max_count
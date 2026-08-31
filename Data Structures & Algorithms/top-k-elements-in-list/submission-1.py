class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for i in nums:
            if i not in nums_dict:
                nums_dict[i] = 1
            else:
                nums_dict[i] += 1
        return_list = []
        while k != 0:
            max_num = 0
            max_count = 0
            for key,value in nums_dict.items():
                if value > max_count and key not in return_list:
                    max_num = key
                    max_count = value
            return_list.append(max_num)
            k -= 1
        return return_list   
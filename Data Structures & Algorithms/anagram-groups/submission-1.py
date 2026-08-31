class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def make_dict(word: str) -> set:
            curr_dict = {}
            for i in range(len(word)):
                if word[i] not in curr_dict:
                    curr_dict[word[i]] = 1
                else:
                    curr_dict[word[i]] += 1
            return curr_dict

        set_of_sets = set()

        for i in strs:
            curr_dict = frozenset(make_dict(i).items())
            if curr_dict not in set_of_sets:
                set_of_sets.add(curr_dict)
        
        list_of_lists = []
        for d in set_of_sets:
            curr_list = []
            for word in strs:
                if frozenset(make_dict(word).items()) == d:
                    curr_list.append(word)
            list_of_lists.append(curr_list)
        
        return list_of_lists

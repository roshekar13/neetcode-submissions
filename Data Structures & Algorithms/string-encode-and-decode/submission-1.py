class Solution:

    def encode(self, strs: List[str]) -> str:
        gaps = []
        encoded_str = ""
        for string in strs:
            encoded_str = encoded_str + string + "_%_"
        return encoded_str   

    def decode(self, s: str) -> List[str]:
        org_list = []
        while s != "":
            for i in range(len(s)):
                if s[i:i+3] == "_%_":
                    org_list.append(s[:i])
                    s = s[i+3:]
                    break
        return org_list

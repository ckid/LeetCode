class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_length, start, char_dict = 0, 0, {}
        for idx, char in enumerate(s, 1):
            if char_dict.get(char, -1) >= start:
                start = char_dict[char]
            char_dict[char] = idx
            max_length = max(max_length, idx - start)
        return max_length
    # def lengthOfLongestSubstring(self, s):
    #     """
    #     寻找最长不重复字串
    #     :type s: str
    #     :rtype: int
    #     """
    #     subStr = {}
    #     maxLen = 0
    #     for i, v in enumerate(s):
    #         if v in subStr.keys():
    #             self.delValuetoItem(subStr, v)
    #         subStr[v] = i
    #         if subStr.__len__() > maxLen:
    #             maxLen = subStr.__len__()
    #             print (subStr)
    #     return maxLen
    #
    # def delValuetoItem(self,dic, value):
    #     index =dic[value]
    #     keySet = set(dic.keys())
    #     for k in keySet:
    #         if dic[k] <= index:
    #             dic.pop(k)

# class Dict(dict):
#     def delValuetoItem(self, value):
#         index =self[value]
#         keySet = set(self.keys())
#         for k in keySet:
#             if self[k] <= index:
#                 self.pop(k)

if __name__ =="__main__":
    s = Solution()
    a =s.lengthOfLongestSubstring("sjdkjfsklajhkgjhjkhsajkldhsjkahgjkrhekuhadskhlakjh")
    print(a)

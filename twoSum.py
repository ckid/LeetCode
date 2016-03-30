from numpy import *
from numpy.random.mtrand import random_integers


class Solution(object):
    @staticmethod
    def twoSum(nums, target):
        # 如果使用暴力法 复杂度书n^2,会报超时
        """
        本例使用空间换时间的方法
        :param nums:
        :param target:
        :return:
        """
        result_dict = {}
        for i, item in enumerate(nums):
            sum_key = target - item
            if sum_key in result_dict.keys():
                return result_dict[sum_key], i
            else:
                result_dict[item] = i


if __name__ == "__main__":
    data_to_test = list(random_integers(1, 100, 1000))
    print(data_to_test)
    print(Solution.twoSum(data_to_test, 121))

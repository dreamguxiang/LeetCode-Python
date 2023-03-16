from typing import List
# Description: 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for index, value in enumerate(nums):
            complement = hash_table.get(target - value, None)
            if complement is not None:
                return [index, complement]
            hash_table[value] = index



def main():
    test = Solution()
    result = test.twoSum([2,7,11,15],9)
    print(result)


if __name__ == '__main__':
    main()




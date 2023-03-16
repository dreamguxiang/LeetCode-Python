from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 两个数组合并成一个数组
        nums = nums1 + nums2
        nums.sort()
        
        if len(nums) % 2 == 0:
            # 因为len(nums)是奇数，所以len(nums)//2是中间的数，len(nums)//2 - 1是中间的前一个数
            return (nums[len(nums)//2] + nums[len(nums)//2 - 1]) / 2
        else:
            return nums[len(nums)//2]


def main():
    test = Solution()
    result1 = test.findMedianSortedArrays([1,3],[2])
    print(result1)
    result2 = test.findMedianSortedArrays([1,3],[2,4])
    print(result2)


if __name__ == '__main__':
    main()


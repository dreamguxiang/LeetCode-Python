
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_length = 0
        d = []

        for c in s:
            if c in d:
                # 如果c在d中，那么就把d中c之前的元素全部删掉
                d = d[d.index(c)+1:]
            # 把c加到d的最后
            d.append(c)
            # 如果d的长度大于max_length，那么就把d的长度赋值给max_length
            max_length = max(max_length, len(d))

        return max_length



def main():
    test = Solution()
    result1 = test.lengthOfLongestSubstring("abcabcbb")
    print(result1)

    result2 = test.lengthOfLongestSubstring("bbbbc")
    print(result2)


if __name__ == '__main__':
    main()


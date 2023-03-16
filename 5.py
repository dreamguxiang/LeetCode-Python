

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(s: str, left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''
        for i in range(len(s) - 1):
            result = max(result, expandAroundCenter(s, i, i + 1), expandAroundCenter(s, i, i + 2), key=len)
        return result
        




def main():
    test = Solution()
    result1 = test.longestPalindrome("babad")
    print(result1)
    result2 = test.longestPalindrome("cbbd")
    print(result2)

if __name__ == '__main__':
    main()


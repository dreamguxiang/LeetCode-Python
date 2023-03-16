from functools import cache

#参考https://leetcode.cn/problems/regular-expression-matching/solution/by-annfrost-sf5b/

class Solution:
    def isMatch(self, s, p):
        
        def isEndOfPattern(j):
            return j == len(p)

        def isEndOfString(i):
            return i == len(s)

        def isMatched(i, j):
            return i < len(s) and (s[i] == p[j] or p[j] == '.')

        def isStar(j):
            return j + 1 < len(p) and p[j + 1] == '*'

        @cache
        def DFS(i, j):
            if isEndOfPattern(j):
                return isEndOfString(i)
            firstMatch = isMatched(i, j)
            if isStar(j):
                return DFS(i, j + 2) or (firstMatch and DFS(i + 1, j))
            return firstMatch and DFS(i + 1, j + 1)

        return DFS(0, 0)



def main():
    test = Solution()
    result1 = test.isMatch("aa","a*")
    print(result1)

if __name__ == '__main__':
    main()

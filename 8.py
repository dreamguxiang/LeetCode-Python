#导入正则
import re

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        num_re = re.compile(r'^[\+\-]?\d+')
        num = num_re.findall(s)
        num = int(*num)
        return max(min(num,2147483647),-2147483648) 


def main():
    test = Solution()
    result = test.myAtoi("42")
    print(result)


if __name__ == '__main__':
    main()


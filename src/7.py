class Solution:
    def reverse(self, x: int) -> int:
        result = ''
        if x < 0:    
            x = -x
            result = '-'
        xstr = str(x)
        l = ['']
        l.append(xstr[::-1])
        num = int(result + ''.join(l))
        return num if -2147483648 < num < 2147483647 else 0


def main():
    test = Solution()
    result = test.reverse(123)
    print(result)


if __name__ == '__main__':
    main()


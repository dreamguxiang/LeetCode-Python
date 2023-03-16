class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = [''] * numRows
        row = 0
        step = 1
        for i in s:
            result[row] += i
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        return ''.join(result)


def main():
    test = Solution()
    result = test.convert("PAYPALISHIRING", 3)
    print(result)

if __name__ == '__main__':
    main()


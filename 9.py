class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0) :
            return False
        
        reverse_x = 0          
        while x > reverse_x:                  
            reverse_x = reverse_x * 10 + x % 10
            x = x // 10

        return x == reverse_x or x == reverse_x // 10



def main():
    test = Solution()
    result1 = test.isPalindrome(121)
    print(result1)
    result2 = test.isPalindrome(-121)
    print(result2)

if __name__ == '__main__':
    main()


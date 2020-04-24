
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        xr = str(x)
        return xr[::-1] == xr

class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_str = str(x)
        n = len(x_str)
        if n % 2 == 0:
            str1 = x_str[:n//2]
            str2 = x_str[-1:n//2-1:-1]
            if str1 == str2:
                return True
            else:
                return False
        else:
            str1 = x_str[:(n-1)//2]
            str2 = x_str[-1:(n-1)//2:-1]
            if str1 == str2:
                return True
            else:
                return False

nums = 1234554321
t = Solution1()
print(t.isPalindrome(nums))
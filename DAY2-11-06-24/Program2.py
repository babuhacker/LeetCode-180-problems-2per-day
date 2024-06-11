# Reverse Integer



class Solution:
    def reverse(self, x: int) -> int:
        # Integer.MAX_VALUE =  2147483647 (end with 7)
        # Integer>MIN_VALUE = -2147483648 (end with 8)

        MIN = -2147483648 # -2^31
        MAX =  2147483647 # 2^31 -1

        result = 0
        while x:
            digit = int(math.fmod(x, 10)) # (python dumb) -1 % 10 = 9
            x = int(x / 10)               # (python dumb) -1 // 10 = -1

            if (result > MAX // 10 or
                (result == MAX // 10 and digit >= MAX % 10)):
                return 0
            if (result < MIN // 10 or
                (result == MIN // 10 and digit <= MIN % 10)):
                return 0
            result = (result * 10) + digit
        return result

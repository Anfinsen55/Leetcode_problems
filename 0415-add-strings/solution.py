class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000)
        n1=int (num1)
        n2=int (num2)
        sum1=n1 + n2
        return str(sum1)

class Solution:
    def romanToInt(self, s: str) -> int:
            roman_int_values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
            roman_val = 0
            val = 0
            s=s[::-1]
            for i in s:
                if(val<=roman_int_values[i]):
                    roman_val += roman_int_values[i]
                else:
                    roman_val -= roman_int_values[i]
                val = roman_int_values[i]
            return roman_val

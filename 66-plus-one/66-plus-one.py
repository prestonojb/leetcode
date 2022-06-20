class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        for i in range(length-1, -1, -1):
            num = digits[i] + 1
            if num > 9:
                digits[i] = 0
                if i == 0:
                    digits = [1] + digits
            else:
                digits[i] += 1
                break
                
        return digits
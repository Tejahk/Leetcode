class Solution(object):
    def fizzBuzz(self, n):
        sas = []
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                sas.append("FizzBuzz")
            elif i%3==0:
                sas.append("Fizz")
            elif i%5==0:
                sas.append("Buzz")
            else:
                sas.append(str(i))
        return sas
        """
        :type n: int
        :rtype: List[str]
        """
        
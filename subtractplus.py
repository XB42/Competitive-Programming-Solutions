class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=0
        p=1
        while True:
            if n == 0:
                break
            ld = n % 10
            n/=10
            s+=ld
            p*=ld
        return p-s
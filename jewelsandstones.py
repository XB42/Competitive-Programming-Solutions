class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        ctr = 0
        for j in J:
            for i in range(len(S)):
                if j in S[i:i+1]:
                    ctr-=-1;
        return ctr;
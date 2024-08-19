word1 = "abc"
word2 = "pqr"
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged=[]
        merg=[]
        #merge=;
        for i,j in zip(word1,word2):
            merged.append(i+j)
        for n in merged:
            merg.append(n)
        for m in merged:
            merge = ''.join(merged)
        return merge
        if len(word1) > len(word2):
            merge += word1[len(word2):]
        elif len(word2) > len(word1):
            merge += word2[len(word1):]     
    print(word1,word2)
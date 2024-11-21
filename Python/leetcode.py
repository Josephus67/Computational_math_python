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

    #leetcode today
    class Solution(object):
        def findMedianSortedArrays(self, nums1, nums2):
            """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: float
            """
            # Combine the two lists
            med_set = nums1 + nums2
            med_set.sort()  
            n = len(med_set)
            
            # Check if the total number of elements is even or odd
            if n % 2 == 0:  # Even number of elements
                mid1 = med_set[n // 2 - 1]  # First middle element
                mid2 = med_set[n // 2]      # Second middle element
                median = (mid1 + mid2) / 2    # Average of the two middle elements
            else:  # Odd number of elements
                median = med_set[n // 2]      # Middle element
            
            return median  # Return the median

# Example usage
solution = Solution()
nums1 = [1, 3]
nums2 = [2]
print(solution.findMedianSortedArrays(nums1, nums2))  # Output: 2.0
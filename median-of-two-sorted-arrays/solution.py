class Solution:
    def calMed(self, nums):
        l =len(nums)

        if l%2 == 0:
            return (nums[l//2] + nums[(l//2)-1])/2
        else:
            return nums[l//2]


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) == 0:
            return self.calMed(nums2)
        if len(nums2) == 0:
            return self.calMed(nums1)
        
        l1,l2 = len(nums1), len(nums2)
        n = (l1+l2)//2
        temp=[]
        i,j=0,0
        while n>=0:
            
            if i<l1 and j<l2:
                if nums1[i] <= nums2[j]:
                    temp.append(nums1[i])
                    i +=1 
                else:
                    temp.append(nums2[j])
                    j +=1
            elif i>=l1:
                temp.append(nums2[j])
                j +=1
            else:
                temp.append(nums1[i])
                i +=1
            n -=1

        n = l1+l2
        if n%2 ==  0:
            return (temp[-1] + temp[-2])/2
        else:
            return temp[-1]
        
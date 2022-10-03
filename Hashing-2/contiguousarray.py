class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        #declaring a hashmap
        hashmap={0:-1}
        maxlen=0
        #initialize a varibale to zero
        rSum=0
        
        
        #iterate through the array values
        for i in range(len(nums)):
            #if the value in nums is zero
            if nums[i]==0:
                #then return the -1
                rSum-=1
            else:
                #if the value in nums is 1 then add 1 to running sum 
                rSum+=1
                
            if rSum not in hashmap:
                #adding the index as key id it is not in hashmap
                hashmap[rSum]=i
            
           #if it is already there 
            else:
                #returning the max length between two previous and current value
                maxlen=max(maxlen,i-hashmap[rSum])
                
        return maxlen   
        
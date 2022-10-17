#TC:O(n) 
#SC:O(n)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        #initiawlize a hashset
        hset=set()
        
        #initialize a count variable to zero
        count=0
        
        
        #iterate for every character in string
        for ch in s:
            #if the value is first encountered
            if ch not in hset:
                #adding the ch to hset
                hset.add(ch)
             
            #if the character is already there
            else:
                #removing from the hashset 
                hset.remove(ch)
                #counting the value to two everytime it is removed
                count+=2

            #if the hashset is not empty then ther is atleast one odd vale character we can use only one character of this at the middle of palindrome    
        if len(hset)!=0:
            count+=1
            
     #if hashset is empty then return the coubt value as it is
        return count

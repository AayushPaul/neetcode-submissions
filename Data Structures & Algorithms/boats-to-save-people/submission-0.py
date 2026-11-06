class Solution:
    # Time: 9:54 - 
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #U: Return min number of boats to carry every person 
            # people[i] is the weight of the ith person 
            # Each boat can carry a max weight of limit 
        
        #M/P: Two Pointers 

        #I: 
        l, r = 0, len(people) - 1
        count = 0 
        sortedArr = sorted(people) 

        while l <= r: 
            if l < r and sortedArr[l] + sortedArr[r] <= limit:
                l += 1
            
            r -= 1
            count += 1

        return count

        #R: people = [1, 3, 2, 3, 2], limit = 3
            # sortedArr = [1, 2, 2, 3, 3]
            # count = 4

        #E: Time: O(nlogn), Space: O(1)
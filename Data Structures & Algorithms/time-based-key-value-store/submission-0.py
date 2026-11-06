class TimeMap:

    def __init__(self):
        self.keyValues = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        #U: Stores the key "key" with the value at the given timestamp 

        #P: Use normal hashmap operations 

        #I: 
        if key not in self.keyValues: 
            self.keyValues[key] = []

        self.keyValues[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        #U: Returns the most recent value of key if set was previously called and most recent timestamp 
        # for that key is <= the given timestamp 

        #P: Check the hashmap for certain conditions 
            # If there are no values for the corresponding key, return ""

            # Returns the value if set was called on the key AND most recent timestamp 
            # for that key is <= the given timestamp 
                # Can be implemented with binary search 
        
        #I: 
        result = ""
        values = self.keyValues.get(key, []) #List of values and timestamps for the key 
        #keyValues = {"alice": ["happy", 1], ["happy", 3]}, values = [["happy", 1], ["happy", 3]]

        left, right = 0, len(values) - 1

        while left <= right: 
            mid = (left + right) // 2

            if values[mid][1] <= timestamp: 
                result = values[mid][0]
                left = mid + 1
            else: 
                right = mid - 1 
        
        return result
    
    #E: 
    #Time for set: O(1), Time for get: O(logn), Space: O(m * n) where m = #keys and n = #subarrays/values
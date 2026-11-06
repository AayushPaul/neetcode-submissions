class TimeMap:
    # Time: 4:29 - 6:04 
    def __init__(self):
       self.keyValues = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyValues: 
            self.keyValues[key] = [] 

        self.keyValues[key].append((timestamp, value)) 

    def get(self, key: str, timestamp: int) -> str:
        #U: Return most recent value of key if: 
            # set was previously called on it 
            # prev_timestamp <= given timestamp 

            # If there are no values, program returns ""
        
        #M/P: timestamp as left ptr, prev_timestamp as right ptr 
            # (assuming most recent timestamp > given timestamp at first)

        #I: 
        if key not in self.keyValues: 
            return ""

        values = self.keyValues[key]
        left_timestamp, right_timestamp = 0, len(values) - 1  #Indices of timestamp occurences
        result = "" # Value found at the best timestamp so far 

        while left_timestamp <= right_timestamp: 
            mid_timestamp = (left_timestamp + right_timestamp) // 2

            if values[mid_timestamp][0] <= timestamp: 
                result = values[mid_timestamp][1]
                left_timestamp = mid_timestamp + 1
            else: 
                right_timestamp = mid_timestamp - 1
        
        return result

    #E: Time: O(logn), Space: O(n) 
class Solution:
    # Time: 9:35 - 10:13 
    def calPoints(self, operations: List[str]) -> int:
        #U: Based on ops, return sum of all the scores on the record after applying all the ops 
            # Keep track of +, D, and C
        
        #M/P: Stacks 
            # Create a record stack
            # For loop go through the ops array 

        #I: 
        record = [] 

        for op in operations: 
            if op == "+": 
                total = record[-1] + record[-2]
                record.append(total)
            elif op == "C": 
                record.pop() 
            elif op == "D": 
                newScore = 2 * record[-1]
                record.append(newScore) 
            else: 
                record.append(int(op))

        return sum(record)

        #R: ops = ["1", "2", "+", "C", "5", "D"]
            # stack/record = [1, 2, 5, 10], sumRecords = 1 + 2 + 5 + 10 = 18
            # sum = record[-1] + record[-2] = 2 + 1 = 3
            # 2 * record[-1] = 2 * 5 = 10 

            # When an integer is encountered (else condition), it's just appended to the stack 

            # When a + is encountered, access the last two elems/nums from the record stack, add those two nums, append that sum 
            # to the record stack 

            # When a "C" is encountered, remove the previous score by popping it from the record stack 

            # When a "D" is encountered, add a score that is 2 * previous score to the record stack. 
        
        #E: Time: O(n), Space: O(n)
        
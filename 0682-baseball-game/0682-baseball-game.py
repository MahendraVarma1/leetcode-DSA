class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

      
        for op in operations:
            if op == "C":
             
                if record:
                    record.pop()
            elif op == "D":
             
                if record:
                    record.append(2 * record[-1])
            elif op == "+":
              
                if len(record) >= 2:
                    record.append(record[-1] + record[-2])
            else:
                
                record.append(int(op))

      
        return sum(record)
        
class Solution:
    def calPoints(self, operations: List[str]) -> int:

        newList= []

        for val in operations:

            match val:
                case "C":
                    self.Clear(newList)
                case "D":
                    newList.append(self.Duplicate(newList[-1]))
                case "+":
                    newList.append(self.Add(newList[-1],newList[-2]))
                case _:
                    newList.append(int(val))
        
        return sum(newList)
    

    def Add(self, num1, num2) -> int:
        return num1 + num2

    def Duplicate(self, num1) -> int:
        return num1 * 2
    
    def Clear(self, lista):
        lista.pop()
        return
        
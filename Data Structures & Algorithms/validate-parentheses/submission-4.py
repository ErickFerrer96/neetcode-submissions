class Solution:
    def isValid(self, s: str) -> bool:

        newList =[]
        
        for val in s:
            if val in "([{":
                newList.append(val)
            if val in ")]}":
                if len(newList) == 0:
                    return False
                
                if val == ")":
                    auxValue = newList.pop()
                    if auxValue == "(":
                        continue
                    else:
                        return False

                elif val == "]":
                    auxValue = newList.pop()
                    if auxValue == "[":
                        continue
                    else:
                        return False
                
                else: 
                    auxValue = newList.pop()
                    if auxValue == "{":
                        continue
                    else:
                        return False

        if len(newList) == 0:
            return True
        else:
            return False
            

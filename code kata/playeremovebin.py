
import math as mt 
  

def checkSub(sub, s): 
  
    j = 0
    for i in range(len(s)): 
        if (sub[j] == s[i]): 
            j += 1
  
    if j == int(len(sub)): 
        return True
    else: 
        return False
  

def getMultiple(s): 
      
    
    for i in range(0, 10**3, 8): 
  
        if (checkSub(str(i), s)): 
            return i 
  
    return -1
  

s = "3454"
print(getMultiple(s)) 

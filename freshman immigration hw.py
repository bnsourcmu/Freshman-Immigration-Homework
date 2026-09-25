def reverseString(s):
    returnarr = []
    
    for i in range(len(s)-1,-1, -1):
        
        returnarr.append(s[i])
    
    return returnarr
                         
                         




def twoSum(s, target):
    
    
    indices = []
    
    for i in range(len(s)):
        num = s[i]
        sumnum = num
        for z in range(i+1, len(s)):
            
            if sumnum+s[z] == target:
                
                indices.append(i)
                indices.append(z)
                
                
                break
            
            
    return indices




def flattenedLists(n):
    
    
    if len(n)==0:
        
        return []
    
    else:
        
        
        if isinstance(n[0],list):
            
            
            return flattenedLists(n[0])+flattenedLists(n[1:])
        
        
        
        
        else:
            
            return [n[0]] + flattenedLists(n[1:])


#find out all palindromes in a given range
#range = {10,115}
def findpalnums(x,y):
    pal = []
    temp = []
    for i  in range(x,y+1):
        for  j  in str(i):
            temp.append(j)
        temp.reverse()
        #print(temp)
        newi = ''.join(temp)
        #print(newi)
        if int(newi) == i:
            pal.append(i)
        temp = []
    return pal
            
print(findpalnums(10,115))   
   

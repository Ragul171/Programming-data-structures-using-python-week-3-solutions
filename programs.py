'''QUESTION 1:
Write a function contracting(l) that takes as input a list of integer l and returns True 
if the absolute difference between each adjacent pair of elements strictly decreases.
 example : >>> contracting([9,2,7,3,1])
             True '''
def contracting(l):
    s=0
    for i in range(0,len(l)-2):
        if(abs(l[i]-l[i+1])>abs(l[i+1]-l[i+2])):
            s+=1
        else:
            s=0
        if s == 0:
            break
    if s != 0:
      return True
    else:
      return False

'''QUESTION 2:
In a list of integers l, the neighbours of l[i] are l[i-1] and l[i+1]. l[i] is a hill if it is strictly greater than its neighbours 
and a valley if it is strictly less than its neighbours.
Write a function counthv(l) that takes as input a list of integers l and returns a list [hc,vc] 
where hc is the number of hills in l and vc is the number of valleys in l
example : >>> counthv([1,2,1,2,3,2,1])
           [2, 1] '''
def counthv(l):
    hc,vc=0,0
    for i in range(1,len(l)-1):
        if l[i]>l[i-1] and l[i] > l[i+1]:
            hc+=1
        elif l[i]<l[i-1] and l[i] < l[i+1]:
            vc+=1
    return [hc,vc]

'''QUESTION 3:
Write a function leftrotate(m) that takes a list representation m of a square matrix as input, 
and returns the matrix obtained by rotating the original matrix counterclockwize by 90 degrees. 
Example :>>> leftrotate([[1,2],[3,4]])
         [[2, 4], [1, 3]] '''
def leftrotate(m):
    s=[]
    for i in range(len(m)):
        temp=[]
        for j in range(len(m[i])):
            temp.append(m[j][len(m)-1-i])
        s.append(temp)
    return s

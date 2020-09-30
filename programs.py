def contracting(l):
    for i in range(0,len(l)):
        if(l[i]-l[i+1]>l[i+1]-l[i+2]):
            return True
        else:
            return False
          
def counthv(l):
    hc,vc=0,0
    for i in range(1,len(l)-1):
        if l[i]>l[i-1] and l[i] > l[i+1]:
            hc+=1
        elif l[i]<l[i-1] and l[i] < l[i+1]:
            vc+=1
    return [hc,vc]

def leftrotate(m):
    s=[]
    for i in range(len(m)):
        temp=[]
        for j in range(len(m[i])):
            temp.append(m[j][len(m)-1-i])
        s.append(temp)
    return s

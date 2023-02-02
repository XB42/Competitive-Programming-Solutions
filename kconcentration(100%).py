class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        #return maxstrengthmid(arr + arr)%10**9+7
        m = sumofall(arr)
        print(m)
        if k<=5:
            print("yoo")
            return maxstrengthmid(arr*k)%(10**9+7)
        else:
            
            if m>0:
                print("yo")
                
                return (m*(k-2) + maxstrengthmid(arr+arr))%(10**9+7)
            else:
                print("whatsup")
                return maxstrengthmid(arr + arr)%(10**9+7)
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        
'''     l = []
        maxx = 0
        m = sumofall(arr)
        arr = arr
'''
        
        #[maxstrengthstart,flag if whole list]
        #l = maxstrength(arr,len(arr))
        #x = maxstrengthend(arr,0)
''' 
            f = m*(k-2)+l[0]+x
        else:
            f = 0
        i = 1
        o = 1
        n = 1
        for i in range(0,k):
            n = maxstrengthmid(arr*i,1)
            o = maxstrengthmid(arr*(i+1),1)
            print("n and o    "+str(n)+"   "+str(o))
            if n<f:
                maxx = f
                break
            elif n < o:
                maxx = o
            else:
                maxx = n
                break
'''
    
        
"""
        print("maxstrength:" +str(l[0]))
        print("maxstrengthend:" +str(m))
        print("maxstrengthmid:" +str(n))
        #if maxsum includes all elements
        if l[1]:
            return int(l[0]*k)%1000000007
        else:
            if(int(l[0])+m)>int(l[0]):
                if (n > int(l[0]+m)):
                    return n
                else:
                    return (l[0]+m)%1000000007
            else:
                if l[0]> n:
                    return int(l[0])%1000000007
                else:
                    return n
                    """
'''  
def maxstrength(arr,index):
        #print("in function maxstrength index is "+str(index))
        total = 0
        if index == 0:
            return [arr[0],False]
        for i in range(index):
            total +=arr[i]
        
        #print("total is "+str(total))
        prevtotal = maxstrength(arr, index-1)
        if total < 0:
            total = 0
        if total > prevtotal[0]:
            if index == len(arr):
                return [total,True]
            else:
                return [total,False]
        else:
            return[prevtotal[0],False]
        
def maxstrengthend(arr,index):
        #print("in function maxstrength index is "+str(index))
        total = 0
        if index >= len(arr):
            return arr[len(arr)-1]
        for i in range(index,len(arr)):
            total +=arr[i]
        
        #print("total is "+str(total))
        prevtotal = maxstrengthend(arr, index+1)
        if total <0:
            total = 0
        if total > prevtotal:
            return total
        else:
            return prevtotal
'''
def maxstrengthmid(arr):
        maxx = 0
        summ = 0
        for i in arr:
            summ +=i
            if summ > maxx :
                maxx = summ
                if maxx>400000:
                    print(maxx)
            elif summ<0:
                summ = 0
        return maxx
            
def sumofall(arr):
    s = 0
    for i in arr:
        s +=i
    return s
def sumcentre(arr):
    f = 0
    front = 0
    back = 0
    for i in arr:
        f +=i
        if front < f:
            front = f
        elif f<0:
            f = 0
    f = 0
    for i in reversed(arr):
        f +=i
        if back < f:
            back = f
        elif f<0:
            f = 0
        back += arr[0]
        return(front + back)
'''

def fn(k,i)
    if k< 20
        return 1
    else:
        '''
        
        
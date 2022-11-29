#my sol
def solution(arr):
    res=[]
    if len(arr) <= 1000000:
        for i in arr:
            if i<10:
                for i in range(1,len(arr)):
                    if arr[i-1] != arr[i]:
                        res.append(arr[i-1])
                    if i == len(arr)-1:
                        res.append(arr[i])
                return res

#better sol
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

print(solution([1,1,3,3,0,1,1]))
print(no_continuous([1,1,3,3,0,1,1]))
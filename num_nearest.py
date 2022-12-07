'''
(문제 설명)
정수 배열 array와 정수 n이 매개변수로 주어질 때, array에 들어있는 정수 중 
n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.

(제한사항)
1 ≤ array의 길이 ≤ 100
1 ≤ array의 원소 ≤ 100
1 ≤ n ≤ 100
가장 가까운 수가 여러 개일 경우 더 작은 수를 return 합니다.
'''

def mine(array, n):
    arr = sorted(array)
    res = [abs(n-i) for i in arr]
    return(arr[res.index(min(res))])

print(mine([3, 10, 28],	20))
print(mine([10, 11, 12], 13))
print(mine([9, 8, 11, 12], 10))

otherSol =lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]

print(otherSol([3, 10, 28],	20))
print(otherSol([10, 11, 12], 13))
print(otherSol([9, 8, 11, 12], 10))
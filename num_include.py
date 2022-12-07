'''
(문제 설명)
머쓱이는 행운의 숫자 7을 가장 좋아합니다. 정수 배열 array가 매개변수로 주어질 때,
7이 총 몇 개 있는지 return 하도록 solution 함수를 완성해보세요.

(제한사항)
1 ≤ array의 길이 ≤ 100
0 ≤ array의 원소 ≤ 100,000
'''
def mine_1(array):
    #int형 배열-> str
    strArr = "".join(map(str, array))
    return strArr.count('7') if '7' in strArr else 0

print(mine_1([7, 77, 17]))
print(mine_1([10, 29]))

def otherSol_1(arr):
  return str(arr).count('7')

print(otherSol_1([7, 77, 17]))
print(otherSol_1([10, 29]))

'''
(문제설명)
1부터 13까지의 수에서, 1은 1, 10, 11, 12, 13 이렇게 총 6번 등장합니다. 정수 i, j, k가 매개변수로 주어질 때, i부터 j까지 k가 몇 번 등장하는지 return 하도록 solution 함수를 완성해주세요.

(제한사항)
1 ≤ i < j ≤ 100,000
0 ≤ k ≤ 9
'''
def mine_2(i, j, k):
    cnt = 0
    for a in range(i,j+1):
        if str(k) in str(a):
            cnt += str(a).count(str(k))
    return cnt 
print(mine_2(1,13,1))
print(mine_2(3,10,2))

def otherSol_2(i, j, k):
    return sum(map(lambda v: str(v).count(str(k)), range(i, j+1)))
print(otherSol_2(1,13,1))
print(otherSol_2(3,10,2))

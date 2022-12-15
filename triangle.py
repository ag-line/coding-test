'''
(문제 설명)
선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.
가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
삼각형의 두 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다. 
나머지 한 변이 될 수 있는 정수의 개수를 return하도록 solution 함수를 완성해주세요.

(제한사항)
sides의 원소는 자연수입니다.
sides의 길이는 2입니다.
1 ≤ sides의 원소 ≤ 1,000
'''

def mySol(sides):
    max_min = max(sides)-min(sides)
    maxSides,remaind = 0, 0
    #sides가 가장 긴 변인 경우
    for i in range(max_min+1,max(sides)+1):
        maxSides += 1
    #나머지 한 변이 가장 긴 변인 경우
    for i in range(max(sides)+1,sum(sides)):
        remaind += 1
    return (maxSides+remaind)

print(mySol([1,2]))
print(mySol([3,6]))
print(mySol([11,7]))

def otherSol(sides):
    return sum(sides) - max(sides) + min(sides) - 1

print(otherSol([1,2]))
print(otherSol([3,6]))
print(otherSol([11,7]))
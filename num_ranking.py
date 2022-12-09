'''
(문제 설명)
외과의사 머쓱이는 응급실에 온 환자의 응급도를 기준으로 진료 순서를 정하려고 합니다. 
정수 배열 emergency가 매개변수로 주어질 때 응급도가 높은 순서대로 
진료 순서를 정한 배열을 return하도록 solution 함수를 완성해주세요.

(제한사항)
중복된 원소는 없습니다.
1 ≤ emergency의 길이 ≤ 10
1 ≤ emergency의 원소 ≤ 100
'''
def solution(emergency):
    numList = sorted(emergency)
    numList.reverse()
    return [numList.index(i)+1 for i in emergency]
print(solution([3, 76, 24]))
print(solution([1, 2, 3, 4, 5, 6, 7]))
print(solution([30, 10, 23, 6, 100]	))

def otherSol(emergency):
    return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]
print(otherSol([3, 76, 24]))
print(otherSol([1, 2, 3, 4, 5, 6, 7]))
print(otherSol([30, 10, 23, 6, 100]	))
'''
문제 설명
약수의 개수가 세 개 이상인 수를 합성수라고 합니다. 자연수 n이 매개변수로 주어질 때 
n이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ n ≤ 100
'''

def solution(n):
    cnt = 0
    res = 0
    for i in range(4, n+1):
        for j in range(1,i+1):
            if i % j == 0:
                cnt+=1
        if cnt>=3:
            res+=1
            cnt = 0
    return(res)
  
print(solution(10)) #5
print(solution(15)) #8
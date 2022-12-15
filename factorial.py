import math

#재귀함수
def factorial(n):
    if(n > 1):
        return n * factorial(n - 1)
    else:
        return 1
#for문
def forFactorial(n):
  num = 1
  for i in range(1, n+1):
      num *= i 
  print(num)
#Math module
def moudulUse(n):
    print(math.factorial(n))

'''
머쓱이는 구슬을 친구들에게 나누어주려고 합니다. 구슬은 모두 다르게 생겼습니다. 
머쓱이가 갖고 있는 구슬의 개수 balls와 친구들에게 나누어 줄 구슬 개수 share이 매개변수로 주어질 때, 
balls개의 구슬 중 share개의 구슬을 고르는 가능한 모든 경우의 수를 return 하는 solution 함수를 완성해주세요.

서로 다른 n개 중 m개를 뽑는 경우의 수 공식은 다음과 같습니다.
= n! / ((n-m)! * m!)
'''
def forUse(balls, share):
    n=1
    n_m=1
    m=1
    for i in range(1,balls+1):
        n*=i
    for i in range(1,balls-share+1):
        n_m*=i
    for i in range(1,share+1):
        m*=i
    return n/n_m/m

def mathUse(balls, share):
    return math.factorial(balls) /(math.factorial(balls-share) * math.factorial(share))

print(forUse(3,2))
print(forUse(5,3))
print(mathUse(3,2))
print(mathUse(5,3))
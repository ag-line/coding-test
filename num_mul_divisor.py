'''
(문제 설명)
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

(제한 사항)
두 수는 1이상 1000000이하의 자연수입니다.
'''
def solution(n, m):
  #Max-common-divisor
  n_div = [i  for i in range(1,n+1) if n%i == 0]
  m_div = [i  for i in range(1,m+1) if m%i == 0]
    
  #Min-common-multiple
  n_mul = [i*n for i in range(1, m+1)]
  m_mul = [i*m for i in range(1, n+1)]
    
  res = [max(set(n_div) & set(m_div)), min(set(n_mul) & set(m_mul))]
  return res

print(solution(3,12))
print(solution(2,5))

def oherSol(n, m):
  #import math
  #math.gcd(nums) // 숫자들의 최대 공약수(정수)를 반환
  #math.icm(nums) // 숫자들의 최대 공배수(정수)를 반환
  gcd = lambda a,b : b if not a%b else gcd(b, a%b)
  lcm = lambda a,b : a*b//gcd(a,b)
  return [gcd(n, m), lcm(n, m)]
print(oherSol(3,12))
print(oherSol(2,5))
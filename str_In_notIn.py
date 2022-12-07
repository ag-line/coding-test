'''
(문제 설명)
문자열 before와 after가 매개변수로 주어질 때, 
before의 순서를 바꾸어 after를 만들 수 있으면 1을,
만들 수 없으면 0을 return 하도록 solution 함수를 완성해보세요.

(제한사항)
0 < before의 길이 == after의 길이 < 1,000
before와 after는 모두 소문자로 이루어져 있습니다.
'''

def solution(before, after):
  res = 1
  if len(before) == len(after) and not before.isupper() and not after.isupper():
    before, after = list(before), list(after)
    for i in before:
      if i in after:
          res *= 1
          after.remove(i)
      else:
          res *= 0
    return res

print(solution("olleh","hello"))
print(solution("allpe","apple"))

def otherSol(before, after):
    return 1 if sorted(before)==sorted(after) else 0

print(otherSol("olleh","hello"))
print(otherSol("allpe","apple"))

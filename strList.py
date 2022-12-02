""" 
문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 
각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.
<제한 사항>
문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다. 
"""

def solution1(s):
  res = ''
  for str in s.split(' '):
    stL = list(str)
    for i in range(len(stL)):
        if i%2 == 0:
            stL[i] = stL[i].upper()
    #list->str
    res += ' '.join(s for s in stL).replace(" " , "") +' '
  return(res.rstrip())

import re
def solution2(s):
    res=''
    string = re.sub(r"\s", ",", s).split(',')
    for str in string:
        stL =[str[i].upper() if i%2 == 0 else str[i] for i in range(len(str))]
        #list->str
        res += ' '.join(s for s in stL).replace(" " , "") +' '
    #마지막 공백제거
    return res.rstrip()


print(solution1("try hello world"))
print(solution2("try hello world"))
'''
문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때,
my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.
'''

def mine(my_string, num1, num2):
    str = list(my_string)
    temp = str[num1]
    str[num1] = str [num2]
    str [num2] = temp

    return (''.join(str))

def otherSol(my_string, num1, num2):
    str = list(my_string)
    str[num1], str[num2] = str[num2], str[num1]
    answer = ''.join(str)
    return answer

print(mine("hello",1,2))
print(otherSol("hello",1,2))
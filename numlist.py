#정수 n과 정수 배열 numlist가 매개변수로 주어질 때, 
#numlist에서 n의 배수가 아닌 수들을 제거한 배열을 return하도록 solution 함수를 완성해주세요.

def solution1(n, numlist):
    for i in range(len(numlist)):
        for num in numlist:
            if num%n != 0:
                numlist.remove(num)
    return numlist

def solution2(n, numlist):
    return list(filter(lambda num: num%n == 0, numlist))
  
def solution3(n, numlist):
    answer = [num for num in numlist if num%n==0]
    return answer

print(solution1(3,[4, 5, 6, 7, 8, 9, 10, 11, 12]))
print(solution2(3,[4, 5, 6, 7, 8, 9, 10, 11, 12]))
print(solution3(3,[4, 5, 6, 7, 8, 9, 10, 11, 12]))
#array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
#divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.
def solution1(arr, divisor):
    ans = sorted([arr[i] for i in range(len(arr)) if arr[i]%divisor==0 ])
    if len(ans) == 0 :
        ans.append(-1)
    return ans

def solution2(arr, divisor): 
  return sorted([n for n in arr if n%divisor == 0]) or [-1]

print(solution1([5, 9, 7, 10],5))
print(solution2([5, 9, 7, 10],5))
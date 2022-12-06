'''
<문제 설명>
정수 배열 numbers가 매개변수로 주어집니다. 
numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.
<제한사항>
-10,000 ≤ numbers의 원소 ≤ 10,000
2 ≤ numbers 의 길이 ≤ 100
'''
def mine(nums):
    if len(nums)>=2 and len(nums)<=100 and filter(lambda x:-10000<=x<=10000, nums):
        nums.sort()
        if nums[0] < 0 and nums[0] * nums[1] > 0 and nums[-1] * nums[-2] < nums[0] * nums[1]:
            return nums[0] * nums[1]
        else:
            return nums[-1] * nums[-2]

print(mine([1, 2, -3, 4, -5]))
print(mine([10, 20, 30, 5, 5, 20, 5]	))
          
def otheSol(numbers):
  numbers.sort()
  return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])

print(otheSol([1, 2, -3, 4, -5]))
print(otheSol([10, 20, 30, 5, 5, 20, 5]	))

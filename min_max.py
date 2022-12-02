""" 
명함 지갑을 만드는 회사에서 지갑의 크기를 정하려고 합니다. 
다양한 모양과 크기의 명함들을 모두 수납할 수 있으면서, 작아서 들고 다니기 편한 지갑을 만들어야 합니다. 
이러한 요건을 만족하는 지갑을 만들기 위해 디자인팀은 모든 명함의 가로 길이와 세로 길이를 조사했습니다.
번호 / 가로 / 세로
1	/ 60	/ 50
2	/ 30	/ 70
3	/ 60	/ 30
4	/ 80	/ 40
가장 긴 가로 길이와 세로 길이가 각각 80, 70이기 때문에 80(가로) x 70(세로) 크기의 지갑을 만들면 모든 명함들을 수납할 수 있습니다. 
하지만 2번 명함을 가로로 눕혀 수납한다면 80(가로) x 50(세로) 크기의 지갑으로 모든 명함들을 수납할 수 있습니다. 이때의 지갑 크기는 4000(=80 x 50)입니다.
모든 명함의 가로 길이와 세로 길이를 나타내는 2차원 배열 sizes가 매개변수로 주어집니다. 
모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return 하도록 solution 함수를 완성해주세요.
"""

def mine(sizes):
    sizes.sort()
    Maxlist = [max(i) for i in sizes]
    Minlist = [min(i) for i in sizes]
    return(max(Minlist)*max(Maxlist))
  
#use lambda
solution1 = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)

#not use Math
def solution2(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col

print(mine([[60, 50], [30, 70], [60, 30], [80, 40]])) #4000
print(solution1(([[60, 50], [30, 70], [60, 30], [80, 40]]))) #4000
print(solution2([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])) #120
print(mine([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])) #120
print(mine([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])) #133

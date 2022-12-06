""" 2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 
두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요. 
요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT입니다. 
예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.

<제한 조건>
2016년은 윤년입니다. =>2월 29일까지
2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)
 """
def mine(a, b):
    day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    start = 5 #금
    end = 7 #일
    if a<13 and b<32:
        for i in range(a-1):
            i = i+2
            date = (30 if i%2 == 0 and i!=2  else 29 if i==2 else 31) if i<7 else (31 if i%2 == 0 or i==7 else 30)          
            start = (end + 1) % 7
            end = (start if date==29 else (start+1) % 7 if date ==30 else (start+2) % 7) 
        return day[(start + b%7-1) % 7]

def otherSol(a, b):
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    dayLen = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    now = 5
    for i in range(0, a - 1) :
        now += dayLen[i]

    answer = (now + b - 1) % 7

    return days[answer]

print(mine(5,24))
print(otherSol(5,24))
print(mine(2,28))
print(otherSol(2,28))
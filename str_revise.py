""" 다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.
1478 → "one4seveneight" / 234567 → "23four5six7" / 10203 → "1zerotwozero3"
이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 
혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. 
s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.
"""
def mine(s):
  alpha = ["zero","one","two","three","four","five","six","seven","eight","nine"]
  for i in range(len(alpha)):
    if alpha[i] in s:
      s = s.replace(alpha[i],str(i))
  print(s)

#zip() use
def solution1(s):
  answer = 0
  word_list=['zero','one','two','three','four','five','six','seven','eight','nine']
  num_list=[a for a in range(len(word_list))]
  for word, i in zip(word_list,num_list):
      s=s.replace(word,str(i))
  answer=int(s)  
  print (answer)

#dic use
def solution(s):
  num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
  answer = s
  for key, value in num_dic.items():
      answer = answer.replace(key, value)
  print(int(answer)) 

mine("one4seveneight")
mine("2three45sixseven")
# solution1("one4seveneight")
# solution("2three45sixseven")
# solution2("2three45sixseven")
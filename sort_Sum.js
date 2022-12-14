/* 문제:
  정수 배열 numbers가 주어집니다. 
  numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 
  만들 수 있는 모든 수를 배열에 오름차순으로 담아 
  return 하도록 solution 함수를 완성해주세요.
  numbers의 길이는 2 이상 100 이하입니다.
  numbers의 모든 수는 0 이상 100 이하입니다.
*/

function solution(numbers) {
  var answer = [];
  if (
    numbers.length >= 2 &&
    numbers.length <= 100 &&
    numbers.every((v) => v <= 100)
  ) {
    for (var i in numbers) {
      for (var j in numbers) {
        if (i != j) answer.push(numbers[i] + numbers[j]);
      }
    }
  }
  //set: 중복제거
  const res = [...new Set(answer)];
  //오름차순 정렬
  res.sort((a, b) => a - b);
  return res;
}

console.log(solution([2, 1, 3, 4, 1]));
console.log(solution([5, 0, 2, 7]));

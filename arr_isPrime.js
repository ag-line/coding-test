/*
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
숫자들이 들어있는 배열 nums가 매개변수로 주어질 때,
 nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 
소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.
*/

const getCombinations = function (arr, selectNumber) {
  const results = [];
  if (selectNumber === 1) return arr.map((el) => [el]);
  // n개중에서 1개 선택할 때(nC1), 바로 모든 배열의 원소 return
  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1);
    // 해당하는 fixed를 제외한 나머지 뒤
    const combinations = getCombinations(rest, selectNumber - 1);
    // 나머지에 대해서 조합을 구한다.
    const attached = combinations.map((el) => [fixed, ...el]);
    //  돌아온 조합에 떼 놓은(fixed) 값 붙이기
    results.push(...attached);
    // 배열 spread syntax 로 모두다 push
  });

  return results; // 결과 담긴 results return
};
function isPrime(num) {
  for (let i = 2; num > i; i++) {
    if (num % i === 0) return false;
  }
  return num > 1;
}

function solution(nums) {
  const result = getCombinations(nums, 3);
  let count = 0;
  for (let i = 0; i < result.length; i++) {
    let sum1 = result[i].reduce((sum2, currValue) => {
      return sum2 + currValue;
    });
    if (isPrime(sum1)) {
      count += 1;
    }
  }
  return count;
}

console.log(solution([1, 2, 3, 4])); //1
console.log(solution([1, 2, 7, 6, 4])); //4

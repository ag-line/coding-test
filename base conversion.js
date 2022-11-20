/*문제: 
  자연수 n이 매개변수로 주어집니다.
  n을 3진법 상에서 앞뒤로 뒤집은 후, 
  이를 다시 10진법으로 표현한 수를 
  return 하도록 solution 함수를 완성해주세요.
*/

function solution(n) {
  //10진법->n진법 : var.toString(n)
  let three_n = n.toString(3);
  let rev = three_n.split("").reverse().join("");
  //n진법->10진법 : parseInt(var, n)
  let ans = parseInt(rev, 3);
  console.log(n, " => ", three_n, "(3) => reverse ", rev, "=> ", ans, "(10)");
  return ans;
}
solution(45);
solution(125);

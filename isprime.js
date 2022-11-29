//1. half num
const isPrime_Half = (num) => {
  if (!num || num === 1) return false;
  for (let i = 2; i <= num / 2; i++) {
    if (num % i === 0) return false;
  }
  return true;
};
//2. Math.sqrt
function isPrime_Sqrt(num) {
  for (let i = 2; i <= Math.floor(Math.sqrt(num)); i++) {
    if (num % i === 0) return false;
  }
  return true;
}
console.log("half_7:", isPrime_Half(7)); //true
console.log("Sqrt_10:", isPrime_Sqrt(10)); //false

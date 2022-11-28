function getBinary(x) {
  let str = "";

  if (x === 0) {
    return "0";
  }

  while (x > 0) {
    let bin = x % 2;
    x = Math.floor(x / 2);
    str = bin.toString() + str;
  }
  return str;
}

function solution(N) {
  let binary = N.toString(2);
  console.log(binary);

  let i = 0;
  let goOn = binary.length > 1;
  let maxGap = 0;

  while (goOn) {
    for (let j = i + 1; j < binary.length; j++) {
      if (j === binary.length - 1) {
        goOn = false;
      }
      if (binary[i] == 1 && binary[j] == 1 && i < j) {
        maxGap = Math.max(maxGap, j - i - 1);
        i = j;
        break;
      }
    }
  }
  return maxGap;
}

console.log(solution(1));

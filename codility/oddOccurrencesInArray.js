function solution(A) {
  if (A.length === 1) {
    return A[0];
  }

  let cacheUnpaired = {};

  A.forEach((element) => {
    if (cacheUnpaired[element] === undefined) {
      cacheUnpaired[element] = 1;
    } else {
      delete cacheUnpaired[element];
    }
  });

  return parseInt(Object.keys(cacheUnpaired)[0]);
}

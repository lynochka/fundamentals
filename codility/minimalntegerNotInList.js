function solution(A) {
  let n = A.length;
  let found = Array(n + 1).fill(false);

  for (let i = 0; i < n; i++) {
    if (A[i] > 0 && A[i] <= n) {
      found[A[i]] = true;
    }
  }

  for (let i = 1; i <= n; i++) {
    if (!found[i]) {
      return i;
    }
  }
  return n + 1;
}

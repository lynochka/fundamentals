function solution(A) {
  let n = A.length;
  let found = Array(n + 2).fill(false);

  for (let i = 0; i < n; i++) {
    found[A[i]] = true;
  }

  for (let i = 1; i <= n + 1; i++) {
    if (!found[i]) {
      return i;
    }
  }
}

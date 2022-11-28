function solution(A, K) {
  N = A.length;
  K = K % N;

  if (K === 0) {
    return A;
  }

  const A2 = A.slice(0, N - K);

  const A1 = A.slice(N - K);

  return [...A1, ...A2];
}

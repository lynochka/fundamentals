function solution(X, Y, D) {
  if (X === Y) {
    return 0;
  }
  let jumps = Math.floor((Y - X) / D);
  return (Y - X) % D > 0 ? jumps + 1 : jumps;
}

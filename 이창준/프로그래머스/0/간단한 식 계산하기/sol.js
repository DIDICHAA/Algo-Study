function solution(binomial) {
  var answer = 0;
  const s = binomial.split(" ");
  const n1 = parseInt(s[0]);
  const n2 = parseInt(s[2]);

  switch (s[1]) {
    case "+":
      return n1 + n2;
    case "-":
      return n1 - n2;
    case "*":
      return n1 * n2;
  }
}

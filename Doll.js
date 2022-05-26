//뽑은거 위치를 열로 표시하면
//그리고 포문으로 각 행의 pickColumn열의 숫자가 0이 아닌 곳까지 찾아.
//만약 0이 아니라면 그 숫자를 리턴해줌  //해당 위치는 0으로 만들어주는 거 따로
const findFirstMeetDollNumber = (board, move) => {
  for (let i = 0; i < board.length; i++) {
    if (board[i][move] !== 0) {
      dollNumber = board[i][move];
      board[i][move] = 0;
      return dollNumber;
    }
  }
  return "인형없음";
};

const checkSameDoll = (stack, doll, answer) => {
  console.log("stack,doll,answer인풋 :" + stack + " " + doll + " " + answer);
  if (stack.length < 0) {
    stack.push(doll);
    return { answer, stack };
  } else if (doll === stack[stack.length - 1]) {
    answer += 1;
    stack.pop();
    return { answer, stack };
  } else {
    if (doll === "인형없음") {
      return { answer, stack };
    }
    stack.push(doll);
    return { answer, stack };
  }
};

function solution(board, moves) {
  var answer = 0;
  let stack = [];

  //본문//
  for (let i = 0; i < moves.length; i++) {
    console.log("####" + (i + 1) + "회차" + "####\n");
    //뽑아야할 위치를 1~5 => 0~4
    const move = moves[i] - 1;
    const doll = findFirstMeetDollNumber(board, move);
    console.log("doll: " + doll);

    const checkResult = checkSameDoll(stack, doll, answer);
    console.log(board);
    answer = checkResult.answer;
    stack = checkResult.stack;
    console.log("answer: " + answer);
    console.log("stack: " + stack);
  }
  return answer * 2;
}

solution(
  [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1],
  ],
  [1, 5, 3, 5, 1, 2, 1, 4]
);

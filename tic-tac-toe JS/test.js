let winningPattern = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [2, 4, 6],
];
let player1 = true;
let reset = document.querySelector("#reset");
let button = document.querySelectorAll(".box");
let winner = document.querySelector(".winner");

for (let i = 0; i < 9; i++) {
  button[i].addEventListener(
    "click",
    () => {
      if (player1) {
        button[i].innerHTML = `O`;
        button[i].classList.add("blue");
        player1 = false;
      } else {
        button[i].innerHTML = `X`;
        button[i].classList.add("red");

        player1 = true;
      }
      checkWinner();
    },
    { once: true }
  );
}
function checkWinner() {
  for (pattern of winningPattern) {
    let pos1 = button[pattern[0]].innerText;
    let pos2 = button[pattern[1]].innerText;
    let pos3 = button[pattern[2]].innerText;
    if (pos1 !== "" && pos2 !== "" && pos3 !== "") {
      if (pos1 === pos2 && pos2 === pos3) {
        if (pos1 == "O") {
          winner.textContent = `Player 1`;
        } else {
          winner.textContent = `Player 2`;
        }
      }
    }
  }
}

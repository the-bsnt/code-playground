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
let count = 0;
let player1 = true;
let reset = document.querySelector("#reset");
let button = document.querySelectorAll(".box");
let winner = document.querySelector(".winner");
let restart = document.querySelector(".restart");
// let clickIt;
button.forEach((box) => {
  box.addEventListener("click", () => {
    if (player1) {
      box.innerHTML = `O`;
      box.classList.add("blue");
      player1 = false;
    } else {
      box.innerHTML = `X`;
      box.classList.add("red");
      player1 = true;
    }
    count++;
    checkWinner();
    checkDraw(count);
    box.classList.add("notclick");
  });
});

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
        disableEvent();
      }
    }
  }
}
function disableEvent() {
  button.forEach((box) => {
    box.classList.add("disabled");
  });
}
reset.addEventListener("click", () => {
  button.forEach((box) => {
    box.classList.remove("disabled", "notclick", "blue", "red");
    box.innerHTML = ``;
    player1 = true;
    count = 0;
    restart.innerHTML = ``;
    restart.classList.remove("gameover");
  });
  winner.textContent = ``;
});
function checkDraw(c) {
  if (c == 9 && winner.textContent == ``) {
    restart.innerHTML = `Game Over <br> Restart Again `;
    restart.classList.add("gameover");
  }
}

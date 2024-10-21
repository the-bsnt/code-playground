const display = document.querySelector(".display");

flag = 0;
const optrs = "+-*/";
const stack = [];

//for each button pressed;
const btn = document.querySelectorAll(".btn");
btn.forEach((btnn) => {
  btnn.addEventListener("click", () => {
    const input = btnn.textContent;
    appendToDisplay(input);
  });
});

// to clear the display screen of calculator;
const clear = document.querySelector("#clear");
clear.onclick = () => {
  display.value = "";
  display.classList.remove("error", "result");
  stack.length = 0;
};

//to calculate total result
const equalto = document.querySelector("#equalto");
equalto.onclick = () => {
  calculate();
  stack.length = 0;
};

//back key;

const cross = document.querySelector("#cross");
cross.addEventListener("click", () => {
  let tempVal = display.value;
  clearDisplay();
  if (flag != 2) {
    display.value = tempVal.slice(0, tempVal.length - 1);
  }
});

// key for bracket ;
const braces = document.querySelector(".braces");
braces.addEventListener("click", () => {
  if (flag != 0) {
    display.classList.remove("result", "error");
    if (flag == 2) {
      display.value == "";
    }
  }
  const lastChr = display.value[display.value.length - 1];
  if (stack.length === 0) {
    //both stack and display are empty
    if (lastChr === undefined) {
      console.log("a");
      display.value += "(";
    }
    //stack is empty but display contains something
    else {
      if (optrs.includes(lastChr)) {
        display.value += "(";
      } else {
        display.value += "*(";
      }
    }
    stack.push("(");
  }
  //stack is not empty and display is also not empty
  else {
    if (optrs.includes(lastChr) || lastChr == "(") {
      stack.push("(");
      display.value += "(";
    } else {
      stack.pop();
      display.value += ")";
    }
  }
});

// functions
function appendToDisplay(input) {
  if (input === "¬" || input === "%") {
    sfn(input);
    return;
  }

  if (flag != 0) {
    let tempVal = display.value;
    clearDisplay();
    if (flag === 1 && optrs.includes(input)) {
      display.value = tempVal;
      5;
    }
  }
  display.value += input;
  flag = 0;
}
function clearDisplay() {
  display.classList.remove("result", "error");
  display.value = "";
}
function calculate() {
  if (display.value === ``) {
    return;
  }
  try {
    let result = eval(display.value);
    if (isNaN(result)) {
      throw new Error("");
    }
    display.value = result;
    display.classList.add("result");
    flag = 1;
  } catch (e) {
    display.value = "";
    display.classList.add("error");
    console.log(display.classList);
    display.value += `syntax error`;

    flag = 2;
  }
}
//special function for negation (¬) and percentage [ % ];
function sfn(f) {
  if (display.value === "") {
    return;
  }
  if (f === "%") {
    display.value = display.value / 100;
  } else if (f === "¬") {
    display.value = -display.value;
  }
  calculate();
  display.classList.remove("result");
  return;
}

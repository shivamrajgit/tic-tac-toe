let turnCounter = 0;
let X = [];
let O = [];
let winOptions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]];
let oTurn = true;

let btns = document.querySelectorAll(".button");
let resetBtn = document.querySelector(".resetBtn");
let h2 = document.querySelector("h2");

const reset = () => {
    turnCounter = 0;
    X = [];
    O = [];
    oTurn = true;
    resetBtn.innerText = "RESET GAME";
    enableBtns();
    h2.innerText = "";
}


const game = () => {
    if (oTurn) {
        for (let option of winOptions) {
            if (option.every(element => X.includes(element))) {
                h2.innerText = "X WINS!";
                console.log("X WINS!");
                disableBtns();
                resetBtn.innerText = "NEW GAME";
                return;
            }
        }
    }
    else {
        for (let option of winOptions) {
            if (option.every(element => O.includes(element))) {
                h2.innerText = "O WINS!";
                console.log("O WINS!");
                disableBtns();
                resetBtn.innerText = "NEW GAME";
                return;
            }
        }
    };
}

const disableBtns = () => {
    for(let btn of btns){
        btn.disabled = true;
    }
}

const enableBtns = () => {
    for(let btn of btns){
        btn.disabled = false;
        btn.innerText = "";
    }
}

btns.forEach((btn) => {
    btn.addEventListener("click", (ev) => {
        if (oTurn) {
            btn.innerText = "O";
            oTurn = false;
            btn.disabled = true;
            O.push(Number(ev.target.id));
            turnCounter++;
        }
        else {
            btn.innerText = "X";
            oTurn = true;
            btn.disabled = true;
            X.push(Number(ev.target.id));
            turnCounter++;
        }
        if (turnCounter >= 5) {
            game();
        }
        if (turnCounter == 9){
            h2.innerText = "IT'S A DRAW";
            disableBtns();
            resetBtn.innerText = "NEW GAME";
        }

    });
});

resetBtn.addEventListener("click",reset);
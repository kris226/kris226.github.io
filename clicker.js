let count = 0;
let power = 1;

function changeScore()
{
    count = count + power;
    document.getElementById("score").innerText = `Coins ${count}`;    
}


function upgrade()
{
    if (count >= 10){
    power++;
    document.getElementById("powerText").innerText = `Power ${power}`;
    count = count - 10;
    document.getElementById("score").innerText = `Coins ${count}`;
    }
}




document.getElementById("clicker").addEventListener("click", changeScore);

document.getElementById("upgrador").addEventListener("click", upgrade);
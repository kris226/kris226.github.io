let count = 0;
let power = 1;

function changeScore()
{
    count = count + power;
    document.getElementById("score").innerText = `Clicked: ${count} times`;    
}


function upgrade()
{
    
    power++;
    count = count - 10;
    document.getElementById("score").innerText = `Clicked: ${count} times`;
}




document.getElementById("clicker").addEventListener("click", changeScore);

document.getElementById("upgrador").addEventListener("click", upgrade);
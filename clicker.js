let count = 0;
let power = 1;

let applePrice = 0;
let pearPrice = 0;
let bananaPrice = 0;
let peachPrice = 0;
let pineapplePrice = 0;





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

function NextDay()
{
    applePrice = Math.floor(Math.random() * 11) + 30;
    document.getElementById("applePriceText").innerText = `Apple ${applePrice}`;

    pearPrice = Math.floor(Math.random() * 11) + 30;
    document.getElementById("pearPriceText").innerText = `Pear ${pearPrice}`;
    
    bananaPrice = Math.floor(Math.random() * 11) + 30;
    document.getElementById("bananaPriceText").innerText = `Banana ${bananaPrice}`;
    
    peachPrice = Math.floor(Math.random() * 11) + 30;
    document.getElementById("peachPriceText").innerText = `Peach ${peachPrice}`;
    
    pineapplePrice = Math.floor(Math.random() * 11) + 30;
    document.getElementById("pineapplePriceText").innerText = `Pineapple ${pineapplePrice}`;
    


}






document.getElementById("clicker").addEventListener("click", changeScore);

document.getElementById("upgrador").addEventListener("click", upgrade);

document.getElementById("nextDay").addEventListener("click", NextDay);
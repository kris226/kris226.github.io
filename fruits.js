function NextDay()
{
    applePrice = Math.floor(Math.random() * 11) + 30;
    document.getElementById("applePriceText").innerText = applePrice;

    pearPrice = Math.floor(Math.random() * 11) + 30;
    document.getElementById("pearPriceText").innerText = pearPrice;
    
    bananaPrice = Math.floor(Math.random() * 11) + 30;
    document.getElementById("bananaPriceText").innerText = bananaPrice;
    
    peachPrice = Math.floor(Math.random() * 11) + 30;
    document.getElementById("peachPriceText").innerText = peachPrice;
    
    pineapplePrice = Math.floor(Math.random() * 11) + 30;
    document.getElementById("pineapplePriceText").innerText = pineapplePrice;
    


}


function BuyFruit()
{

    document.getElementById("moneyText").innerText = fruit;






}






document.getElementById("nextDay").addEventListener("click", NextDay);



document.getElementsByClassName("buysellButton").addEventListener("click", fruit = 4,BuyFruit)
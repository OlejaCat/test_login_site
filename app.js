let tg = window.Telegram.WebApp;

tg.expand();

let btn = document.getElementById("btn");
let username = document.getElementById("username");
let password = document.getElementById("password");

btn.addEventListener(
    "click", function() {
        tg.sendData("testtest");
    }
 )
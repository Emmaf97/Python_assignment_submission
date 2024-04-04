document.addEventListener("DOMContentLoaded", init);

function init() {
    let lightToggle = document.getElementById("dark-icon");
    lightToggle.addEventListener("click", lightMode);
    checkLightActive();
}

let toggleCheck = false;

function checkLightActive() {
    if (localStorage.getItem("light-mode") === "true") {
        lightMode();
    }
}

function lightMode() {
    let { btnElements, body, pLight, cardtext, trainergrid,header,toplayer,nav } = getIndexDocElements();
    for (let i = 0; i < btnElements.length; i++) {
        let lightModeAdded = btnElements[i].classList.toggle("dark-icon");
        if (!lightModeAdded) {
            toggleCheck = false;
            localStorage.setItem("light-mode", toggleCheck);
            body.classList.remove("body-light");
            header.classList.remove("bg-light")
            header.classList.add("bg-dark")
            nav.classList.remove("bg-light")
            nav.classList.add("bg-dark")
            toplayer.classList.remove("bg-light")
            toplayer.classList.add("bg-dark")
            nav.classList.toggle("bg-light")
            for (let j = 0; j < pLight.length; j++) {
                pLight[j].classList.remove("p-light");
            }
            for (let c = 0; c < cardtext.length; c++) {
                cardtext[c].classList.remove("card-text-light")
            }
            if (trainergrid){
            trainergrid.classList.toggle("bg-dark");
            trainergrid.classList.remove("bg-light");
            }
        }
        else {
            toggleCheck = true;
            localStorage.setItem("light-mode", toggleCheck);
            body.classList.add("body-light");
            header.classList.remove("bg-dark")
            header.classList.add("bg-light")
            nav.classList.remove("bg-dark")
            nav.classList.add("bg-light")
            toplayer.classList.remove("bg-dark")
            toplayer.classList.add("bg-light")
            for (let k = 0; k < pLight.length; k++) {
                pLight[k].classList.add("p-light");
            }
            for (let b = 0; b < cardtext.length; b++) {
                cardtext[b].classList.add("card-text-light")
            }
            if (trainergrid){
            trainergrid.classList.toggle("bg-dark")
            trainergrid.classList.add("bg-light")
            }
        }
    }
}
function getIndexDocElements() {
    let btnElements = document.querySelectorAll(".material-symbols-outlined");
    let body = document.querySelector("body")
    let header = document.querySelector("header")
    let nav = document.querySelector("nav")
    let toplayer = document.querySelector(".toplayer")
    let pLight = document.querySelectorAll(".p.left")
    let cardtext = document.querySelectorAll(".card-text")
    let trainergrid = document.querySelector("#trainer-grid")
    return { btnElements, body, pLight, cardtext, trainergrid,header,toplayer,nav};
}

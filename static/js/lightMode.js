document.addEventListener("DOMContentLoaded", init);

function init() {
    let lightToggle = document.getElementById("dark-icon");
    lightToggle.addEventListener("click", lightMode);
    console.log(lightToggle)
    checkLightActive();
}

let toggleCheck = false;

function checkLightActive() {
    if (localStorage.getItem("light-mode") === "true") {
        lightMode();
    }
}

function lightMode() {
    let { btnElements } = getIndexDocElements();
    for (let i = 0; i < btnElements.length; i++) {
        let lightModeAdded = btnElements[i].classList.toggle("dark-icon");
        if (!lightModeAdded) {
            toggleCheck = false;
            localStorage.setItem("light-mode", toggleCheck);
        }
        else {
            toggleCheck = true;
            localStorage.setItem("light-mode", toggleCheck);
        }
    }
}
function getIndexDocElements() {
    let btnElements = document.querySelectorAll(".material-symbols-outlined");
    return { btnElements };

}

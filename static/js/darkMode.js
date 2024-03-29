document.addEventListener("DOMContentLoaded", init);

function init() {
    let darkToggle = document.getElementById("dark-icon");
    darkToggle.addEventListener("click", darkMode);
    console.log(darkToggle)
    checkDarkActive();
}

let toggleCheck = false;

function checkDarkActive() {
    if (localStorage.getItem("dark-mode") === "true") {
        darkMode();
    }
}

function darkMode() {
    let { btnElements } = getIndexDocElements();
    for (let i = 0; i < btnElements.length; i++) {
        let darkModeAdded = btnElements[i].classList.toggle("dark-icon");
        if (!darkModeAdded) {
            toggleCheck = false;
            localStorage.setItem("dark-mode", toggleCheck);
        }
        else {
            toggleCheck = true;
            localStorage.setItem("dark-mode", toggleCheck);
        }
    }
}
function getIndexDocElements() {
    let btnElements = document.querySelectorAll(".material-symbols-outlined");
    return { btnElements };

}

// function connectionIndex(){
//     console.log("The connection works index page.")
// }

// function connectionTrainer(){
//     console.log("The connection works trainer page.")
// }

// function connectionSchedule(){
//     console.log("The connection works Schedule page.")
// }
// function connectionVideos(){
//     console.log("The connection works Schedule page.")
// }

// function connectionContact(){
//     console.log("The connection works Schedule page.")
// }
const div = document.getElementsByClassName("proj");

for(let i=0; i<div.length; i++) {
    div[i].addEventListener("click", function() {
        div[i].classList.toggle("larger");
    })
}
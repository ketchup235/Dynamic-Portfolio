const proj = document.getElementsByClassName("proj");
const details= document.getElementsByClassName("details");


for(let i=0; i<proj.length; i++) {
    proj[i].addEventListener("click", function() {
        proj[i].classList.toggle("larger");
        details[i].classList.toggle("visible");
    })
}
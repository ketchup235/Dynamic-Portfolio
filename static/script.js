const proj = document.getElementsByClassName("proj");
const details= document.getElementsByClassName("details");
const typed = new Typed('#typed', {
    strings: ["Kasyap Tumuluri"],
    startDelay: 500,
    typeSpeed: 130,     
    backSpeed: 50,       
    showCursor: true,
    cursorChar: '|',
    loop: false,
    onComplete (self) {
        self.cursor.style.visibility = 'hidden'
    }
  });

for(let i=0; i<proj.length; i++) {
    proj[i].addEventListener("click", function() {
        proj[i].classList.toggle("larger");
        details[i].classList.toggle("visible");
    })
}


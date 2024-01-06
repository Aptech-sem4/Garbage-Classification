const hiddenContent = document.querySelector("#content-to-hide"); // get the div element containing the paragraphs to be revealed
 // get all the paragraph elements inside the div
const revealedContent = document.querySelector("#content-to-reveal"); // get the div element that will show the typing effect

let i = 0; // initialize a counter variable
let speed = 50; // set the typing speed

function type() {
    const paragraphs = hiddenContent.querySelectorAll("p");
    if (i < paragraphs.length) {
        const paragraph = document.createElement("p"); // create a new paragraph element
        revealedContent.appendChild(paragraph); // add the new paragraph to the revealed content div

        const text = paragraphs[i].innerText; // get the text content of the current paragraph
        const letters = text.split(""); // split the text into an array of individual letters

        let j = 0; // initialize another counter variable

        const intervalId = setInterval(() => {
        if (j < letters.length) {
            paragraph.innerHTML += letters[j]; // add the next letter to the paragraph
            j++; // increment the counter variable
        } else {
            clearInterval(intervalId); // stop the interval once all the letters have been added
            i++; // increment the outer counter variable to move on to the next paragraph
            type(); // call the type function recursively to start typing the next paragraph immediately
        }
        }, speed);
    }
}

function render_text(str) {
    const p = document.createElement("p");
    p.innerHTML = str
    hiddenContent.innerHTML = p
    hiddenContent.style.display = "none"; // hide the original content
    revealedContent.style.display = "block"; // show the revealed content
    type(); // start the typing effect
}

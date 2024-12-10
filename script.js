// Create the starfield effect
const numberOfStars = 1000;
const starField = document.createElement('div');
starField.classList.add('background-react');
document.body.appendChild(starField);

// Generate random stars
for (let i = 0; i < numberOfStars; i++) {
    const star = document.createElement('div');
    star.classList.add('star');
    star.style.left = `${Math.random() * 100}vw`; // Random X position
    star.style.top = `${Math.random() * 100}vh`; // Random Y position
    starField.appendChild(star);
}

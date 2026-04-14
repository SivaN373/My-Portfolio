// Contact Form Submit
document.getElementById("contactForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const formData = new FormData(this);

    try {
        const response = await fetch("/contact", {
            method: "POST",
            body: formData
        });

        const result = await response.json();

        alert(result.message);
        this.reset();

    } catch (error) {
        alert("Something went wrong!");
    }
});


// Mobile Menu Toggle
const toggle = document.getElementById('nav-toggle');
const nav = document.getElementById('nav-menu');

if (toggle) {
    toggle.addEventListener('click', () => {
        nav.classList.toggle('show');
    });
}
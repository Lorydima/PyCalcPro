document.addEventListener("DOMContentLoaded", () => {
    const cards = document.querySelectorAll(".card");

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
                observer.unobserve(entry.target); // Rimuove l'osservazione per migliorare le prestazioni
            }
        });
    }, { threshold: 0.1 }); // La card diventa visibile quando il 10% è nella viewport

    cards.forEach(card => observer.observe(card));
});
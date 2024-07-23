document.addEventListener('DOMContentLoaded', function() {
    // Toggle the navigation menu on small screens
    const menuButton = document.querySelector('.menu-bar');
    const navLinks = document.querySelector('nav ul');

    if (menuButton) {
        menuButton.addEventListener('click', function() {
            navLinks.classList.toggle('show');
        });
    }

    // Smooth scrolling for internal links
    const links = document.querySelectorAll('a[href^="#"]');

    links.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
});clearInterval
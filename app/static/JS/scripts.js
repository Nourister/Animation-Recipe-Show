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
});

function toggleLoginForm() {
    document.getElementById('login-form').classList.toggle('active');
    document.getElementById('register-form').classList.remove('active');
}

// Function to handle automatic dismissal of alerts after a specified time
function dismissAlerts() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(function() {
            alert.remove();
        }, 3000); // Adjust timeout value as needed
    });
}

// Call dismissAlerts function when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', dismissAlerts);
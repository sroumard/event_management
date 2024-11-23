// Menu Burger
const menuBurger = document.querySelector('.menu-burger');
const mobileMenu = document.querySelector('.mobile-menu');
const body = document.body;

// Lorsque le bouton du menu burger est cliqué
menuBurger.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden'); // Toggle pour afficher/masquer le menu mobile
    body.classList.toggle('no-scroll');   // Toggle pour désactiver/activer le scroll du body
});

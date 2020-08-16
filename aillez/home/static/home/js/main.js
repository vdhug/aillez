
document.addEventListener('DOMContentLoaded', () => {
    const menuWrapper = document.querySelector(".menu-wrapper");

    if (menuWrapper) {

        menuWrapper.addEventListener("click", () => {
            const hamburger = document.querySelector(".hamburger-menu");
            const menu = document.querySelector(".menu-mobile");
            hamburger.classList.toggle("animate");
            menu.classList.toggle("active");
        });
    }
    
});
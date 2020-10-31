function burgerMenu(selector) {
    let menu = $(selector);
    let button = menu.find('.menu-btn');
    let links = menu.find('.menu-link');

    button.on('click', (e) => {
    e.preventDefault();
    toggleMenu();
    });
    links.on('click', () => toggleMenu());

    function toggleMenu(){
        menu.toggleClass('menu-btn_active');
        }

}

burgerMenu(".section");
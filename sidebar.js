document.addEventListener("DOMContentLoaded", () => {
    const menuItems = document.querySelectorAll(".menu-item > a");

    menuItems.forEach(item => {
        item.addEventListener("click", e => {
            e.preventDefault();
            const parent = item.parentElement;

            // Cerrar todos los demás
            document.querySelectorAll(".menu-item").forEach(menu => {
                if (menu !== parent) {
                    menu.classList.remove("open");
                }
            });

            // Alternar el actual
            parent.classList.toggle("open");
        });
    });
});




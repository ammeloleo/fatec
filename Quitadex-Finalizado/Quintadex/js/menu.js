document.addEventListener('DOMContentLoaded', function() {
    const menuButton = document.getElementById('menuHamburguer');
    const navMenu = document.getElementById('navMenu');
    
    // Função para alternar o menu
    function toggleMenu() {
        const isExpanded = menuButton.getAttribute('aria-expanded') === 'true';
        menuButton.setAttribute('aria-expanded', !isExpanded);
        navMenu.classList.toggle('active');
        document.body.style.overflow = isExpanded ? 'auto' : 'hidden';
        
        // Alternar ícone
        const icon = menuButton.querySelector('i');
        icon.classList.toggle('fa-bars');
        icon.classList.toggle('fa-times');
    }
    
    // Evento de clique no botão
    menuButton.addEventListener('click', function(e) {
        e.stopPropagation(); // Impede a propagação
        toggleMenu();
    });
    
    // Fechar ao clicar em um link
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', toggleMenu);
    });
    
    // Fechar ao clicar fora
    document.addEventListener('click', function(e) {
        if (navMenu.classList.contains('active') && 
            !navMenu.contains(e.target) && 
            e.target !== menuButton) {
            toggleMenu();
        }
    });
    
    // Fechar ao pressionar ESC
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && navMenu.classList.contains('active')) {
            toggleMenu();
        }
    });
});
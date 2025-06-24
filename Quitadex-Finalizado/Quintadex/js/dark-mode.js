// Inicialização do Modo Escuro
document.addEventListener('DOMContentLoaded', () => {
    const darkModeAtivo = localStorage.getItem('darkMode') === 'true'
    const styleElement = document.getElementById('dark-mode-style')
    const btnModo = document.getElementById('btnModo')
    
    if (darkModeAtivo) {
        styleElement.disabled = false
        document.body.classList.add('dark-mode')
        if (btnModo) btnModo.textContent = '☀️ Modo Claro'
    }
})
// Sistema de Listas
class ListaManager {
    constructor() {
        this.listas = JSON.parse(localStorage.getItem('listas')) || []
        this.itens = JSON.parse(localStorage.getItem('itens')) || {}
        this.listaAtual = null
    }

    criarLista(nome) {
        const novaLista = {
            id: Date.now(),
            nome: nome,
            criadaEm: new Date().toISOString()
        }
        this.listas.push(novaLista)
        this.salvar()
        return novaLista
    }

    removerLista(id) {
        this.listas = this.listas.filter(l => l.id !== id)
        delete this.itens[id]
        this.salvar()
    }

    adicionarItem(listaId, item) {
        if (!this.itens[listaId]) this.itens[listaId] = []
        this.itens[listaId].push(item)
        this.salvar()
    }

    atualizarQuantidade(listaId, itemId, novaQuantidade) {
        if (this.itens[listaId]) {
            const item = this.itens[listaId].find(i => i.id === itemId)
            if (item) {
                item.quantidade = novaQuantidade
                this.salvar()
            }
        }
    }

    salvar() {
        localStorage.setItem('listas', JSON.stringify(this.listas))
        localStorage.setItem('itens', JSON.stringify(this.itens))
    }
}

// Sistema de Interface
class UI {
    constructor() {
        this.manager = new ListaManager()
        this.initEventos()
        this.carregarListas()
        this.verificarModoEscuro()
    }

    verificarModoEscuro() {
        const darkModeAtivo = localStorage.getItem('darkMode') === 'true'
        const btnModo = document.getElementById('btnModo')
        if (btnModo) {
            btnModo.textContent = darkModeAtivo ? '☀️ Modo Claro' : '🌙 Modo Escuro'
        }
    }

    initEventos() {
        // Modo Escuro
        document.getElementById('btnModo').addEventListener('click', () => {
            const darkModeStyle = document.getElementById('dark-mode-style')
            const estaAtivo = darkModeStyle.disabled
            darkModeStyle.disabled = !estaAtivo
            document.body.classList.toggle('dark-mode', estaAtivo)
            localStorage.setItem('darkMode', estaAtivo)
            
            // Atualiza o texto do botão
            const btnModo = document.getElementById('btnModo')
            btnModo.textContent = estaAtivo ? '☀️ Modo Claro' : '🌙 Modo Escuro'
        })

        document.getElementById('selecionar-lista').addEventListener('change', (e) => {
            this.manager.listaAtual = e.target.value ? parseInt(e.target.value) : null
            this.carregarItens()
        })

        // Nova Lista
        document.getElementById('btnNovaLista').addEventListener('click', () => {
            const nome = prompt('Nome da nova lista:')
            if (nome) {
                const lista = this.manager.criarLista(nome)
                this.carregarListas()
                this.selecionarLista(lista.id)
            }
        })

        // Remover Lista
        document.getElementById('btnRemoverLista').addEventListener('click', () => {
            const select = document.getElementById('selecionar-lista')
            if (select.value && confirm('Tem certeza?')) {
                this.manager.removerLista(parseInt(select.value))
                this.carregarListas()
            }
        })

        // Categorias
        document.querySelectorAll('.Imgs').forEach(img => {
            img.addEventListener('click', () => {
                if (!this.manager.listaAtual) {
                    alert('Selecione uma lista primeiro!')
                    return
                }

                const item = prompt(`Item de ${img.dataset.categoria}:`)
                if (item) {
                    this.manager.adicionarItem(this.manager.listaAtual, {
                        nome: item,
                        quantidade: 1,
                        categoria: img.dataset.categoria,
                        id: Date.now()
                    })
                    this.carregarItens()
                }
            })
        })
    }

    carregarListas() {
        const select = document.getElementById('selecionar-lista')
        select.innerHTML = '<option value="">Selecione uma lista</option>'

        this.manager.listas.forEach(lista => {
            const option = document.createElement('option')
            option.value = lista.id
            option.textContent = lista.nome
            select.appendChild(option)
        })
    }

    selecionarLista(id) {
        this.manager.listaAtual = id
        this.carregarItens()
    }

    carregarItens() {
        const container = document.getElementById('itens-lista')
        container.innerHTML = ''

        if (!this.manager.listaAtual) return

        const itens = this.manager.itens[this.manager.listaAtual] || []
        itens.forEach(item => {
            const div = document.createElement('div')
            div.className = 'item-lista'
            div.dataset.id = item.id
            div.innerHTML = `
                <span>${item.nome} - ${item.categoria}</span>
                <div class="controle-quantidade">
                    <button class="btn-diminuir">-</button>
                    <input type="number" value="${item.quantidade}" min="1" class="quantidade-item">
                    <button class="btn-aumentar">+</button>
                </div>
                <button class="btn-remover">❌</button>
            `
            container.appendChild(div)

            // Eventos para controle de quantidade
            div.querySelector('.btn-diminuir').addEventListener('click', () => {
                const input = div.querySelector('.quantidade-item')
                if (input.value > 1) {
                    input.value--
                    this.manager.atualizarQuantidade(this.manager.listaAtual, item.id, parseInt(input.value))
                }
            })

            div.querySelector('.btn-aumentar').addEventListener('click', () => {
                const input = div.querySelector('.quantidade-item')
                input.value++
                this.manager.atualizarQuantidade(this.manager.listaAtual, item.id, parseInt(input.value))
            })

            div.querySelector('.quantidade-item').addEventListener('change', (e) => {
                const novaQuantidade = parseInt(e.target.value) || 1
                e.target.value = novaQuantidade
                this.manager.atualizarQuantidade(this.manager.listaAtual, item.id, novaQuantidade)
            })

            div.querySelector('.btn-remover').addEventListener('click', () => {
                this.removerItem(item.id)
            })
        })
    }
    removerItem(itemId) {
        if (!this.manager.listaAtual) return

        this.manager.itens[this.manager.listaAtual] =
            this.manager.itens[this.manager.listaAtual].filter(item => item.id !== itemId)
        this.manager.salvar()
        this.carregarItens()
    }
}

document.querySelectorAll('.Imgs').forEach(item => {
    item.addEventListener('touchstart', function() {
        this.classList.add('active');
    });
    
    item.addEventListener('touchend', function() {
        this.classList.remove('active');
    });
});


document.querySelector('.produtos').addEventListener('touchstart', function(e) {
    this.style.scrollSnapType = 'none';
});

document.querySelector('.produtos').addEventListener('touchend', function(e) {
    this.style.scrollSnapType = 'x mandatory';
});

// Inicialização
document.addEventListener('DOMContentLoaded', () => {
    new UI()
})
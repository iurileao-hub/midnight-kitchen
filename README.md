<p align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/status-completo-brightgreen.svg" alt="Status: Completo">
  <img src="https://img.shields.io/badge/rich-terminal%20UI-purple.svg" alt="Rich Terminal UI">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT License">
</p>

<h1 align="center">
  深夜食堂<br>
  <sub>Midnight Kitchen</sub>
</h1>

<p align="center">
  <em>Um jogo narrativo de terminal sobre culpa, memoria e perdao.</em><br>
  <em>Ambientado 10 anos antes de Midnight Diner.</em>
</p>

---

## A Historia

Voce e o **Master**, dono de um pequeno restaurante em Tokyo que funciona de meia-noite as 7h da manha. Ha 10 anos, um incendio destruiu o restaurante do seu mentor, Takeshi — e ele morreu naquela noite.

Voce carrega uma cicatriz no rosto. E uma culpa que nunca conseguiu superar.

Durante **7 noites**, clientes antigos retornam. Cada um carrega um fragmento daquela noite. Atraves de conversas cuidadosas e pratos preparados com intencao, voce descobre a verdade sobre o incendio — e sobre si mesmo.

## Screenshots

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│     "Nao fotografo mais pessoas. So paisagens agora."       │
│                                                             │
│     Yuki olha para a camera antiga no seu pescoco.          │
│     Os dedos tracam o contorno gasto da alca de couro.      │
│                                                             │
│     "Coisas que nao mudam enquanto voce olha pra elas."     │
│                                                             │
└───────────────────────────────────────────── ⏱ 2:15 ────────┘

┌─ O que voce diz? ───────────────────────────────────────────┐
│                                                             │
│  1. "Paisagens sao bonitas mesmo."                          │
│  2. "Pessoas mudam rapido demais?"                          │
│  3. "Algo aconteceu enquanto voce fotografava alguem?"      │
│  4. [Continua trabalhando em silencio]                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Mecanicas

| Mecanica | Descricao |
|----------|-----------|
| **7 Noites** | 6 clientes + 1 noite de reflexao final |
| **Sistema de Confianca** | Fechado → Cauteloso → Curioso → Aberto → Vulneravel |
| **Prato como Gatilho** | Descubra o prato certo → Sirva → Memoria revelada |
| **Consequencias** | Suas escolhas importam — voce pode falhar |
| **Multiplos Finais** | Perfeito, Bom, Neutro ou Ruim |

## Os Clientes

| Noite | Cliente | Quem e | Conexao com o Incendio |
|:-----:|---------|--------|------------------------|
| 1 | **Yuki Tanabe** | Fotografa, 28 anos | Fotografou o incendio |
| 2 | **Tanaka Kenji** | Ex-bombeiro, 58 anos | Tentou salvar Takeshi |
| 3 | **Ryo Ishida** | Taxista, 35 anos | Era garcom do restaurante |
| 4 | **Midori Sato** | Florista aposentada, 67 anos | Vizinha que viu faiscas |
| 5 | **Sachiko Yamamoto** | Contadora, 32 anos | Filha de Takeshi |
| 6 | **Hiroto Kimura** | Estudante, 18 anos | Crianca salva por Master |
| 7 | *Reflexao* | — | Master confronta a verdade |

## Instalacao

```bash
# Clone o repositorio
git clone https://github.com/seu-usuario/midnight-kitchen.git
cd midnight-kitchen

# Instale as dependencias
pip install -r requirements.txt

# Jogue
python3 main.py
```

### Requisitos

- Python 3.8+
- Terminal com suporte a cores (a maioria dos terminais modernos)

## Estrutura do Projeto

```
midnight-kitchen/
├── main.py              # Ponto de entrada
├── config.py            # Configuracoes globais
├── contracts.py         # Tipos e interfaces
│
├── core/                # Nucleo do jogo
│   ├── game.py          # Estado global
│   ├── menu.py          # Menu inicial + save
│   ├── noite.py         # Orquestrador de noites
│   ├── scene.py         # Gerenciador de cenas
│   ├── tempo.py         # Sistema de tempo
│   └── save.py          # Sistema de save
│
├── sistemas/            # Logica de jogo
│   ├── dialogo.py       # Sistema de dialogo
│   ├── cozinha.py       # Sistema de cozinha
│   └── reflexao.py      # Dia 7 + finais
│
├── narrativa/           # Conteudo narrativo
│   ├── abertura.py      # Textos de abertura
│   └── onboarding.py    # Tutorial
│
├── dados/               # Dados em JSON
│   ├── clientes/        # 6 clientes
│   ├── dialogos/        # Arvores de dialogo (~600 nos)
│   └── pratos.json      # Receitas
│
├── ui/                  # Interface Rich
│   ├── styles.py        # Estilos e cores
│   ├── components.py    # Componentes UI
│   ├── ascii_art.py     # Arte ASCII
│   ├── effects.py       # Efeitos visuais
│   └── renderer.py      # Renderizacao
│
└── docs/                # Documentacao
    ├── DESIGN.md        # Design consolidado (historia, personagens, mecanicas)
    └── PROMPTS.md       # Prompts de analise narrativa
```

## Tecnologias

| Tecnologia | Uso |
|------------|-----|
| **Python 3** | Linguagem principal |
| **Rich** | Interface rica no terminal (cores, paineis, efeitos) |
| **JSON** | Dados de clientes, dialogos e pratos |

## Conceitos Praticados

- [x] Classes e Programacao Orientada a Objetos
- [x] Dicionarios e estruturas de dados
- [x] Listas e manipulacao de colecoes
- [x] Funcoes e modularizacao
- [x] Controle de versao com Git
- [x] Leitura/escrita de arquivos JSON
- [x] Design de sistemas de dialogo
- [x] Narrativa interativa

## Inspiracao

Baseado na serie de TV **Midnight Diner** (深夜食堂 *Shinya Shokudo*), criada por Yaro Abe. Este jogo conta a pre-historia da serie, explorando a origem da cicatriz de Master atraves de uma narrativa interativa.

## Contexto

Projeto desenvolvido como parte do **Portfolio Project: Python Terminal Game** do curso CS 101 da Codecademy, expandido para uma experiencia narrativa completa.

## Autor

**Iuri Leao de Almeida**
Projeto desenvolvido como parte da transicao para Ciencia da Computacao (FIAP 2026-2030)

## Licenca

Este projeto esta licenciado sob a [MIT License](LICENSE).

---

<p align="center">
  <em>"Todo mundo tem uma historia. Alguns so precisam do prato certo para conta-la."</em>
</p>

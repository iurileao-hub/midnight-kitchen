# Midnight Kitchen

Um jogo narrativo de terminal em Python, ambientado **10 anos antes** da serie *Midnight Diner*.

## A Historia

Voce e o **Master**, dono de um pequeno restaurante em Tokyo que funciona de meia-noite as 7h da manha. Ha 10 anos, um incendio destruiu o restaurante do seu mentor, Takeshi — e ele morreu naquela noite. Voce carrega uma cicatriz e uma culpa que nunca conseguiu superar.

Durante **7 noites**, clientes antigos retornam. Cada um carrega um fragmento daquela noite. Atraves de conversas e pratos preparados com cuidado, voce descobre a verdade sobre o incendio — e sobre si mesmo.

## Mecanicas

- **7 dias:** 6 clientes + 1 noite de reflexao
- **Estados emocionais:** fechado -> cauteloso -> aberto -> vulneravel
- **Prato como gatilho:** Descubra o prato favorito -> Sirva -> Memoria revelada
- **Pode falhar:** Maximo 1 falha para o final bom
- **Envelope de Yuki:** So existe se a primeira noite foi sucesso

## Os Clientes

| Dia | Cliente | Conexao com o Incendio |
|-----|---------|------------------------|
| 1 | Yuki Tanabe (28, fotografa) | Fotografou o incendio |
| 2 | Tanaka Kenji (58, ex-bombeiro) | Tentou salvar Takeshi |
| 3 | Ryo Ishida (35, taxista) | Era garcom do restaurante |
| 4 | Midori Sato (67, florista) | Vizinha que viu faiscas |
| 5 | Sachiko Yamamoto (32, contadora) | Filha de Takeshi |
| 6 | Hiroto Kimura (18, estudante) | Crianca salva por Master |
| 7 | *Reflexao* | Master confronta a verdade |

## Requisitos

- Python 3.8+
- Nenhuma dependencia externa (stdlib apenas)

## Como Jogar

```bash
python3 main.py
```

## Estrutura do Projeto

```
midnight-kitchen/
├── models/                 # Classes base
│   ├── cliente.py          # Visitante do restaurante
│   ├── prato.py            # Receita preparavel
│   ├── memoria.py          # Fragmento do passado
│   └── jogo.py             # Estado central do jogo
├── sistemas/               # Sistemas de gameplay (Fase 2)
│   ├── dialogo.py          # Sistema de conversas
│   ├── cozinha.py          # Preparacao de pratos
│   └── reflexao.py         # Logica do dia 7
├── dados/                  # Arquivos de dados (Fase 3)
│   └── clientes.json       # Dados dos clientes
├── docs/
│   ├── ARQUITETURA_v3.md   # Arquitetura atual
│   ├── PERSONAGENS_PROPOSTA.md
│   └── DESIGN.md
└── CLAUDE.md               # Instrucoes para o tutor
```

## Contexto do Projeto

Este projeto faz parte do **Portfolio Project: Python Terminal Game** do curso CS 101 da Codecademy.

### Conceitos Praticados

- [x] Classes e Programacao Orientada a Objetos
- [x] Dicionarios e estruturas de dados
- [x] Listas e manipulacao de colecoes
- [x] Funcoes e modularizacao
- [x] Controle de versao com Git
- [ ] Leitura/escrita de arquivos JSON

## Autor

**Dr. Iuri Leao de Almeida**
Projeto desenvolvido como parte da transicao para Ciencia da Computacao (FIAP 2026-2030)

## Licenca

MIT License

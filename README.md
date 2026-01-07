# Midnight Kitchen 🌙

Um jogo narrativo de terminal em Python, inspirado na série japonesa *Midnight Diner* (深夜食堂).

## Sobre o Jogo

Você é o **Master**, dono de um pequeno restaurante em Tokyo que funciona de meia-noite às 7h da manhã. Cada noite, clientes chegam com fome — e com histórias. Através de conversas e pratos cuidadosamente preparados, você descobre seus segredos e, aos poucos, relembra fragmentos do seu próprio passado.

### Estrutura

- **5 noites** de gameplay
- **4 clientes** com histórias únicas
- **1 mistério central** que conecta tudo
- **Sistema de culinária** com receitas e ingredientes

## Requisitos

- Python 3.8+
- Nenhuma dependência externa (stdlib apenas)

## Como Jogar

```bash
python main.py
```

## Estrutura do Projeto

```
midnight-kitchen/
├── main.py              # Ponto de entrada do jogo
├── models/              # Classes do domínio
│   ├── cliente.py       # Classe Cliente
│   ├── prato.py         # Classe Prato e sistema de receitas
│   ├── restaurante.py   # Estado do jogo
│   └── memoria.py       # Fragmentos de memória do Master
├── sistemas/            # Sistemas de gameplay
│   ├── dialogo.py       # Sistema de conversas
│   ├── cozinha.py       # Sistema de preparação de pratos
│   └── revelacao.py     # Lógica da noite final
├── dados/               # Arquivos de dados
│   ├── clientes.json    # Dados e diálogos dos clientes
│   ├── pratos.json      # Receitas e significados
│   └── memorias.json    # Fragmentos da história do Master
└── docs/
    ├── DESIGN.md        # Arquitetura e decisões de design
    └── APRENDIZAGEM.md  # Plano de aprendizagem
```

## Contexto do Projeto

Este projeto faz parte do **Portfolio Project: Python Terminal Game** do curso CS 101 da Codecademy.

### Conceitos Praticados

- [x] Classes e Programação Orientada a Objetos
- [x] Dicionários e estruturas de dados
- [x] Listas e manipulação de coleções
- [x] Funções e modularização
- [x] Controle de versão com Git
- [x] Leitura/escrita de arquivos JSON

## Autor

**Dr. Iuri Leão de Almeida**
Projeto desenvolvido como parte da transição para Ciência da Computação (FIAP 2026-2030)

## Licença

MIT License

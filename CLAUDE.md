# CLAUDE.md — Midnight Kitchen v2.0

## Sobre o Projeto

**Midnight Kitchen** e um jogo narrativo de terminal em Python.
Se passa **10 anos antes** da serie *Midnight Diner*.
Conta a historia de origem da **cicatriz de Master**.

**Status atual:** Refatoracao para versao de alta qualidade.

---

## Fase Atual: Refatoracao v2.0

O prototipo funcional esta completo. Agora estamos elevando o jogo
para uma versao **apresentavel a jogadores reais**.

### Objetivos

1. **Interface elegante** com `rich` (cores, paineis, efeitos)
2. **Narrativa imersiva** com prosa atmosferica
3. **Dialogos profundos** unicos para cada personagem
4. **Sistema de pistas** que recompensa atencao
5. **Experiencia emocional** genuina

### Documentacao Principal

```
docs/
├── VISAO_v2.md       # Visao de produto e arquitetura
├── NARRATIVA.md      # Guia de escrita e tom
└── PERSONAGENS.md    # Perfis detalhados dos 6 clientes
```

---

## Estrutura do Projeto (Atual)

```
midnight-kitchen/
├── main.py              # Loop principal (v1 - sera refatorado)
├── models/
│   ├── cliente.py       # Classe Cliente
│   ├── prato.py         # Classe Prato
│   ├── memoria.py       # Classe Memoria
│   └── jogo.py          # Estado do jogo
├── sistemas/
│   ├── dialogo.py       # Sistema de dialogo (sera expandido)
│   ├── cozinha.py       # Sistema de cozinha
│   └── reflexao.py      # Dia 7 - reflexao
├── dados/
│   └── clientes.json    # Dados dos clientes (sera expandido)
└── docs/
    ├── VISAO_v2.md      # Visao da refatoracao
    ├── NARRATIVA.md     # Guia de narrativa
    └── PERSONAGENS.md   # Perfis dos personagens
```

---

## Estrutura Planejada (v2.0)

```
midnight-kitchen/
├── main.py
├── config.py            # Configuracoes globais
├── requirements.txt     # Dependencias (rich)
│
├── core/                # NOVO - Nucleo do jogo
│   ├── game.py          # Loop e estado
│   ├── scene.py         # Gerenciador de cenas
│   └── renderer.py      # Renderizacao
│
├── models/              # Entidades (expandir)
├── sistemas/            # Logica (expandir)
│
├── narrativa/           # NOVO - Conteudo narrativo
│   ├── ambientacao.py
│   ├── monologos.py
│   └── transicoes.py
│
├── dados/               # Expandir com dialogos por personagem
│   ├── clientes/
│   │   ├── yuki.json
│   │   └── ...
│   ├── dialogos/
│   │   ├── yuki_dialogos.json
│   │   └── ...
│   └── pratos.json
│
├── ui/                  # NOVO - Interface
│   ├── styles.py
│   ├── components.py
│   ├── ascii_art.py
│   └── effects.py
│
└── docs/
```

---

## Fases da Refatoracao

### Fase 1: Infraestrutura UI
- [ ] Instalar `rich`
- [ ] Criar sistema de renderizacao
- [ ] Implementar componentes visuais
- [ ] Arte ASCII elaborada

### Fase 2: Narrativa Base
- [ ] Reescrever ambientacao
- [ ] Monologos de Master
- [ ] Descricoes expandidas
- [ ] Transicoes entre cenas

### Fase 3: Sistema de Dialogo
- [ ] JSONs de dialogo por personagem
- [ ] Sistema de confianca granular
- [ ] Ramificacoes e consequencias
- [ ] Pistas e recompensas

### Fase 4: Integracao
- [ ] Conectar sistemas
- [ ] Balancear dificuldade
- [ ] Testes completos
- [ ] Polish final

---

## Comandos

```bash
# Rodar o jogo (versao atual)
python3 main.py

# Testar sistemas individuais
python3 sistemas/dialogo.py
python3 sistemas/cozinha.py
python3 sistemas/reflexao.py
```

---

## Mecanicas do Jogo

- **7 noites:** 6 clientes + 1 reflexao
- **Estados emocionais:** fechado -> cauteloso -> aberto -> vulneravel
- **Prato como gatilho:** Descobrir prato -> Servir -> Memoria
- **Sistema de falha:** Maximo 1 falha para final bom
- **Envelope:** So existe se Yuki (noite 1) foi sucesso

---

## Metodologia

Claude guia o desenvolvimento, explicando conceitos de Python
conforme implementamos. O foco agora e qualidade do produto,
com aprendizado integrado ao processo.

---

*Atualizado: 14/01/2026 — Inicio da refatoracao v2.0*

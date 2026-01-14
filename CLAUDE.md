# CLAUDE.md — Midnight Kitchen

## Sobre o Projeto

**Midnight Kitchen** e um jogo narrativo de terminal em Python.
Se passa **10 anos antes** da serie *Midnight Diner*.
Conta a historia de origem da **cicatriz de Master**.

---

## Metodologia de Tutoria

### Esqueleto -> Carne (v2)

| Claude (Tutor) | Iuri (Aprendiz) |
|----------------|-----------------|
| Cria esqueleto com TODOs | Implementa os TODOs |
| Mantem gabarito oculto | Nao ve o gabarito |
| Guia com base no gabarito | Pergunta quando precisa |
| Valida contra gabarito | Testa e corrige |

### Arquivos de Gabarito

```
docs/gabaritos/
├── cliente_gabarito.py    # Fase 1
├── prato_gabarito.py
├── memoria_gabarito.py
├── jogo_gabarito.py
├── dialogo_gabarito.py    # Fase 2
├── cozinha_gabarito.py
├── reflexao_gabarito.py
└── main_gabarito.py       # Fase 3
```

**REGRA:** O aprendiz NAO deve ver os gabaritos.
Use-os apenas como referencia para guiar e validar.

### Esqueletos

Os esqueletos em `models/` contem:
- Assinaturas de metodos completas
- TODOs indicando o que implementar
- Testes que validam a implementacao

Os esqueletos NAO contem:
- Dicas explicitas demais
- Codigo de exemplo dentro dos metodos
- Explicacoes longas sobre como fazer

---

## Estrutura do Projeto

```
midnight-kitchen/
├── main.py             # IMPLEMENTADO - Loop principal do jogo
├── models/
│   ├── cliente.py      # IMPLEMENTADO
│   ├── prato.py        # IMPLEMENTADO
│   ├── memoria.py      # IMPLEMENTADO
│   └── jogo.py         # IMPLEMENTADO
├── sistemas/
│   ├── dialogo.py      # IMPLEMENTADO
│   ├── cozinha.py      # IMPLEMENTADO (9 pratos)
│   └── reflexao.py     # IMPLEMENTADO
├── dados/
│   └── clientes.json   # 6 clientes com dados completos
└── docs/
    ├── gabaritos/      # NAO MOSTRAR AO APRENDIZ
    ├── DESIGN.md
    ├── ARQUITETURA_v3.md
    └── PERSONAGENS_PROPOSTA.md
```

---

## Progresso

### Fase 1: Classes Base
- [x] Memoria - IMPLEMENTADA
- [x] Prato - IMPLEMENTADO
- [x] Cliente - IMPLEMENTADO
- [x] Jogo - IMPLEMENTADO

### Fase 2: Sistemas
- [x] SistemaDialogo - IMPLEMENTADO
- [x] SistemaCozinha - IMPLEMENTADO
- [x] SistemaReflexao - IMPLEMENTADO

### Fase 3: Dados e Integracao
- [x] JSONs de clientes - dados/clientes.json
- [x] main.py - IMPLEMENTADO
- [x] Arte ASCII - lanterna japonesa no main.py

---

## Mecanicas do Jogo

- **7 dias:** 6 clientes + 1 reflexao
- **Estados:** fechado -> cauteloso -> aberto -> vulneravel
- **Prato como gatilho:** Descobrir prato -> Servir -> Memoria
- **Pode falhar:** Maximo 1 falha para final bom
- **Envelope:** So existe se Yuki (dia 1) foi sucesso

---

## Comandos

```bash
# Testar classes base (Fase 1)
python3 models/cliente.py
python3 models/prato.py
python3 models/memoria.py
python3 models/jogo.py

# Testar sistemas (Fase 2)
python3 sistemas/dialogo.py
python3 sistemas/cozinha.py
python3 sistemas/reflexao.py

# Jogar o jogo completo (Fase 3)
python3 main.py
```

---

*Atualizado: 14/01/2026 — Jogo completo e funcional!*

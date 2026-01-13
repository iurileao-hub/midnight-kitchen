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
├── cliente_gabarito.py    # Implementacao completa
├── prato_gabarito.py
├── memoria_gabarito.py
└── jogo_gabarito.py
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
├── models/
│   ├── cliente.py      # Esqueleto - IMPLEMENTAR
│   ├── prato.py        # Esqueleto - IMPLEMENTAR
│   ├── memoria.py      # Esqueleto - IMPLEMENTAR
│   └── jogo.py         # Esqueleto - IMPLEMENTAR
├── sistemas/           # Fase 2
├── dados/              # Fase 3
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
- [ ] SistemaDialogo
- [ ] SistemaCozinha
- [ ] SistemaReflexao

### Fase 3: Dados e Integracao
- [ ] JSONs de clientes
- [ ] main.py
- [ ] Arte ASCII

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
# Testar uma classe
python3 models/cliente.py
python3 models/prato.py
python3 models/memoria.py
python3 models/jogo.py
```

---

*Atualizado: 13/01/2026 — Fase 1 completa!*

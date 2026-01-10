# CLAUDE.md — Midnight Kitchen

Instruções para Claude Code ao trabalhar neste repositório.

---

## Sobre o Projeto

**Midnight Kitchen** é um jogo narrativo de terminal em Python, inspirado na série japonesa *Midnight Diner* (深夜食堂).

- **Tipo:** Projeto de portfólio (CS 101 Codecademy)
- **Autor:** Dr. Iuri Leão de Almeida
- **Status:** Em desenvolvimento (Fase 1 - Fundamentos)

---

## Contexto de Tutoria

Este projeto usa metodologia **"Esqueleto → Carne"**:

| Claude (Tutor) | Iuri (Aprendiz) |
|----------------|-----------------|
| Cria estrutura de arquivos | Implementa lógica de negócio |
| Define assinaturas de métodos | Escreve o corpo dos métodos |
| Faz code review | Corrige e refatora |
| Explica conceitos | Pergunta quando tem dúvidas |

**Objetivo:** Maximizar aprendizado através da prática guiada.

---

## Estrutura do Projeto

```
midnight-kitchen/
├── main.py              # Ponto de entrada (a criar)
├── models/
│   ├── __init__.py
│   ├── cliente.py       # ✅ Implementado
│   ├── prato.py         # Próximo
│   ├── restaurante.py   # Pendente
│   └── memoria.py       # Pendente
├── sistemas/
│   ├── dialogo.py       # Pendente
│   ├── cozinha.py       # Pendente
│   └── revelacao.py     # Pendente
├── dados/
│   ├── clientes.json    # Pendente
│   ├── pratos.json      # Pendente
│   └── memorias.json    # Pendente
└── docs/
    ├── DESIGN.md        # Arquitetura completa
    └── APRENDIZAGEM.md  # Plano de tutoria e progresso
```

---

## Progresso Atual

### Fase 1: Fundamentos (Classes e Objetos)
- [x] `Cliente` — classe completa com testes
- [ ] `Prato` — próximo a implementar
- [ ] `Restaurante` — pendente
- [ ] `Memoria` — pendente

### Próxima Tarefa
Criar esqueleto da classe `Prato` em `models/prato.py` para Iuri implementar.

---

## Padrões de Código

- **Linguagem:** Python 3.8+
- **Estilo:** snake_case para funções/variáveis, PascalCase para classes
- **Docstrings:** Google style com type hints
- **Testes:** Bloco `if __name__ == "__main__"` em cada módulo
- **Commits:** Português, presente do indicativo

---

## Conceitos-Chave do Jogo

- **5 noites:** 4 clientes + 1 revelação final
- **Sistema de confiança:** 0-100, ≥80 revela segredo
- **Mistério central:** Incêndio há 10 anos conecta todos os clientes ao Master
- **Mecânica de pratos:** Ingredientes → Receita → Efeito emocional

---

## Clientes Planejados

| # | Nome | Profissão | Conexão com Master |
|---|------|-----------|-------------------|
| 1 | Yuki | Fotógrafa, 28 | Fotografou o incêndio |
| 2 | Tanaka | Ex-bombeiro, 55 | Estava no incêndio |
| 3 | Hana | Estudante, 19 | Filha de vítima |
| 4 | Kenji | Detetive, 40 | Investiga o caso |

---

## Comandos Úteis

```bash
# Navegar ao projeto
cd ~/Documents/Projects/midnight-kitchen

# Rodar testes de um módulo
python3 models/cliente.py

# Ver status do git
git status

# Commit padrão
git add -A && git commit -m "Descrição em português"
```

---

## Referências

- **Documentação:** `docs/DESIGN.md` (arquitetura), `docs/APRENDIZAGEM.md` (tutoria)
- **Inspiração:** Midnight Diner (深夜食堂) — série Netflix
- **Curso:** CS 101 Codecademy — Portfolio Project

---

*Última atualização: 10/01/2026*

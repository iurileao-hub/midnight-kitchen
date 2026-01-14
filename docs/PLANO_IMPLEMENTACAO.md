# Plano de Implementacao — Sessao Unica

## Visao Geral

Este plano descreve como implementar o Midnight Kitchen v2.0 completo
em uma unica sessao de trabalho, usando automacao e paralelismo.

**Tempo estimado:** 2-4 horas de trabalho do Claude
**Resultado:** Jogo completo, testado e polido

---

## Estrategia de Implementacao

### Principio: Modulos Independentes

Dividimos o trabalho em modulos que podem ser desenvolvidos em paralelo:

```
┌─────────────────────────────────────────────────────────────────┐
│                      MODULOS PARALELOS                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │     UI      │  │  NARRATIVA  │  │   DIALOGOS  │             │
│  │  (styles,   │  │ (textos,    │  │  (JSONs por │             │
│  │  renderer)  │  │  transicoes)│  │  personagem)│             │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘             │
│         │                │                │                     │
│         └────────────────┼────────────────┘                     │
│                          ▼                                      │
│                 ┌─────────────────┐                             │
│                 │   INTEGRACAO    │                             │
│                 │   (game.py,     │                             │
│                 │    main.py)     │                             │
│                 └─────────────────┘                             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Fases de Execucao

```
FASE 1: SETUP (5 min)
    └── Instalar dependencias, criar estrutura de pastas

FASE 2: PARALELO (60-90 min)
    ├── Modulo UI (componentes visuais)
    ├── Modulo Narrativa (textos atmosfericos)
    └── Modulo Dialogos (6 JSONs de personagens)

FASE 3: CORE (30-45 min)
    └── Sistema principal (game.py, cenas, integracao)

FASE 4: INTEGRACAO (30 min)
    └── Conectar modulos, ajustar fluxo

FASE 5: TESTE E POLISH (30-45 min)
    └── Jogar, revisar, corrigir, polir
```

---

## Ferramentas Necessarias

### 1. Biblioteca Python: rich

```bash
pip install rich
```

A biblioteca `rich` fornece:
- Console com cores e estilos
- Paineis e boxes decorativos
- Efeito de digitacao (Live)
- Tabelas e markdown
- Barra de progresso

### 2. Subagentes Claude (ja disponiveis)

| Subagente | Uso |
|-----------|-----|
| `Bash` | Executar comandos, testes |
| `Explore` | Navegar codebase quando necessario |
| `feature-dev:code-reviewer` | Revisar codigo no final |

### 3. Paralelismo com Task Tool

O Claude pode executar multiplas tarefas em paralelo usando o Task tool.
Isso acelera significativamente o desenvolvimento.

---

## Estrutura de Arquivos a Criar

```
midnight-kitchen/
├── requirements.txt          # [CRIAR] Dependencias
├── config.py                 # [CRIAR] Configuracoes globais
│
├── ui/                       # [CRIAR] Interface visual
│   ├── __init__.py
│   ├── styles.py             # Cores e estilos
│   ├── components.py         # Paineis, boxes, menus
│   ├── effects.py            # Efeito de digitacao
│   └── ascii_art.py          # Arte ASCII elaborada
│
├── narrativa/                # [CRIAR] Conteudo narrativo
│   ├── __init__.py
│   ├── abertura.py           # Tela inicial e introducao
│   ├── ambientacao.py        # Descricoes de ambiente
│   ├── transicoes.py         # Entre cenas
│   └── monologos.py          # Pensamentos de Master
│
├── dados/                    # [EXPANDIR] Dados JSON
│   ├── clientes/             # [CRIAR] Um arquivo por cliente
│   │   ├── yuki.json
│   │   ├── tanaka.json
│   │   ├── ryo.json
│   │   ├── midori.json
│   │   ├── sachiko.json
│   │   └── hiroto.json
│   ├── dialogos/             # [CRIAR] Dialogos expandidos
│   │   ├── yuki.json         # 20-30 trocas unicas
│   │   ├── tanaka.json
│   │   ├── ryo.json
│   │   ├── midori.json
│   │   ├── sachiko.json
│   │   └── hiroto.json
│   └── pratos.json           # [CRIAR] Dados expandidos
│
├── core/                     # [CRIAR] Nucleo do jogo
│   ├── __init__.py
│   ├── game.py               # Estado e loop principal
│   └── scene.py              # Gerenciador de cenas
│
├── models/                   # [REFATORAR] Modelos existentes
│   ├── cliente.py            # Expandir com sistema de confianca
│   └── ...
│
├── sistemas/                 # [REFATORAR] Sistemas existentes
│   ├── dialogo.py            # Refatorar para novo sistema
│   └── ...
│
└── main.py                   # [REESCREVER] Novo ponto de entrada
```

---

## Detalhamento por Modulo

### Modulo 1: UI (ui/)

**Arquivos:** 5
**Linhas estimadas:** ~400

```python
# ui/styles.py
# Define cores, temas, estilos consistentes

# ui/components.py
# Funcoes para criar paineis, boxes, menus de escolha

# ui/effects.py
# Efeito de digitacao letra por letra

# ui/ascii_art.py
# Arte ASCII: lanterna, logo, decoracoes
```

### Modulo 2: Narrativa (narrativa/)

**Arquivos:** 4
**Linhas estimadas:** ~600

```python
# narrativa/abertura.py
# Tela de titulo, introducao atmosferica

# narrativa/ambientacao.py
# Descricoes do restaurante, clima, horarios

# narrativa/transicoes.py
# Textos entre noites, mudancas de cena

# narrativa/monologos.py
# Pensamentos internos de Master
```

### Modulo 3: Dialogos (dados/dialogos/)

**Arquivos:** 6 JSONs
**Linhas estimadas:** ~2000 (total)

Cada JSON contem:
- 20-30 nos de dialogo
- 3-4 opcoes por no
- Respostas variadas por nivel de confianca
- Pistas progressivas
- Gatilhos e consequencias

### Modulo 4: Core (core/)

**Arquivos:** 2
**Linhas estimadas:** ~300

```python
# core/game.py
# Classe Game: estado, loop, transicoes

# core/scene.py
# Gerenciador de cenas: noite, dialogo, cozinha, reflexao
```

---

## Ordem de Implementacao

### Etapa 1: Setup (Claude executa)

```bash
# 1. Criar requirements.txt
# 2. Instalar rich
# 3. Criar estrutura de pastas
# 4. Criar config.py
```

### Etapa 2: Modulo UI (Pode ser paralelo)

```
1. ui/styles.py       - Definir cores e temas
2. ui/ascii_art.py    - Arte ASCII elaborada
3. ui/components.py   - Paineis, menus
4. ui/effects.py      - Efeito de digitacao
```

### Etapa 3: Modulo Narrativa (Pode ser paralelo)

```
1. narrativa/abertura.py      - Tela inicial
2. narrativa/ambientacao.py   - Descricoes
3. narrativa/monologos.py     - Pensamentos Master
4. narrativa/transicoes.py    - Entre cenas
```

### Etapa 4: Dados JSON (Pode ser paralelo)

```
1. dados/clientes/yuki.json + dados/dialogos/yuki.json
2. dados/clientes/tanaka.json + dados/dialogos/tanaka.json
3. ... (outros 4 clientes)
4. dados/pratos.json (expandido)
```

### Etapa 5: Core e Integracao

```
1. core/game.py          - Estado do jogo
2. core/scene.py         - Gerenciador de cenas
3. Refatorar sistemas/   - Adaptar para novo fluxo
4. Reescrever main.py    - Novo ponto de entrada
```

### Etapa 6: Teste e Polish

```
1. Executar jogo completo
2. Revisar com code-reviewer
3. Corrigir bugs
4. Ajustar textos
5. Commit final
```

---

## Comandos para o Usuario

### Antes de Comecar

Voce nao precisa habilitar nenhum plugin especial.
As ferramentas necessarias ja estao disponiveis:

- **Task tool** - Para paralelizar trabalho
- **Bash** - Para executar comandos
- **Read/Write/Edit** - Para manipular arquivos
- **feature-dev:code-reviewer** - Para revisao final

### Como Iniciar

Basta dizer:

> "Vamos comecar a implementacao. Execute o plano."

Ou, se preferir acompanhar fase por fase:

> "Vamos comecar pela Fase 1: Setup"

### Durante a Implementacao

Voce pode:
- Observar o progresso
- Fazer ajustes pontuais
- Pedir explicacoes sobre o codigo
- Testar o jogo a qualquer momento

---

## Estimativa de Trabalho

| Fase | Tempo | Paralelismo |
|------|-------|-------------|
| Setup | 5 min | - |
| UI | 20-30 min | Sim |
| Narrativa | 30-40 min | Sim |
| Dialogos | 40-60 min | Sim |
| Core | 20-30 min | Nao |
| Integracao | 20-30 min | Nao |
| Teste/Polish | 20-30 min | Nao |
| **Total** | **2-4 horas** | |

**Nota:** Com paralelismo maximo, o tempo real pode ser menor.

---

## Checkpoints

### Checkpoint 1: Setup Completo
- [ ] requirements.txt criado
- [ ] rich instalado
- [ ] Pastas criadas
- [ ] config.py funcional

### Checkpoint 2: UI Funcional
- [ ] Efeito de digitacao funcionando
- [ ] Paineis renderizando
- [ ] Arte ASCII visivel
- [ ] Cores aplicadas

### Checkpoint 3: Narrativa Pronta
- [ ] Abertura implementada
- [ ] Ambientacao por noite
- [ ] Monologos de Master
- [ ] Transicoes fluidas

### Checkpoint 4: Dialogos Completos
- [ ] 6 JSONs de clientes
- [ ] 6 JSONs de dialogos
- [ ] Sistema de confianca
- [ ] Pistas funcionando

### Checkpoint 5: Jogo Jogavel
- [ ] Loop principal funciona
- [ ] Todas as noites acessiveis
- [ ] Dia 7 funcional
- [ ] Finais diferentes

### Checkpoint 6: Versao Final
- [ ] Revisao de codigo feita
- [ ] Bugs corrigidos
- [ ] Textos revisados
- [ ] Commit final

---

## Resultado Esperado

Ao final da sessao, voce tera:

1. **Jogo completo e jogavel** via `python3 main.py`
2. **Interface elegante** com cores, paineis, efeitos
3. **Narrativa imersiva** que envolve o jogador
4. **6 noites unicas** com dialogos profundos
5. **Sistema de pistas** que recompensa atencao
6. **3 finais diferentes** baseados nas escolhas
7. **Codigo limpo** e bem organizado

---

*Plano criado em 14/01/2026*
*Pronto para execucao*

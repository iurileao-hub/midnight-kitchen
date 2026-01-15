# Midnight Kitchen v2.0 — Visao de Produto

## Objetivo

Transformar o prototipo funcional em uma **experiencia narrativa de alta qualidade**,
digna de ser apresentada a jogadores reais e servir como portfolio.

---

## Pilares da Refatoracao

### 1. Interface CLI Elegante

**Antes:** Texto simples com separadores basicos
**Depois:** Interface estilizada com cores, boxes, animacoes de texto

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  ░░░░░                    N O I T E  1                      │
│ ░░░░░░░                                                     │
│  ░░░░░    A cortina de noren balanca suavemente.            │
│    ║║     Passos leves no beco de pedra.                    │
│ ═══╩╩═══                                                    │
│                                                             │
│  Uma jovem entra. Carrega uma camera antiga no pescoco      │
│  e um envelope amarelado na bolsa. Seus olhos percorrem     │
│  o restaurante antes de se sentar no canto do balcao.       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Tecnologias:**
- `rich` — biblioteca Python para terminal rico (cores, paineis, tabelas, markdown)
- Efeito de digitacao (texto aparecendo letra por letra)
- Transicoes suaves entre cenas
- Arte ASCII mais elaborada e contextual

---

### 2. Narrativa Imersiva

**Antes:** Descricoes curtas e funcionais
**Depois:** Prosa atmosferica que evoca os sentidos

**Exemplo — Entrada de Yuki:**

```
ANTES:
"Uma jovem de olhar melancolico entra."

DEPOIS:
O sino da porta tilinta suavemente.

Uma jovem aparece na fresta da cortina de noren, hesitante.
Veste um casaco cinza desbotado, e no pescoco carrega uma
camera antiga — uma Pentax dos anos 80, com a alca de couro
gasta pelo tempo.

Ela percorre o restaurante com os olhos antes de entrar.
Conta os lugares. Avalia as saidas. So entao se aproxima
do balcao, escolhendo o banco mais distante de voce.

No silencio que se instala, voce nota: ela segura a bolsa
com forca, como se protegesse algo precioso — ou perigoso.
```

**Elementos narrativos:**
- Descricoes sensoriais (visao, som, cheiro, toque)
- Detalhes que revelam personalidade
- Tensao e misterio sutis
- Voz narrativa em segunda pessoa ("voce nota...")

---

### 3. Sistema de Dialogo Profundo

**Antes:** Opcoes genericas por estado emocional
**Depois:** Dialogos unicos para cada personagem, com multiplas camadas

#### Estrutura de Dialogo por Personagem

Cada cliente tem (IMPLEMENTADO):
- **86-111 nos de dialogo unicos** (592 total no jogo)
- **3-4 opcoes por momento**, cada uma com consequencias diferentes
- **Pistas sutis** que o jogador precisa perceber
- **Respostas que variam** conforme o nivel de confianca

| Cliente | Nos | Temas Principais |
|---------|-----|------------------|
| Yuki | 99 | Fotografia, culpa, envelope do incendio |
| Tanaka | 99 | Bombeiro, investigacao, laudo fraudulento |
| Ryo | 95 | Fuga, culpa de sobrevivente, Mika |
| Midori | 102 | Florista, faiscas no quadro eletrico |
| Sachiko | 111 | Filha de Takeshi, briga, caderno do pai |
| Hiroto | 86 | Busca de 10 anos pelo salvador |

#### Exemplo — Yuki, Momento Inicial

```
[Yuki senta no canto do balcao, evitando contato visual]

┌─ O que voce diz? ──────────────────────────────────────────┐
│                                                             │
│  1. "Boa noite. O cardapio esta ali, se quiser olhar."     │
│     [Neutro - da espaco, mas sem conexao]                   │
│                                                             │
│  2. "Camera bonita. Pentax K1000?"                          │
│     [Observador - mostra atencao aos detalhes]              │
│                                                             │
│  3. "Parece cansada. Quer comeco com um cha quente?"       │
│     [Acolhedor - oferece cuidado]                           │
│                                                             │
│  4. [Apenas continue trabalhando em silencio]               │
│     [Silencioso - respeita o espaco dela]                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Cada opcao leva a uma ramificacao diferente:**

- Opcao 1: Yuki pede algo simples, conversa nao avanca muito
- Opcao 2: Yuki se surpreende — "Voce entende de cameras?" — abre porta para conversa
- Opcao 3: Yuki aceita o cha, relaxa um pouco, mas ainda distante
- Opcao 4: Apos um tempo, Yuki quebra o silencio — "Esse lugar... e tranquilo"

#### Sistema de Confianca Granular

```
NIVEL 0-20:  FECHADA    - Respostas curtas, evasivas
NIVEL 21-40: CAUTELOSA  - Comeca a observar, algumas perguntas
NIVEL 41-60: CURIOSA    - Faz perguntas, mostra interesse
NIVEL 61-80: ABERTA     - Compartilha historias, ri
NIVEL 81-100: VULNERAVEL - Revela segredos, emocao genuina
```

**Cada fala de Master tem um impacto:**
- Falas certas no momento certo: +10 a +20 confianca
- Falas neutras: +0 a +5
- Falas erradas: -5 a -15 (pode fechar o cliente)

**O jogador pode FALHAR uma noite** se:
- Confianca cair abaixo de 20
- Escolher opcoes que ofendem ou afastam
- Nao prestar atencao nas pistas

---

### 4. Pistas e Atencao aos Detalhes

**Conceito:** O jogador precisa PRESTAR ATENCAO ao que os clientes dizem
para fazer as escolhas certas.

**Exemplo — Pista de Yuki:**

```
Yuki: "Nao fotografo mais pessoas. So paisagens agora.
       Edificios. Coisas que nao... que nao mudam enquanto
       voce olha pra elas."

[Ela faz uma pausa. Seus dedos tracam o contorno da camera.]
```

**Opcoes de resposta:**

```
1. "Paisagens sao bonitas mesmo."
   [Resposta superficial - nao captou a dor]

2. "Pessoas mudam rapido demais?"
   [Captou algo, mas nao o cerne]

3. "Algo aconteceu enquanto voce fotografava alguem?"
   [PISTA CAPTADA - pergunta direta sobre o trauma]

4. "Esse restaurante tambem nao muda. Esta aqui ha anos."
   [Conexao indireta - cria ponte emocional]
```

A opcao 3 e a que mais avanca a confianca, mas tambem e arriscada —
pode fazer Yuki se fechar se o timing estiver errado.

---

### 5. Ambientacao Viva

**O restaurante como personagem:**

```
ABERTURA DE CADA NOITE:

O relogio acima do balcao marca 1:47 da manha.

La fora, Shinjuku pulsa em neon e embriaguez. Aqui dentro,
apenas o chiado suave do oleo na chapa e o tinir ocasional
de uma colher contra ceramica.

O ar cheira a dashi — aquele caldo de bonito seco que voce
prepara toda noite, mesmo quando ninguem aparece. E um
ritual. Uma oracao para ninguem em particular.

A cortina de noren balanca.
Alguem esta la fora, hesitando.
```

**Elementos de ambientacao:**
- Hora da noite (sempre de madrugada)
- Sons do restaurante e da rua
- Cheiros da cozinha
- Detalhes visuais (luz, sombras, objetos)
- Contraste interior/exterior

---

### 6. Monologos Internos de Master

**O jogador ve os pensamentos de Master**, criando conexao emocional:

```
[Yuki menciona um incendio de passagem]

Voce congela por um instante. A faca para no meio do corte.

    [Incendio. A palavra ecoa em algum lugar
     que voce tentou trancar ha dez anos.]

Yuki nao parece notar. Esta perdida em seus proprios fantasmas.

Voce volta a cortar. O ritmo da faca esconde o tremor nas maos.
```

**Quando usar:**
- Quando clientes tocam em temas do passado de Master
- Em momentos de tensao dramatica
- Na transicao entre noites
- Durante o Dia 7 (reflexao completa)

---

## Estrutura de Arquivos Refatorada

```
midnight-kitchen/
├── main.py                 # Ponto de entrada
├── config.py               # Configuracoes (cores, tempos, etc)
│
├── core/                   # Nucleo do jogo
│   ├── __init__.py
│   ├── game.py             # Loop principal e estado
│   ├── scene.py            # Gerenciador de cenas
│   └── renderer.py         # Renderizacao da interface
│
├── models/                 # Entidades
│   ├── __init__.py
│   ├── cliente.py          # Classe Cliente (expandida)
│   ├── prato.py            # Classe Prato
│   └── memoria.py          # Fragmentos de memoria
│
├── sistemas/               # Logica de jogo
│   ├── __init__.py
│   ├── dialogo.py          # Sistema de dialogo (refatorado)
│   ├── cozinha.py          # Sistema de cozinha
│   └── reflexao.py         # Dia 7
│
├── narrativa/              # Conteudo narrativo
│   ├── __init__.py
│   ├── ambientacao.py      # Descricoes de ambiente
│   ├── monologos.py        # Pensamentos de Master
│   └── transicoes.py       # Textos de transicao
│
├── dados/                  # Dados em JSON
│   ├── clientes/           # Um arquivo por cliente
│   │   ├── yuki.json
│   │   ├── tanaka.json
│   │   ├── ryo.json
│   │   ├── midori.json
│   │   ├── sachiko.json
│   │   └── hiroto.json
│   ├── dialogos/           # Arvores de dialogo
│   │   ├── yuki_dialogos.json
│   │   └── ...
│   └── pratos.json         # Todos os pratos
│
├── ui/                     # Interface
│   ├── __init__.py
│   ├── styles.py           # Estilos e cores
│   ├── components.py       # Componentes reutilizaveis
│   ├── ascii_art.py        # Arte ASCII
│   └── effects.py          # Efeitos visuais
│
└── docs/                   # Documentacao
    ├── VISAO_v2.md         # Este documento
    ├── NARRATIVA.md        # Guia de escrita
    └── PERSONAGENS.md      # Perfis detalhados
```

---

## Dependencias

```
# requirements.txt
rich>=13.0.0      # Interface rica no terminal
```

A biblioteca `rich` oferece:
- Paineis e boxes estilizados
- Cores e estilos de texto
- Tabelas formatadas
- Markdown no terminal
- Barra de progresso
- Efeito de digitacao (Live display)

---

## Fases da Refatoracao

### Fase 1: Infraestrutura UI ✓
- [x] Instalar e configurar `rich`
- [x] Criar sistema de renderizacao
- [x] Implementar componentes visuais
- [x] Criar arte ASCII elaborada

### Fase 2: Narrativa Base ✓
- [x] Reescrever descricoes de ambientacao
- [x] Criar monologos internos de Master
- [x] Expandir descricoes de personagens
- [x] Escrever transicoes entre cenas

### Fase 3: Sistema de Dialogo ✓
- [x] Estruturar dialogos por personagem em JSON
- [x] Implementar sistema de confianca granular
- [x] Criar ramificacoes de dialogo (592 nos total)
- [x] Adicionar pistas e consequencias

### Fase 4: Integracao e Polish ✓
- [x] Conectar todos os sistemas
- [x] Balancear dificuldade
- [x] Testar fluxo completo
- [x] Revisar toda a escrita

---

## Metricas de Qualidade

O jogo estara "pronto" quando:

1. **Imersao:** Jogador esquece que esta no terminal
2. **Escolhas:** Cada opcao de dialogo parece significativa
3. **Emocao:** Dia 7 provoca reacao emocional genuina
4. **Rejogabilidade:** Jogador quer tentar caminhos diferentes
5. **Polimento:** Zero bugs, zero textos placeholder

---

*Documento criado em 14/01/2026*
*Atualizado em 15/01/2026 — Dialogos expandidos para 592 nos*
*Versao 2.0 — Implementacao Completa*

# Design Document: Midnight Kitchen

## Conexao com a Serie

> **Este jogo se passa 10 anos antes** dos eventos da serie de TV
> *Midnight Diner* (Shinya Shokudo / 深夜食堂).
>
> Na serie, vemos um Master maduro, sabio e seguro de si.
> A **cicatriz em seu rosto** nunca e explicada.
>
> Este jogo conta a **historia de origem** dessa cicatriz
> e de como Master se tornou o homem que conhecemos.

---

## A Historia

### O Incendio (10 anos atras)

- **Chef Takeshi** era dono de um pequeno restaurante tradicional
- **Master** era seu jovem aprendiz, dedicado e talentoso
- Uma noite, um incendio destruiu o restaurante
- **Takeshi morreu** nas chamas
- **Master foi ferido** — a cicatriz no rosto e dessa noite
- Laudo oficial: **Acidente eletrico** (fiacao antiga)
- Porem, ha elementos de duvida no laudo
- Master nunca foi acusado, mas **se culpa** ha 10 anos

### O Presente

- Master abriu o **Midnight Kitchen**, um restaurante noturno
- Ele cozinha em silencio, carregando a culpa pela morte do mentor
- Seis clientes desconhecidos aparecem em seis noites consecutivas
- Cada um, sem saber, traz uma peca do quebra-cabeca
- No setimo dia, Master finalmente descobre a verdade e se liberta

### O Quebra-Cabeca

As pecas que provam a inocencia de Master:

| Noite | Cliente | Peca | Certeza |
|-------|---------|------|---------|
| 1 | Yuki | Fotos mostram fogo no quadro eletrico | Alta |
| 2 | Tanaka | "Nao parecia vir da cozinha" | Baixa |
| 3 | Ryo | "Acho que ele estava no deposito" | Baixa |
| 4 | Midori | Viu faiscas no quadro dias antes | Media |
| 5 | Sachiko | Caderno: Takeshi sabia do problema | Alta |
| 6 | Hiroto | Master salvou uma crianca | Alta |

**Nenhuma peca sozinha prova a inocencia. Juntas, formam o quadro.**

---

## Mecanica Narrativa

### Regras Fundamentais

1. **Nao-reconhecimento inicial**
   - Os clientes e Master NAO se reconhecem no inicio
   - 10 anos mudam muito as pessoas
   - A conexao so emerge apos o "desbloqueio"

2. **Prato como gatilho de memoria**
   - O prato favorito funciona como "chave" emocional
   - Ao receber o prato certo, memorias sao desbloqueadas
   - Cada cliente tem um prato especifico que ativa sua revelacao

3. **Sutileza das evidencias**
   - As pecas do quebra-cabeca sao sutis, nao explicitas
   - Clientes nao dizem "voce e inocente"
   - Master monta tudo sozinho no Dia 7

4. **Envelope de Yuki**
   - Yuki entrega fotos que ela mesma nunca analisou
   - Master so abre o envelope no Dia 7
   - A evidencia visual e a peca final

---

## Os 6 Clientes

### Noite 1: Yuki Tanabe

| Campo | Valor |
|-------|-------|
| Idade | 28 |
| Profissao | Fotografa freelancer |
| Prato | Tamago Gohan |
| Conexao | Fotografou o inicio do incendio |

**Arco:** Carrega vergonha por ter ficado fotografando em vez de ajudar.
Entrega envelope com fotos como presente de gratidao.

### Noite 2: Tanaka Kenji

| Campo | Valor |
|-------|-------|
| Idade | 58 |
| Profissao | Ex-bombeiro aposentado |
| Prato | Katsudon |
| Conexao | Tentou salvar Takeshi |

**Arco:** Carrega culpa por nao ter salvado Takeshi. Aposentou-se apos o trauma.
Tem apenas uma impressao vaga sobre a origem do fogo.

### Noite 3: Ryo Ishida

| Campo | Valor |
|-------|-------|
| Idade | 35 |
| Profissao | Motorista de taxi |
| Prato | Ochazuke |
| Conexao | Ex-garcom do restaurante |

**Arco:** Correu durante o incendio enquanto outros ficaram. Mudou de vida.
Memorias fragmentadas pelo trauma — nao lembra detalhes com clareza.

### Noite 4: Midori Sato

| Campo | Valor |
|-------|-------|
| Idade | 67 |
| Profissao | Aposentada (ex-florista) |
| Prato | Missoshiru |
| Conexao | Vizinha de Takeshi |

**Arco:** Viu faiscas no quadro eletrico dias antes e avisou Takeshi.
So lembra disso apos receber o prato — memoria enterrada.

### Noite 5: Sachiko Yamamoto

| Campo | Valor |
|-------|-------|
| Idade | 32 |
| Profissao | Contadora |
| Prato | Nikujaga |
| Conexao | Filha de Takeshi |

**Arco:** Brigou com o pai antes da morte. Nunca pediu desculpas.
Tem o caderno do pai que menciona o problema eletrico e "o menino" (Master).

### Noite 6: Hiroto Kimura

| Campo | Valor |
|-------|-------|
| Idade | 18 |
| Profissao | Estudante universitario |
| Prato | Omurice |
| Conexao | Crianca salva por Master |

**Arco:** Passou 10 anos procurando o homem que o salvou.
O encontro e o climax emocional — Master percebe que salvou uma vida.

---

## Dia 7: A Reflexao

O restaurante esta vazio. Master esta sozinho.

### Sequencia

1. Master relembra as conversas da semana
2. As pecas comecam a se conectar em sua mente
3. Ele abre o envelope de Yuki
4. As fotos mostram: fogo comecou no quadro eletrico
5. Monologo interno — catarse
6. Master finalmente se perdoa

### A Catarse

> "Dez anos. Dez anos carregando uma culpa que nao era minha.
> Takeshi-san sabia do problema. Ele estava tentando resolver.
> Ele me protegia enquanto eu achava que tinha matado ele.
> O menino... Hiroto... eu salvei ele. Eu fiz algo certo naquela noite.
> Takeshi-san... eu posso finalmente deixar voce ir?"

---

## Visao Geral da Arquitetura

```
┌─────────────────────────────────────────────────────────────────┐
│                         main.py                                 │
│                    (Loop Principal)                             │
├─────────────────────────────────────────────────────────────────┤
│                           │                                     │
│         ┌─────────────────┼─────────────────┐                   │
│         ▼                 ▼                 ▼                   │
│   ┌──────────┐     ┌──────────┐     ┌──────────────┐           │
│   │ dialogo  │     │ cozinha  │     │  reflexao    │           │
│   │ .py      │     │ .py      │     │  .py         │           │
│   └────┬─────┘     └────┬─────┘     └──────┬───────┘           │
│        │                │                  │                    │
│        └────────────────┼──────────────────┘                    │
│                         ▼                                       │
│              ┌─────────────────────┐                            │
│              │    restaurante.py   │                            │
│              │   (Estado do Jogo)  │                            │
│              └──────────┬──────────┘                            │
│                         │                                       │
│         ┌───────────────┼───────────────┐                       │
│         ▼               ▼               ▼                       │
│   ┌──────────┐   ┌──────────┐   ┌──────────┐                   │
│   │ cliente  │   │  prato   │   │ memoria  │                   │
│   │ .py      │   │  .py     │   │ .py      │                   │
│   └──────────┘   └──────────┘   └──────────┘                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Estrutura de Arquivos

```
midnight-kitchen/
├── main.py                    # Ponto de entrada
├── models/
│   ├── __init__.py
│   ├── cliente.py             # Classe Cliente
│   ├── prato.py               # Classe Prato
│   ├── restaurante.py         # Estado do jogo
│   └── memoria.py             # Fragmentos de memoria
├── sistemas/
│   ├── __init__.py
│   ├── dialogo.py             # Sistema de conversas
│   ├── cozinha.py             # Sistema de preparo
│   └── reflexao.py            # Dia 7 e catarse
├── dados/
│   ├── clientes.json          # Dados dos 6 clientes
│   ├── pratos.json            # Receitas e significados
│   └── dialogos.json          # Arvores de dialogo
├── assets/
│   └── ascii/                 # Arte ASCII
│       ├── titulo.txt         # Tela inicial
│       └── lanterna.txt       # Decoracoes
└── docs/
    ├── DESIGN.md              # Este documento
    ├── PERSONAGENS_PROPOSTA.md # Detalhes dos personagens
    └── APRENDIZAGEM.md        # Plano de tutoria
```

---

## Modelos (models/)

### Cliente (`models/cliente.py`)

```python
class Cliente:
    """Representa um cliente que visita o restaurante."""

    # Atributos
    nome: str                    # Nome completo
    idade: int                   # Idade em anos
    profissao: str               # Profissao atual
    descricao: str               # Descricao visual
    humor: str                   # Estado emocional
    prato_favorito: str          # Prato que desbloqueia memoria
    segredo: str                 # O que esconde
    confianca: int               # Nivel de confianca (0-100)
    memoria_desbloqueada: bool   # Se ja revelou seu segredo
    conexao_incendio: str        # Como se conecta ao incendio

    # Metodos
    def apresentar() -> str
    def reagir(acao: str) -> str
    def aumentar_confianca(qtd: int) -> None
    def pode_revelar_segredo() -> bool
    def revelar_segredo() -> str
```

### Prato (`models/prato.py`)

```python
class Prato:
    """Representa um prato que pode ser preparado."""

    # Atributos
    nome: str                    # Nome do prato
    ingredientes: list[str]      # Ingredientes necessarios
    tempo_preparo: int           # Minutos
    significado: str             # Significado emocional
    gatilho: str                 # Tema emocional que ativa
    descricao_preparo: str       # Narrativa do preparo

    # Metodos
    def preparar() -> str
    def servir(cliente: Cliente) -> str
    def listar_ingredientes() -> str
```

### Restaurante (`models/restaurante.py`)

```python
class Restaurante:
    """Estado central do jogo."""

    # Atributos
    dia_atual: int               # 1-7
    cliente_atual: Cliente       # Cliente da noite (None no dia 7)
    memorias: list[str]          # Memorias desbloqueadas
    envelope_yuki: bool          # Se recebeu o envelope
    historico: list[dict]        # Registro de cada noite

    # Metodos
    def iniciar_noite(dia: int) -> str
    def registrar_memoria(cliente: str, conteudo: str) -> None
    def avancar_dia() -> None
    def e_dia_reflexao() -> bool
```

### Memoria (`models/memoria.py`)

```python
class Memoria:
    """Fragmento de memoria desbloqueado."""

    # Atributos
    cliente: str                 # Nome do cliente
    conteudo: str                # O que foi revelado
    peca_quebracabeca: str       # Que evidencia traz
    certeza: str                 # "alta", "media", "baixa"
    dia: int                     # Em qual dia foi desbloqueada

    # Metodos
    def exibir() -> str
    def resumir() -> str
```

---

## Sistemas (sistemas/)

### Dialogo (`sistemas/dialogo.py`)

```python
class SistemaDialogo:
    """Gerencia conversas com clientes."""

    def iniciar_conversa(cliente: Cliente) -> str
    def mostrar_opcoes(cliente: Cliente, fase: str) -> list[dict]
    def processar_escolha(cliente: Cliente, escolha: int) -> str
    def verificar_desbloqueio(cliente: Cliente) -> bool
```

**Fases do dialogo:**
1. `chegada` — Cliente entra, apresentacao inicial
2. `conversa` — Dialogo normal, construindo confianca
3. `prato` — Cliente pede/recebe prato favorito
4. `desbloqueio` — Memoria emerge apos o prato
5. `despedida` — Cliente vai embora

### Cozinha (`sistemas/cozinha.py`)

```python
class SistemaCozinha:
    """Gerencia preparacao de pratos."""

    def listar_pratos_disponiveis() -> list[Prato]
    def preparar_prato(prato: Prato) -> str
    def servir_prato(prato: Prato, cliente: Cliente) -> str
    def verificar_gatilho(prato: Prato, cliente: Cliente) -> bool
```

### Reflexao (`sistemas/reflexao.py`)

```python
class SistemaReflexao:
    """Gerencia o Dia 7 e a catarse de Master."""

    def iniciar_reflexao(restaurante: Restaurante) -> str
    def revisar_memorias(memorias: list[Memoria]) -> str
    def abrir_envelope() -> str
    def monologo_catarse() -> str
    def encerramento() -> str
```

---

## Fluxo de Jogo

```
┌──────────────────────────────────────────────────────────────┐
│                    TELA INICIAL                              │
│              [ASCII Art + Introducao]                        │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                    LOOP PRINCIPAL                            │
│                      (7 dias)                                │
└──────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┴───────────────┐
              │       dia <= 6?               │
              └───────────────┬───────────────┘
                     SIM      │      NAO
                      │       │       │
                      ▼       │       ▼
            ┌─────────────┐   │   ┌─────────────┐
            │  Carregar   │   │   │   Dia 7:    │
            │  Cliente    │   │   │  Reflexao   │
            └──────┬──────┘   │   └──────┬──────┘
                   │          │          │
                   ▼          │          ▼
         ┌─────────────────┐  │    ┌───────────────┐
         │ LOOP DA NOITE:  │  │    │ - Revisar     │
         │ 1. Chegada      │  │    │   memorias    │
         │ 2. Conversa     │  │    │ - Abrir       │
         │ 3. Prato        │  │    │   envelope    │
         │ 4. Desbloqueio  │  │    │ - Catarse     │
         │ 5. Despedida    │  │    │ - Fim         │
         └────────┬────────┘  │    └───────────────┘
                  │           │
                  ▼           │
        ┌──────────────────┐  │
        │ Registrar        │  │
        │ Memoria          │  │
        └────────┬─────────┘  │
                 │            │
                 ▼            │
        ┌──────────────────┐  │
        │ Avancar Dia      │──┘
        └──────────────────┘
```

---

## Dados (dados/)

### clientes.json

```json
{
  "yuki": {
    "nome": "Yuki Tanabe",
    "idade": 28,
    "profissao": "Fotografa freelancer",
    "descricao": "Uma jovem com camera antiga pendurada no pescoco",
    "humor_inicial": "pensativa",
    "prato_favorito": "Tamago Gohan",
    "segredo": "Fotografei a morte de um homem. E fiquei parada.",
    "conexao_incendio": "Fotografou o inicio do incendio",
    "peca_quebracabeca": "Fotos mostram fogo no quadro eletrico",
    "certeza": "alta",
    "entrega_envelope": true
  }
}
```

### pratos.json

```json
{
  "tamago_gohan": {
    "nome": "Tamago Gohan",
    "ingredientes": ["ovo", "arroz", "shoyu"],
    "tempo_preparo": 5,
    "significado": "Simplicidade reconfortante - comida de infancia",
    "gatilho": "nostalgia, conforto, recomecos",
    "descricao_preparo": "O ovo cru e quebrado sobre o arroz quente..."
  },
  "katsudon": {
    "nome": "Katsudon",
    "ingredientes": ["porco", "ovo", "arroz", "cebola", "dashi"],
    "tempo_preparo": 20,
    "significado": "Comida de vitoria - celebracao ou busca de redencao",
    "gatilho": "derrota, busca de vitoria, redencao",
    "descricao_preparo": "O tonkatsu crocante encontra o ovo macio..."
  }
}
```

---

## Tela Inicial

```
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║     ░░░░░░░                                               ║
    ║    ░░░░░░░░░      M I D N I G H T   K I T C H E N        ║
    ║   ░░░░░░░░░░░                                             ║
    ║    ░░░░░░░░░            深 夜 キ ッ チ ン                 ║
    ║     ░░░░░░░                                               ║
    ║       ║║║                                                 ║
    ║       ║║║         Uma historia de culpa,                  ║
    ║    ═══╩╩╩═══          memoria e perdao.                   ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝

    Este jogo se passa 10 anos antes dos eventos da serie
    "Midnight Diner" (Shinya Shokudo).

    Aqui conhecemos um Master mais jovem, carregando uma
    ferida que ainda nao cicatrizou — nem no rosto, nem na alma.

    [Pressione ENTER para comecar]
```

---

## Decisoes de Design

### Por que JSON para dados?

- Separacao clara entre codigo e conteudo
- Facilita edicao de dialogos sem mexer no codigo
- Demonstra habilidade com leitura de arquivos
- Permite expansao futura

### Por que classes separadas em models/?

- Principio de responsabilidade unica
- Facilita testes unitarios
- Codigo mais legivel e manutenivel
- Boa pratica de organizacao

### Por que o prato como gatilho?

- Conecta mecanica (cozinhar) com narrativa (memorias)
- Cria momentos significativos de gameplay
- Reflete o tema da serie original
- Permite escolha do jogador com consequencias

### Por que 7 dias em vez de 5?

- 6 clientes dao mais pecas para o quebra-cabeca
- Dia 7 dedicado a reflexao cria climax adequado
- Estrutura de "semana" e intuitiva
- Permite desenvolvimento mais profundo de cada cliente

---

## Proximos Passos (Desenvolvimento)

### Fase 1: Fundamentos (Atual)
- [x] Classe Cliente
- [ ] Classe Prato
- [ ] Classe Restaurante
- [ ] Classe Memoria

### Fase 2: Sistemas
- [ ] Sistema de Dialogo
- [ ] Sistema de Cozinha
- [ ] Sistema de Reflexao

### Fase 3: Integracao
- [ ] main.py com loop principal
- [ ] Dados JSON dos clientes
- [ ] Dados JSON dos pratos
- [ ] Arte ASCII

### Fase 4: Polish
- [ ] Testes completos
- [ ] Balanceamento de dialogos
- [ ] Revisao de texto

---

*Documento atualizado em 12/01/2026*
*Versao 2.0 — Nova estrutura narrativa aprovada*

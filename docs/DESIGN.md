# Design Document: Midnight Kitchen

## Visão Geral da Arquitetura

```
┌─────────────────────────────────────────────────────────────────┐
│                         main.py                                 │
│                    (Loop Principal)                             │
├─────────────────────────────────────────────────────────────────┤
│                           │                                     │
│         ┌─────────────────┼─────────────────┐                   │
│         ▼                 ▼                 ▼                   │
│   ┌──────────┐     ┌──────────┐     ┌──────────────┐           │
│   │ dialogo  │     │ cozinha  │     │  revelacao   │           │
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

## Modelos (models/)

### Cliente (`models/cliente.py`)

```python
class Cliente:
    """Representa um cliente do restaurante."""

    # Atributos
    nome: str                    # Nome do cliente
    idade: int                   # Idade
    profissao: str               # Profissão atual
    descricao: str               # Descrição visual/primeira impressão
    humor: str                   # Estado emocional atual
    prato_favorito: str          # Prato que desbloqueia memória
    historia: dict               # Diálogos e revelações
    segredo: str                 # O que esconde (conexão com Master)
    fragmento_id: str            # ID do fragmento que desbloqueia
    confianca: int               # Nível de confiança (0-100)

    # Métodos
    def apresentar() -> str      # Retorna descrição inicial
    def reagir(acao: str) -> str # Reage a uma ação do jogador
    def revelar_segredo() -> str # Quando confiança >= 80
```

### Prato (`models/prato.py`)

```python
class Prato:
    """Representa um prato que pode ser preparado."""

    # Atributos
    nome: str                    # Nome do prato
    ingredientes: list[str]      # Lista de ingredientes necessários
    tempo_preparo: int           # Minutos (afeta passagem do tempo)
    significado: str             # Significado emocional/cultural
    gatilho: str                 # Tema emocional que ativa
    descricao_preparo: str       # Texto narrativo do preparo

    # Métodos
    def preparar() -> str        # Retorna narrativa do preparo
    def servir(cliente) -> str   # Retorna reação do cliente
```

### Restaurante (`models/restaurante.py`)

```python
class Restaurante:
    """Estado central do jogo."""

    # Atributos
    noite_atual: int             # 1-5
    hora: str                    # "00:30", "02:15", etc.
    ingredientes: dict[str, int] # Inventário: {"ovo": 5, "arroz": 3}
    cliente_atual: Cliente       # Cliente da noite
    memorias_desbloqueadas: list # Fragmentos já revelados
    historico_pratos: list       # Pratos servidos nesta noite

    # Métodos
    def avancar_tempo(minutos: int)    # Avança o relógio
    def verificar_ingrediente(nome: str) -> bool
    def consumir_ingrediente(nome: str, qtd: int)
    def registrar_memoria(fragmento_id: str)
    def noite_terminou() -> bool       # True se hora >= "07:00"
```

### Memoria (`models/memoria.py`)

```python
class Memoria:
    """Fragmento do passado do Master."""

    # Atributos
    id: str                      # "fragmento_1", "fragmento_2", etc.
    titulo: str                  # Título curto
    conteudo: str                # Texto da memória
    gatilho: str                 # O que desbloqueia (prato + cliente)
    ordem: int                   # Ordem na narrativa (1-4)

    # Métodos
    def exibir() -> str          # Formata para exibição
```

---

## Sistemas (sistemas/)

### Diálogo (`sistemas/dialogo.py`)

```python
class SistemaDialogo:
    """Gerencia conversas com clientes."""

    def iniciar_conversa(cliente: Cliente) -> str
    def mostrar_opcoes(cliente: Cliente, contexto: str) -> list[dict]
    def processar_escolha(cliente: Cliente, escolha: int) -> str
    def verificar_revelacao(cliente: Cliente) -> bool
```

**Estrutura de diálogo:**
```python
opcao = {
    "texto": "Noite difícil no trabalho?",
    "efeito_confianca": +10,
    "resposta": "Tanaka suspira...",
    "desbloqueia": None  # ou "topico_familia"
}
```

### Cozinha (`sistemas/cozinha.py`)

```python
class SistemaCozinha:
    """Gerencia preparação de pratos."""

    def mostrar_ingredientes(restaurante: Restaurante) -> str
    def validar_receita(ingredientes: list[str]) -> Prato | None
    def preparar_prato(prato: Prato, restaurante: Restaurante) -> str
    def calcular_efeito(prato: Prato, cliente: Cliente) -> dict
```

**Lógica de receitas:**
```python
RECEITAS = {
    frozenset(["frango", "ovo", "arroz", "dashi", "cebola"]): "Oyakodon",
    frozenset(["tofu", "miso", "dashi", "cebola"]): "Missoshiru",
    # ...
}
```

### Revelação (`sistemas/revelacao.py`)

```python
class SistemaRevelacao:
    """Gerencia a Noite 5 e conclusões."""

    def calcular_final(memorias: list) -> str  # Qual final baseado em descobertas
    def reunir_clientes() -> str               # Narrativa da reunião
    def revelar_verdade(memorias: list) -> str # Revelação final
```

---

## Dados (dados/)

### clientes.json

```json
{
  "yuki": {
    "nome": "Yuki Tanabe",
    "idade": 28,
    "profissao": "Fotógrafa freelancer",
    "descricao": "Uma mulher jovem com câmera antiga pendurada no pescoço...",
    "humor_inicial": "pensativa",
    "prato_favorito": "Tamago Gohan",
    "fragmento_id": "fragmento_1",
    "dialogos": {
      "abertura": ["Boa noite...", "Ainda aberto?"],
      "sobre_trabalho": {...},
      "sobre_passado": {...}
    }
  }
}
```

### pratos.json

```json
{
  "oyakodon": {
    "nome": "Oyakodon",
    "ingredientes": ["frango", "ovo", "arroz", "dashi", "cebola"],
    "tempo_preparo": 15,
    "significado": "Prato de 'pais e filhos' - frango e ovo unidos",
    "gatilho": "família, perda, conexão entre gerações",
    "descricao_preparo": "O frango dourado na panela, o ovo vertido..."
  }
}
```

### memorias.json

```json
{
  "fragmento_1": {
    "titulo": "A Foto na Parede",
    "conteudo": "Uma fotografia antiga... um restaurante cheio de vida...",
    "ordem": 1
  }
}
```

---

## Fluxo de Jogo

```
┌──────────────────────────────────────────────────────────────┐
│                      LOOP PRINCIPAL                          │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  Iniciar Noite  │
                    │  (1, 2, 3, 4, 5)│
                    └────────┬────────┘
                              │
              ┌───────────────┴───────────────┐
              │  noite <= 4?                  │
              └───────────────┬───────────────┘
                     SIM      │      NÃO
                      │       │       │
                      ▼       │       ▼
            ┌─────────────┐   │   ┌─────────────┐
            │  Carregar   │   │   │  Noite 5:   │
            │  Cliente    │   │   │  Revelação  │
            └──────┬──────┘   │   └──────┬──────┘
                   │          │          │
                   ▼          │          ▼
         ┌─────────────────┐  │    ┌───────────┐
         │ LOOP DA NOITE:  │  │    │  Reunir   │
         │ - Conversar     │  │    │  Clientes │
         │ - Cozinhar      │  │    │  + Final  │
         │ - Servir        │  │    └───────────┘
         │ até 07:00       │  │
         └────────┬────────┘  │
                  │           │
                  ▼           │
        ┌──────────────────┐  │
        │ Fragmento        │  │
        │ Desbloqueado?    │  │
        └────────┬─────────┘  │
                 │            │
                 ▼            │
        ┌──────────────────┐  │
        │ Avançar Noite    │──┘
        └──────────────────┘
```

---

## Decisões de Design

### Por que JSON para dados?

- Separação clara entre código e conteúdo
- Facilita edição de diálogos sem mexer no código
- Demonstra habilidade com leitura de arquivos
- Permite expansão futura (mais clientes, pratos)

### Por que classes separadas em models/?

- Princípio de responsabilidade única
- Facilita testes unitários
- Código mais legível e manutenível
- Boa prática de organização em projetos reais

### Por que sistema de receitas com frozenset?

- Ordem dos ingredientes não importa
- Lookup O(1) em dicionário
- Elegante e pythônico
- Demonstra conhecimento de estruturas de dados

---

## Extensões Futuras (Pós-MVP)

- [ ] Sistema de save/load (persistência em JSON)
- [ ] Mais clientes e noites
- [ ] Finais alternativos baseados em escolhas
- [ ] Arte ASCII para pratos
- [ ] Música/sons no terminal (biblioteca curses)

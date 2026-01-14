# Arquitetura v3 — Midnight Kitchen

## Filosofia de Design

> O jogador nao sabe nada sobre o cliente no inicio.
> Atraves de escolhas sabias de dialogo, Master descobre quem e o cliente,
> o que o aflige, e qual prato pode ajuda-lo.
> O prato certo desbloqueia a memoria critica.

---

## Fluxo de Uma Noite

```
ENTRADA
   │
   ▼
┌─────────────────────────────────────────┐
│ Cliente entra no restaurante            │
│ Master ve apenas: descricao fisica      │
│ Nao sabe: nome, historia, prato         │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│         LOOP DE DIALOGO                 │
│                                         │
│  ┌───────────────────────────────────┐  │
│  │ Master escolhe uma acao:          │  │
│  │  [1] Ficar em silencio            │  │
│  │  [2] Oferecer cha                 │  │
│  │  [3] Perguntar sobre o dia        │  │
│  │  [4] Perguntar sobre trabalho     │  │
│  │  [5] Comentar sobre o tempo       │  │
│  │  ... (opcoes variam por contexto) │  │
│  └───────────────────────────────────┘  │
│                 │                       │
│                 ▼                       │
│  ┌───────────────────────────────────┐  │
│  │ Cliente reage:                    │  │
│  │  - Se abre (revela informacao)    │  │
│  │  - Se fecha (fica desconfortavel) │  │
│  │  - Neutro (conversa continua)     │  │
│  └───────────────────────────────────┘  │
│                 │                       │
│                 ▼                       │
│  ┌───────────────────────────────────┐  │
│  │ Novas opcoes desbloqueadas?       │  │
│  │ Informacoes reveladas?            │  │
│  │ Prato favorito descoberto?        │  │
│  └───────────────────────────────────┘  │
│                 │                       │
│       ┌─────────┴─────────┐             │
│       │                   │             │
│      NAO                 SIM            │
│       │                   │             │
│       ▼                   ▼             │
│  [Continua loop]    [Sai do loop]       │
└─────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│ PREPARACAO DO PRATO                     │
│                                         │
│ Se descobriu prato favorito:            │
│   → Master prepara o prato              │
│   → Narrativa do preparo                │
│                                         │
│ Se NAO descobriu:                       │
│   → Master prepara algo generico        │
│   → Cliente agradece, vai embora        │
│   → Memoria NAO e desbloqueada          │
│   → (Consequencia: quebra-cabeca        │
│      incompleto no dia 7)               │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│ SERVIR = GATILHO                        │
│                                         │
│ Se prato correto:                       │
│   → Cliente tem reacao emocional        │
│   → Memoria critica desbloqueada        │
│   → Revelacao da conexao com incendio   │
│                                         │
│ Casos especiais:                        │
│   → Yuki: SE sucesso, entrega envelope  │
│   → Hiroto reconhece Master             │
│   → Envelope SO EXISTE se Yuki = sucesso│
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│ DESPEDIDA                               │
│                                         │
│ Cliente vai embora                      │
│ Master reflete brevemente               │
│ Proximo dia                             │
└─────────────────────────────────────────┘
```

---

## Sistema de Dialogo

### Conceito: Arvore de Descoberta

Cada cliente tem uma "arvore" de informacoes que podem ser descobertas.
As escolhas do jogador determinam quais ramos sao explorados.

```
                    [CLIENTE ENTRA]
                          │
            ┌─────────────┴─────────────┐
            │                           │
      [Sobre trabalho]           [Sobre vida pessoal]
            │                           │
     ┌──────┴──────┐             ┌──────┴──────┐
     │             │             │             │
[Frustracao]  [Paixao]      [Familia]    [Solidao]
     │             │             │             │
     └─────────────┴─────────────┴─────────────┘
                          │
                   [CONEXAO COM PASSADO]
                          │
                   [PRATO FAVORITO]
                          │
                   [MEMORIA CRITICA]
```

### Estados de Abertura do Cliente

Em vez de "confianca 0-100", usamos estados qualitativos:

```python
class EstadoAbertura:
    FECHADO = "fechado"       # Respostas curtas, defensivo
    CAUTELOSO = "cauteloso"   # Responde, mas sem profundidade
    ABERTO = "aberto"         # Compartilha, faz perguntas
    VULNERAVEL = "vulneravel" # Pronto para revelar o mais profundo
```

### Estrutura de uma Opcao de Dialogo

```python
opcao_dialogo = {
    "id": "perguntar_trabalho",
    "texto_master": "Dia dificil no trabalho?",
    "condicao": None,  # ou "cliente.estado == 'aberto'"
    "efeitos": {
        "estado": +1,  # Melhora abertura (ou -1 se errado)
        "revela": "profissao",  # Informacao revelada
        "desbloqueia": ["perguntar_frustracao", "perguntar_rotina"]
    },
    "resposta_cliente": "Yuki suspira... 'Voce nao tem ideia.'"
}
```

### Exemplo: Yuki (Noite 1)

```
INICIO: Master ve "Uma jovem com camera antiga entra"

OPCOES INICIAIS:
  [1] "Boa noite. O que posso servir?"        → Neutro
  [2] "Camera interessante. Analogica?"       → Abre dialogo sobre trabalho
  [3] Ficar em silencio, preparando cha       → Cria ambiente acolhedor

SE ESCOLHE [2]:
  Yuki: "Sim... e uma Leica antiga. Pertencia ao meu avo."
  REVELA: Ela tem conexao emocional com fotografia
  DESBLOQUEIA: Perguntas sobre familia, sobre fotografia

NOVAS OPCOES:
  [1] "Seu avo era fotografo?"                → Aprofunda familia
  [2] "O que voce gosta de fotografar?"       → Aprofunda trabalho
  [3] Oferecer cha silenciosamente            → Cria conforto

... (dialogo continua) ...

MOMENTO CHAVE (apos varias trocas):
  Yuki: "Eu tenho fotos que nunca mostrei pra ninguem.
         Fotos de uma noite que eu queria esquecer.
         [pausa]
         Sabe o que me conforta quando penso nisso?
         Um prato simples. Tamago Gohan.
         Minha avo fazia quando eu estava triste."

  REVELA: Prato favorito = Tamago Gohan
  DESBLOQUEIA: Opcao de preparar o prato

MASTER PREPARA TAMAGO GOHAN

AO SERVIR:
  Yuki come em silencio. Lagrimas nos olhos.
  "Obrigada. Eu... preciso te dar uma coisa."
  Ela tira um envelope do bolso.
  "Sao fotos. De uma noite ha 10 anos.
   Eu nunca consegui olhar direito.
   Talvez voce encontre algo bonito nelas."

  REVELA: Memoria critica (envelope com fotos)
  ITEM: Envelope de Yuki (abre no dia 7)
```

---

## Classes Revisadas

### Cliente (v3)

```python
class Cliente:
    """Um cliente que visita o restaurante."""

    # Identidade (Master descobre progressivamente)
    nome: str                    # Revelado durante dialogo
    idade: int                   # Pode ser revelado ou nao
    profissao: str               # Revelado durante dialogo

    # Visual (Master ve imediatamente)
    descricao: str               # Primeira impressao visual
    genero_masculino: bool       # Para pronomes

    # Estado (muda durante a noite)
    estado: str                  # "fechado", "cauteloso", "aberto", "vulneravel"
    informacoes_reveladas: list  # O que Master ja sabe

    # Narrativa (carregado de JSON, oculto do jogador)
    dialogo_arvore: dict         # Arvore de dialogo completa
    prato_favorito: str          # Descoberto via dialogo
    memoria_critica: str         # Revelada ao servir prato
    conexao_incendio: str        # Para referencia interna
    peca_quebracabeca: str       # Que evidencia traz

    # Metodos
    def apresentar() -> str      # Descricao visual apenas
    def processar_acao(acao: str) -> dict  # Retorna resposta + efeitos
    def revelar_memoria() -> str  # Quando prato e servido
```

### Prato (v3)

```python
class Prato:
    """Um prato que pode ser preparado."""

    nome: str
    ingredientes: list[str]
    tempo_preparo: int
    descricao_preparo: str       # Narrativa do preparo
    significado: str             # Significado cultural/emocional

    # Metodos
    def preparar() -> str        # Narrativa do preparo
    def servir(cliente: Cliente) -> dict  # Retorna narrativa + desbloqueio
```

### Memoria (v3)

```python
class Memoria:
    """Uma peca do quebra-cabeca descoberta."""

    dia: int                     # Em qual dia foi coletada
    cliente_nome: str            # Quem revelou
    conteudo: str                # O que foi revelado
    peca_quebracabeca: str       # Resumo da evidencia
    certeza: str                 # "alta", "media", "baixa"
    item_especial: str           # Ex: "envelope" para Yuki
```

### Jogo (novo — substitui Restaurante)

```python
class Jogo:
    """Estado central do jogo."""

    dia_atual: int               # 1-7
    cliente_atual: Cliente       # None no dia 7
    memorias: list[Memoria]      # Pecas coletadas

    # Itens especiais
    envelope_yuki: dict          # {"recebido": bool, "aberto": bool}

    # Metodos
    def iniciar_dia() -> str
    def processar_escolha(escolha: str) -> dict
    def preparar_prato(nome_prato: str) -> str
    def servir_prato() -> dict
    def finalizar_dia() -> str
    def executar_dia_7() -> str  # Reflexao final
```

### SistemaDialogo (novo)

```python
class SistemaDialogo:
    """Gerencia o fluxo de conversa."""

    def carregar_arvore(cliente_id: str) -> dict
    def obter_opcoes_disponiveis(cliente: Cliente) -> list[dict]
    def processar_escolha(cliente: Cliente, opcao_id: str) -> dict
    def verificar_prato_descoberto(cliente: Cliente) -> bool
```

---

## Estrutura de Arquivos Revisada

```
midnight-kitchen/
├── main.py                    # Loop principal
├── models/
│   ├── __init__.py
│   ├── cliente.py             # Classe Cliente v3
│   ├── prato.py               # Classe Prato v3
│   ├── memoria.py             # Classe Memoria v3
│   └── jogo.py                # Classe Jogo (estado central)
├── sistemas/
│   ├── __init__.py
│   ├── dialogo.py             # Sistema de dialogo
│   ├── cozinha.py             # Preparacao de pratos
│   └── reflexao.py            # Dia 7
├── dados/
│   ├── clientes/              # Um arquivo por cliente
│   │   ├── yuki.json
│   │   ├── tanaka.json
│   │   ├── ryo.json
│   │   ├── midori.json
│   │   ├── sachiko.json
│   │   └── hiroto.json
│   ├── pratos.json            # Todos os pratos
│   └── reflexao.json          # Textos do dia 7
├── assets/
│   └── ascii/
└── docs/
```

---

## Dados: Exemplo de Cliente (yuki.json)

```json
{
  "id": "yuki",
  "nome": "Yuki Tanabe",
  "idade": 28,
  "genero_masculino": false,
  "profissao": "Fotografa freelancer",
  "descricao": "Uma jovem com uma camera antiga pendurada no pescoco",

  "prato_favorito": "Tamago Gohan",
  "conexao_incendio": "Fotografou o inicio do incendio",
  "peca_quebracabeca": "Fotos mostram fogo comecando no quadro eletrico",
  "certeza": "alta",
  "item_especial": "envelope",

  "estado_inicial": "cauteloso",

  "dialogo": {
    "entrada": {
      "narrativa": "A porta se abre. Uma jovem entra hesitante.",
      "opcoes": ["silencio", "boas_vindas", "comentar_camera"]
    },
    "opcoes": {
      "silencio": {
        "texto_master": "[Ficar em silencio, preparando cha]",
        "resposta": "Ela se senta no balcao, olhando ao redor.",
        "efeito_estado": 0,
        "revela": [],
        "desbloqueia": ["oferecer_cha"]
      },
      "comentar_camera": {
        "texto_master": "Camera interessante. Analogica?",
        "resposta": "Ela toca a camera instintivamente. 'Sim... uma Leica. Era do meu avo.'",
        "efeito_estado": 1,
        "revela": ["gosta_fotografia", "conexao_avo"],
        "desbloqueia": ["perguntar_avo", "perguntar_fotografia"]
      }
    },
    "revelacao_prato": {
      "condicao": "estado >= aberto AND fotografia_discutida",
      "narrativa": "Yuki olha para o balcao vazio. 'Sabe o que me conforta? Um prato simples. Tamago Gohan. Minha avo fazia.'",
      "revela": ["prato_favorito"]
    },
    "memoria_critica": {
      "narrativa": "Yuki come em silencio. Lagrimas escorrem. 'Obrigada. Eu... tenho algo pra voce.'",
      "entrega": "envelope",
      "conteudo": "Fotos de uma noite ha 10 anos. Nunca consegui olhar direito."
    }
  }
}
```

---

## Consequencias de Design

### Se o jogador NAO descobrir o prato favorito:

- Cliente come algo generico
- Agradece e vai embora
- Memoria critica NAO e desbloqueada
- No dia 7, quebra-cabeca esta incompleto
- Final pode ser diferente (mais ambiguo)

### Se o jogador descobrir todos os pratos:

- Todas as memorias sao coletadas
- Dia 7 tem todas as pecas
- Catarse completa de Master

### Isso cria REJOGABILIDADE:

- Primeira vez: talvez perca algumas memorias
- Segunda vez: tenta descobrir todas
- Cada playthrough pode ter final diferente

---

## Decisoes de Design (Aprovadas)

### Falha

- **Sim, o jogador pode falhar** em descobrir o prato favorito
- Se falhar, a memoria daquela noite e perdida
- Maximo de **1 falha** permitida para final bom
- **2+ falhas** = final incompleto

### Duracao

- **5-8 trocas de dialogo** por noite
- Jogo completo em aproximadamente **30 minutos**
- Noites curtas e focadas

### Sistema de Finais

```
┌─────────────────────────────────────────────────────────────────┐
│                    CALCULO DO FINAL                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Memorias coletadas: X de 6                                     │
│  Falhas: 6 - X                                                  │
│                                                                 │
│  SE falhas <= 1 (5-6 memorias):                                 │
│     → FINAL COMPLETO                                            │
│     → Master monta quebra-cabeca                                │
│     → Abre envelope, ve fotos                                   │
│     → Catarse: "Nao foi minha culpa"                            │
│     → Cicatriz nao doi mais                                     │
│                                                                 │
│  SE falhas >= 2 (0-4 memorias):                                 │
│     → FINAL INCOMPLETO                                          │
│     → Master sente que faltam pecas                             │
│     → "Algo importante me escapou..."                           │
│     → Envelope nao faz sentido completo                         │
│     → Convite a rejogar                                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Proximos Passos

### Fase 1: Classes Base
1. [ ] Reescrever `Cliente` (v3)
2. [ ] Reescrever `Prato` (v3)
3. [ ] Criar `Memoria` (v3)
4. [ ] Criar `Jogo` (novo)

### Fase 2: Sistema de Dialogo
5. [ ] Criar `SistemaDialogo`
6. [ ] Criar estrutura JSON para um cliente (Yuki)
7. [ ] Testar fluxo de uma noite

### Fase 3: Integracao
8. [ ] Criar todos os JSONs de clientes
9. [ ] Implementar Dia 7 (reflexao)
10. [ ] Implementar sistema de finais

### Fase 4: Polish
11. [ ] Arte ASCII
12. [ ] Testes completos
13. [ ] Balanceamento de dificuldade

---

*Arquitetura v3 — Aprovada*
*12/01/2026*

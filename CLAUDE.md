# CLAUDE.md — Midnight Kitchen v2.0

## Sobre o Projeto

**Midnight Kitchen** e um jogo narrativo de terminal em Python.
Se passa **10 anos antes** da serie *Midnight Diner*.
Conta a historia de origem da **cicatriz de Master**.

**Status atual:** Implementacao completa.

---

## Jogar

```bash
# Instalar dependencias
pip3 install -r requirements.txt

# Rodar o jogo
python3 main.py
```

---

## Estrutura do Projeto

```
midnight-kitchen/
├── main.py              # Ponto de entrada
├── config.py            # Configuracoes globais
├── contracts.py         # Tipos e interfaces
├── requirements.txt     # Dependencias (rich)
│
├── core/                # Nucleo do jogo
│   ├── game.py          # Estado global
│   ├── menu.py          # Menu inicial + save
│   ├── noite.py         # Orquestrador de noites
│   ├── scene.py         # Gerenciador de cenas
│   ├── tempo.py         # Sistema de tempo
│   └── save.py          # Sistema de save
│
├── sistemas/            # Logica de jogo
│   ├── dialogo.py       # Sistema de dialogo
│   ├── cozinha.py       # Sistema de cozinha
│   └── reflexao.py      # Dia 7 + finais
│
├── narrativa/           # Conteudo narrativo
│   ├── abertura.py      # Textos de abertura
│   └── onboarding.py    # Tutorial
│
├── dados/               # Dados em JSON
│   ├── clientes/        # 6 clientes
│   ├── dialogos/        # Arvores de dialogo
│   └── pratos.json      # Receitas
│
├── ui/                  # Interface
│   ├── styles.py        # Estilos e cores
│   ├── components.py    # Componentes UI
│   ├── ascii_art.py     # Arte ASCII (beco de Shinjuku)
│   ├── effects.py       # Efeitos visuais
│   └── renderer.py      # Renderizacao
│
├── tests/               # Testes automatizados
│   ├── README.md        # Documentacao dos testes
│   ├── test_play.py     # Teste exploratorio
│   ├── test_cliente.py  # Teste por cliente
│   └── test_finais.py   # Teste de finais
│
└── docs/                # Documentacao
    ├── DESIGN.md        # Design consolidado
    └── PROMPTS.md       # Prompts de analise
```

---

## Mecanicas do Jogo

### Fluxo Principal
- **6 noites:** Um cliente por noite
- **Dia 7:** Reflexao + revelacao do final
- **Save automatico:** Entre noites

### Controles
- **ENTER/ESPACO:** Pula texto durante digitacao (util ao rejogar)
- **Numeros:** Seleciona opcoes nos menus

### Sistema de Confianca
- 0-20: Fechado
- 21-40: Cauteloso
- 41-60: Curioso
- 61-80: Aberto
- 81-100: Vulneravel

### Tempo Atmosferico
- Relogio visivel no canto
- Cada interacao avanca 3-18 minutos
- Duracao varia por cliente (Yuki: 200min, Hiroto: 180min, outros: 150-160min)
- Primeira noite mais longa para o jogador se ambientar

### Finais
- **Perfeito:** 0 falhas, 6 memorias, envelope
- **Bom:** Max 1 falha, envelope
- **Neutro:** Max 2 falhas
- **Ruim:** 3+ falhas

### Envelope de Yuki
- So existe se Yuki (noite 1) foi sucesso
- Contem a verdade sobre o incendio
- Essencial para final perfeito

---

## Clientes

| Cliente | Descricao | Prato Gatilho | Nos de Dialogo |
|---------|-----------|---------------|----------------|
| **Yuki** | Fotografa, carrega envelope misterioso | Tamago Gohan | 99 |
| **Tanaka** | Bombeiro aposentado, tentou salvar Takeshi | Katsudon | 99 |
| **Ryo** | Taxista, fugiu do incendio | Ochazuke ou Curry Udon | 95 |
| **Midori** | Vizinha florista, viu faiscas | Missoshiru | 102 |
| **Sachiko** | Filha de Takeshi, caderno do pai | Nikujaga | 111 |
| **Hiroto** | Crianca que Master salvou (adulto agora) | Omurice | 86 |

**Total: ~590 nos de dialogo** — cada personagem tem arvore narrativa profunda
com multiplos caminhos, pistas progressivas e gatilhos emocionais.

---

## Pratos

| Prato | Nome Japones | Cliente Ideal |
|-------|--------------|---------------|
| Tamago Gohan | 卵かけご飯 | Yuki |
| Katsudon | カツ丼 | Tanaka |
| Ochazuke | お茶漬け | Ryo |
| Curry Udon | カレーうどん | Ryo |
| Missoshiru | 味噌汁 | Midori |
| Nikujaga | 肉じゃが | Sachiko |
| Omurice | オムライス | Hiroto |
| Onigiri | おにぎり | Generico |
| Gyudon | 牛丼 | Generico |

---

## Tecnologias

- **Python 3.x**
- **Rich:** Interface rica no terminal (cores, paineis, efeitos)
- **JSON:** Dados de clientes e dialogos

---

## Configuracao (config.py)

Parametros ajustaveis:

- `VELOCIDADE_DIGITACAO`: Efeito typewriter (0.03s padrao)
- `DURACAO_POR_CLIENTE`: Tempo por cliente em minutos
- `HORARIOS_CLIENTES`: Hora de chegada de cada cliente
- `FAIXAS_CONFIANCA`: Limiares dos estados emocionais

---

## Testes Automatizados

Suite de testes usando `pexpect` para automacao de terminal.

```bash
# Instalar dependencia de testes
pip install pexpect

# Testar cliente especifico
python tests/test_cliente.py yuki

# Testar tipo de final
python tests/test_finais.py perfeito
```

Documentacao completa em `tests/README.md`.

**Nota:** Testes validam execucao do jogo, mas tem limitacoes
com navegacao de dialogos complexos. Logica de finais verificada
via simulacao direta.

---

## Inspiracao

Baseado na serie de TV **Midnight Diner** (深夜食堂 Shinya Shokudo),
criada por Yaro Abe. O jogo conta a pre-historia da serie,
explicando a origem da cicatriz de Master.

---

*Atualizado: 18/01/2026 — v2.1 melhorias de UX e correcoes*

# Plano Otimizado — Midnight Kitchen v2.0

**Data:** 15/01/2026
**Status:** Aprovado para execução

---

## Resumo das Otimizações

Este plano corrige os riscos identificados no plano original:

1. **Vertical Slice primeiro** — Uma noite completa antes de expandir
2. **Contratos de interface** — Definir APIs entre módulos antes de codificar
3. **Sistema de tempo atmosférico** — Relógio visível, pressão sutil
4. **Save automático** — Persistência entre noites
5. **Onboarding estruturado** — Introdução pulável para jogadores veteranos

---

## Sistema de Tempo Atmosférico

### Conceito

- Relógio discreto visível no canto superior direito
- Cada interação avança o tempo (5-15 minutos de jogo)
- Cliente vai embora após ~2-3 horas de jogo (despedida melancólica)
- Cria tensão sem ser punitivo

### Especificação

```python
@dataclass
class SistemaTempo:
    hora_inicial: int      # Ex: 1, 2, 3 (1am, 2am, 3am)
    minuto_inicial: int    # Ex: 47 (1:47am)
    minutos_por_interacao: tuple[int, int]  # Range (5, 15)
    duracao_maxima: int    # Minutos até cliente ir embora (ex: 150)

    def avancar(self, tipo_interacao: str) -> None:
        """Avança o tempo baseado no tipo de interação."""

    def formatar_hora(self) -> str:
        """Retorna hora formatada (ex: '2:15')"""

    def tempo_esgotado(self) -> bool:
        """Retorna True se passou do limite."""
```

### Integração Visual

```
┌─ NOITE 1 ──────────────────────────────────── 1:47 ─┐
│                                                      │
│  A cortina de noren balança suavemente...           │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

## Sistema de Save

### Conceito

- Save automático ao final de cada noite
- Arquivo JSON único: `save.json`
- Menu inicial detecta save existente

### Dados Salvos

```python
@dataclass
class SaveData:
    noite_atual: int
    memorias_coletadas: list[tuple[str, str]]
    tem_envelope: bool
    falhas: int
    timestamp: str
```

### Fluxo

```
Início do Jogo
      │
      ▼
┌─────────────────┐
│ Existe save.json? │
└────────┬────────┘
    sim  │  não
         │    │
    ▼    │    ▼
┌────────┴────────┐
│ [1] Continuar   │
│ [2] Novo Jogo   │
└─────────────────┘
```

---

## Fluxo de Onboarding

### Estrutura

```
TELA TÍTULO
    │
    ▼
MENU (Continuar/Novo)
    │ (novo jogo)
    ▼
"Deseja ver a introdução completa?"
[1] Sim, é minha primeira vez
[2] Não, já conheço o jogo
    │
    ▼ (sim)
┌─────────────────────────────────────┐
│ INTRODUÇÃO COMPLETA                 │
│                                     │
│ 1. Contexto da série                │
│    - Midnight Diner (Shinya Shokudo)│
│    - O restaurante, Master          │
│                                     │
│ 2. Premissa deste jogo              │
│    - 10 anos antes da série         │
│    - Origem da cicatriz             │
│    - Como Master se tornou sábio    │
│                                     │
│ 3. Mecânicas                        │
│    - 7 noites, 6 clientes + reflexão│
│    - Diálogos e confiança           │
│    - O tempo passa (relógio)        │
│    - Save automático entre noites   │
│    - Múltiplos finais               │
│                                     │
└─────────────────────────────────────┘
    │
    ▼
NOITE 1
```

---

## Fases de Implementação

### Fase 1: Fundação (Contratos + Setup)

**Objetivo:** Estabelecer a base sólida

```
□ 1.1 Criar requirements.txt (rich)
□ 1.2 Criar config.py com constantes globais
□ 1.3 Criar estrutura de pastas
□ 1.4 Definir interfaces/contratos entre módulos
□ 1.5 Instalar dependências
```

**Arquivos:**
- `requirements.txt`
- `config.py`
- `contracts.py` (tipos e interfaces)

---

### Fase 2: UI Base

**Objetivo:** Sistema de renderização funcional

```
□ 2.1 ui/styles.py — Cores, temas, paleta
□ 2.2 ui/components.py — Painéis, menus, caixas
□ 2.3 ui/effects.py — Efeito de digitação
□ 2.4 ui/ascii_art.py — Logo, lanterna, decorações
□ 2.5 ui/renderer.py — Classe central de renderização
```

**Validação:** Conseguir renderizar um painel estilizado com texto.

---

### Fase 3: Core + Sistemas Base

**Objetivo:** Loop de jogo com tempo e save

```
□ 3.1 core/tempo.py — Sistema de tempo atmosférico
□ 3.2 core/save.py — Sistema de save/load
□ 3.3 core/game.py — Estado do jogo (refatorado)
□ 3.4 core/scene.py — Gerenciador de cenas
□ 3.5 Integrar tempo no renderer (relógio visível)
```

**Validação:** Loop básico funcionando com relógio e save.

---

### Fase 4: Vertical Slice (Noite da Yuki)

**Objetivo:** Uma noite completa e jogável

```
□ 4.1 dados/clientes/yuki.json — Dados da personagem
□ 4.2 dados/dialogos/yuki.json — Árvore de diálogo completa
□ 4.3 narrativa/yuki.py — Textos específicos da Yuki
□ 4.4 Integrar diálogo + cozinha + tempo
□ 4.5 Testar fluxo completo da noite
□ 4.6 Implementar despedida por tempo esgotado
```

**Validação:** Jogar a noite da Yuki do início ao fim.

---

### Fase 5: Onboarding + Menu

**Objetivo:** Experiência completa de início

```
□ 5.1 narrativa/abertura.py — Tela título e introdução
□ 5.2 narrativa/onboarding.py — Tutorial/mecânicas
□ 5.3 core/menu.py — Menu inicial com detecção de save
□ 5.4 Integrar fluxo completo de início
```

**Validação:** Novo jogador entende o jogo; veterano pode pular.

---

### Fase 6: Expansão (5 noites restantes)

**Objetivo:** Conteúdo completo

```
□ 6.1 Tanaka (noite 2) — dados + diálogos + narrativa
□ 6.2 Ryo (noite 3) — dados + diálogos + narrativa
□ 6.3 Midori (noite 4) — dados + diálogos + narrativa
□ 6.4 Sachiko (noite 5) — dados + diálogos + narrativa
□ 6.5 Hiroto (noite 6) — dados + diálogos + narrativa
□ 6.6 narrativa/transicoes.py — Entre noites
```

**Nota:** Estas podem ser paralelizadas após Fase 4 validada.

---

### Fase 7: Dia 7 + Finais

**Objetivo:** Conclusão narrativa

```
□ 7.1 Refatorar sistemas/reflexao.py
□ 7.2 Implementar 3 finais diferentes
□ 7.3 Integrar envelope de Yuki
□ 7.4 Narrativa de encerramento
```

---

### Fase 8: Polish + Revisão

**Objetivo:** Qualidade final

```
□ 8.1 Playtest completo
□ 8.2 Revisão de todos os textos
□ 8.3 Ajuste de timing e ritmo
□ 8.4 Code review
□ 8.5 Bug fixes
□ 8.6 Commit final
```

---

## Estrutura de Arquivos Final

```
midnight-kitchen/
├── main.py                    # Ponto de entrada
├── config.py                  # Constantes globais
├── contracts.py               # Tipos e interfaces
├── requirements.txt           # Dependências
│
├── core/                      # Núcleo do jogo
│   ├── __init__.py
│   ├── game.py                # Estado central
│   ├── scene.py               # Gerenciador de cenas
│   ├── tempo.py               # Sistema de tempo
│   ├── save.py                # Persistência
│   └── menu.py                # Menu inicial
│
├── ui/                        # Interface visual
│   ├── __init__.py
│   ├── styles.py              # Cores e temas
│   ├── components.py          # Painéis, menus
│   ├── effects.py             # Efeito digitação
│   ├── ascii_art.py           # Arte ASCII
│   └── renderer.py            # Renderização central
│
├── narrativa/                 # Conteúdo narrativo
│   ├── __init__.py
│   ├── abertura.py            # Título e intro
│   ├── onboarding.py          # Tutorial/mecânicas
│   ├── ambientacao.py         # Descrições ambiente
│   ├── transicoes.py          # Entre noites
│   └── monologos.py           # Pensamentos Master
│
├── sistemas/                  # Lógica de jogo
│   ├── __init__.py
│   ├── dialogo.py             # Sistema de diálogo
│   ├── cozinha.py             # Sistema de cozinha
│   └── reflexao.py            # Dia 7
│
├── models/                    # Entidades
│   ├── __init__.py
│   ├── cliente.py
│   ├── prato.py
│   └── memoria.py
│
├── dados/                     # Conteúdo JSON
│   ├── clientes/              # Um por personagem
│   │   ├── yuki.json
│   │   ├── tanaka.json
│   │   ├── ryo.json
│   │   ├── midori.json
│   │   ├── sachiko.json
│   │   └── hiroto.json
│   ├── dialogos/              # Árvores de diálogo
│   │   ├── yuki.json
│   │   ├── tanaka.json
│   │   ├── ryo.json
│   │   ├── midori.json
│   │   ├── sachiko.json
│   │   └── hiroto.json
│   └── pratos.json
│
└── saves/                     # Saves do jogador
    └── save.json
```

---

## Checkpoints de Validação

| Checkpoint | Critério de Sucesso |
|------------|---------------------|
| CP1 | `rich` instalado, estrutura criada |
| CP2 | Painel estilizado renderiza corretamente |
| CP3 | Relógio visível e avançando |
| CP4 | Noite da Yuki jogável início ao fim |
| CP5 | Menu detecta save, onboarding funciona |
| CP6 | 6 noites jogáveis |
| CP7 | Dia 7 e finais funcionando |
| CP8 | Jogo completo, polido, sem bugs |

---

## Estimativas

| Fase | Tempo Estimado |
|------|----------------|
| 1. Fundação | 15 min |
| 2. UI Base | 30-40 min |
| 3. Core + Tempo | 30-40 min |
| 4. Vertical Slice | 45-60 min |
| 5. Onboarding | 20-30 min |
| 6. Expansão (5 noites) | 90-120 min |
| 7. Dia 7 + Finais | 30-40 min |
| 8. Polish | 30-45 min |
| **Total** | **4-6 horas** |

---

*Plano otimizado criado em 15/01/2026*
*Pronto para execução*

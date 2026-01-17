# Testes Automatizados — Midnight Kitchen

Suite de testes automatizados para validar o funcionamento do jogo.
Utiliza `pexpect` para simular interacao de terminal.

---

## Arquivos

| Arquivo | Descricao |
|---------|-----------|
| `test_play.py` | Teste exploratório que joga o jogo automaticamente |
| `test_cliente.py` | Teste parametrizado por cliente individual |
| `test_finais.py` | Teste dos 4 tipos de finais do jogo |

---

## Requisitos

```bash
pip install pexpect
```

---

## Uso

### Testar um cliente especifico

```bash
python tests/test_cliente.py <cliente>
```

Clientes disponiveis: `yuki`, `tanaka`, `ryo`, `midori`, `sachiko`, `hiroto`

**Exemplo:**
```bash
python tests/test_cliente.py yuki
```

### Testar um tipo de final

```bash
python tests/test_finais.py <tipo_final>
```

Tipos disponiveis: `perfeito`, `bom`, `neutro`, `ruim`

**Exemplo:**
```bash
python tests/test_finais.py perfeito
```

### Jogar automaticamente (exploratorio)

```bash
python tests/test_play.py
```

---

## Mapeamento de Pratos

Ordem dos pratos no menu do jogo (indices 1-10):

| Indice | Prato | Cliente Ideal |
|--------|-------|---------------|
| 1 | Tamago Gohan | Yuki |
| 2 | Katsudon | Tanaka |
| 3 | Curry Udon | Ryo |
| 4 | Ochazuke | Ryo |
| 5 | Missoshiru | Midori |
| 6 | Nikujaga | Sachiko |
| 7 | Omurice | Hiroto |
| 8 | Onigiri | (generico) |
| 9 | Gyudon | (generico) |
| 10 | Yakitori | (generico) |

**Nota:** Ryo aceita tanto Curry Udon (3) quanto Ochazuke (4).

---

## Logica de Finais

O jogo determina o final baseado em:

```
PERFEITO: 0 falhas + 6 memorias + envelope de Yuki
BOM:      <= 1 falha + envelope de Yuki
NEUTRO:   <= 2 falhas (sem envelope)
RUIM:     3+ falhas
```

### Tipos de Resultado por Noite

| Resultado | Condicao | Conta como falha? |
|-----------|----------|-------------------|
| SUCESSO | Prato certo + memoria revelada | Nao |
| PARCIAL | Prato errado mas confianca >= 20 | **Nao** |
| FALHA_CONFIANCA | Confianca < 20 | Sim |
| FALHA_TEMPO | Tempo esgotado | Sim |

**Importante:** `PARCIAL` nao conta como falha! Isso significa que servir
o prato errado sem antagonizar o cliente resulta em PARCIAL, nao em falha.

---

## Limitacoes Conhecidas

### Teste de Final Perfeito

O teste automatizado tem dificuldade em obter o final PERFEITO porque:

1. **Deteccao de menu**: O teste detecta menus de pratos por nomes no texto,
   mas esses nomes tambem aparecem em dialogos normais

2. **Navegacao de dialogo**: O jogo requer navegar dialogos especificos
   para revelar o prato ideal e entrar na cena de cozinha

3. **Resultado**: O teste frequentemente obtém PARCIAL em vez de SUCESSO,
   resultando em final BOM em vez de PERFEITO

**Verificacao manual confirmou** que a logica de finais esta 100% correta:

```python
# Simulacao direta retorna 'perfeito' corretamente
game.contar_memorias()  # 6
game.contar_falhas()    # 0
game.tem_envelope       # True
game.determinar_final() # 'perfeito'
```

### Tempo de Execucao

- Teste de cliente individual: ~100 segundos
- Teste de final (6 noites): ~400 segundos (~7 minutos)

---

## Execucao Paralela com Subagentes

Os testes foram projetados para execucao paralela. Exemplo de uso com
Claude Code para testar todos os clientes simultaneamente:

```
# Lanca 6 subagentes em paralelo (um por cliente)
# Tempo total: ~100s (vs ~600s sequencial)
```

---

## Historico

- **2026-01-17**: Criacao inicial dos testes
  - `test_play.py`: Teste exploratorio
  - `test_cliente.py`: Teste parametrizado por cliente
  - `test_finais.py`: Teste de finais
  - Corrigido bug: indice de Midori era 4 (Ochazuke), corrigido para 5 (Missoshiru)
  - Verificada logica de finais via simulacao direta

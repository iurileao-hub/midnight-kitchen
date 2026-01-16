# Prompt de Analise de Dialogos — Midnight Kitchen

Use este prompt para analisar e polir os dialogos de cada personagem.

---

## Prompt para Analise Critica

```
Faca uma analise critica completa da estrutura de dialogo e conteudos do personagem [NOME].
Busque polimento de qualidade em termos de coerencia, naturalidade do fluxo e dos textos,
tanto pela personagem quanto por Master, para criar uma experiencia mais imersiva.

Analise os seguintes aspectos:

### 1. ESTRUTURA DA ARVORE
- Quantidade de nos e distribuicao
- Caminhos redundantes ou muito similares
- Convergencia para pontos-chave (prato, revelacao, despedida)
- Nos vazios ou incompletos
- Loops potenciais ou becos sem saida

### 2. COERENCIA NARRATIVA
- Progressao emocional: Fechado → Cauteloso → Curioso → Aberto → Vulneravel
- Velocidade das revelacoes (muito rapido? muito lento?)
- Consistencia de detalhes (nomes, objetos, descricoes)
- Pistas distribuidas apropriadamente ao longo da progressao
- Pensamentos de Master (`pensamento_master`) nos momentos certos

### 3. NATURALIDADE DAS FALAS DO PERSONAGEM
- Consistencia com maneirismos documentados em PERSONAGENS.md
- Padroes repetitivos de estrutura de fala
- Exposicao excessiva (revelar demais de uma vez)
- Falta de hesitacao em momentos de trauma
- Vocabulario consistente com perfil (idade, profissao, estado emocional)

### 4. NATURALIDADE DAS FALAS DE MASTER
- Opcoes apropriadas para cada nivel de confianca
- Opcoes filosoficas demais no inicio (devem aparecer so com confianca alta)
- Repeticao de ofertas de comida ou perguntas similares
- Balance entre silencio, perguntas e observacoes
- Consistencia com o perfil: "fala pouco, ouve muito"

### 5. FLUXO E TRANSICOES
- Transicoes abruptas entre nos
- Cenas de cozinha com texto de transicao adequado
- Revelacoes que podem acontecer mais de uma vez
- Conexao suave entre atos (chegada, aproximacao, revelacao, despedida)

### 6. VERIFICACOES ESPECIFICAS
- Contar quantas vezes palavras-chave aparecem (ex: "dez anos", nome do personagem)
- Identificar padroes estruturais repetidos (ex: "[Palavra]... Ela repete...")
- Verificar se todos os maneirismos do PERSONAGENS.md sao referenciados
- Checar se o prato gatilho tem momento de impacto adequado
```

---

## Checklist de Problemas Comuns

### Padroes de Fala Repetitivos
- [ ] Estrutura "[Palavra]... repete a palavra" usada mais de 3x
- [ ] Mesma abertura em multiplos nos ("E verdade.", "Talvez.", "E.")
- [ ] Perguntas retoricas demais do personagem

### Exposicao
- [ ] Nos com mais de 4 frases de revelacao consecutivas
- [ ] Personagem revela trauma antes de atingir confianca 60+
- [ ] Informacoes cruciais dadas sem pausas narrativas

### Opcoes de Master
- [ ] Mais de 5 variacoes de "quer comer algo?"
- [ ] Opcoes filosoficas disponiveis com confianca < 40
- [ ] Falta de opcoes de silencio em momentos tensos

### Consistencia
- [ ] Descricoes de objetos variam (ex: "envelope amarelado" vs "envelope pardo")
- [ ] Numeros inconsistentes (anos, idades, datas)
- [ ] Maneirismos do PERSONAGENS.md nao aparecem nos dialogos

### Estrutura
- [ ] Nos com `texto: ""` sem justificativa (transicao para cena)
- [ ] Caminhos que levam ao mesmo no sem diferenciacao
- [ ] Nos genericos (`tempo_esgotando`, `confianca_baixa`) sem transicao suave

---

## Principios de Reescrita

### 1. Variar Estrutura de Respostas
**Ruim:**
```
"Peso..."
Ela repete a palavra.
"E. Voce poderia dizer isso."
```

**Bom:**
```
Ela nao responde de imediato. Os dedos vao para a alca da camera.
"E." Uma pausa longa. "Voce poderia dizer isso."
```

### 2. Fragmentar Exposicoes Longas
**Ruim:**
```
"Um restaurante. Eu fotografei tudo. O fogo. As pessoas.
Um homem que entrou. Ele salvou uma crianca. O teto desabou."
```

**Bom:**
```
"Um restaurante pequeno."

Ela olha para as proprias maos.

"Eu estava com a camera. Nao pensei."

[Proximo no com opcao do jogador puxar mais]
```

### 3. Usar Maneirismos como Pontuacao Emocional
- Tocar a camera = nervosismo
- Olhar para a porta = desejo de fugir
- Segurar a bolsa = proteger o envelope
- Falar em frases curtas = estado fechado
- Frases mais longas = abrindo-se

### 4. Silencio como Ferramenta
Master e descrito como quem "ouve muito". Opcoes de silencio devem:
- Estar disponiveis em todos os momentos tensos
- Ter impacto de confianca positivo (mostrar respeito)
- Incluir acao sutil: `[Continuar secando o copo]`, `[Acenar levemente]`

### 5. Gradiente de Abertura nas Opcoes de Master

| Confianca | Tipo de Opcao |
|-----------|---------------|
| 0-20 | Praticas: "Quer comer?", "Cha?", silencio |
| 21-40 | Observacoes: "Bonita camera.", "Noite longa." |
| 41-60 | Perguntas gentis: "Faz tempo que fotografa?" |
| 61-80 | Empatia: "Parece carregar algo pesado." |
| 81-100 | Filosoficas: "Testemunhar e um peso." |

---

## Palavras/Frases a Monitorar

| Termo | Limite Recomendado | Alternativas |
|-------|-------------------|--------------|
| "dez anos" | Max 10x | "uma decada", "todo esse tempo", "desde aquela noite", "tantos anos" |
| "Ela repete" | Max 3x | Variar estrutura completamente |
| "E verdade" | Max 5x | "Talvez.", "Sim.", "Hmm.", silencio |
| "Posso preparar" | Max 6x | Acao direta, silencio, pergunta diferente |
| "Voce parece" | Max 5x | Observacao sobre objeto, ambiente, acao |

---

## Template de Revisao

Ao revisar, documente:

```
## Revisao: [NOME DO PERSONAGEM]

### Metricas Antes/Depois
- Total de nos: X → Y
- "dez anos" (ou equivalente): X → Y
- Padroes repetitivos: X → Y
- Opcoes de silencio: X → Y

### Mudancas Principais
1. [Descricao da mudanca]
2. [Descricao da mudanca]
...

### Nos Modificados
- no_id: [tipo de mudanca]
- no_id: [tipo de mudanca]
...

### Nos Removidos/Fundidos
- no_antigo → no_novo (motivo)
...

### Nos Adicionados
- no_novo: [proposito]
...
```

---

## Ordem de Analise Recomendada

1. **Yuki** (Noite 1) - Base de referencia ✓
2. **Tanaka** (Noite 2) - Contraste: homem mais velho, fala devagar
3. **Ryo** (Noite 3) - Desafio: personagem ansioso, fala rapido
4. **Midori** (Noite 4) - Contraste: naturalmente aberta, gentil
5. **Sachiko** (Noite 5) - Desafio: rigida, evita palavra "pai"
6. **Hiroto** (Noite 6) - Especial: reconhecimento de Master, climax

---

*Prompt criado em 16/01/2026*
*Baseado na analise de Yuki como referencia*

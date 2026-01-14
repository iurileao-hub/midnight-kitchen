# Plano de Aprendizagem: Midnight Kitchen

## Metodologia: "Esqueleto → Carne"

Este projeto usa uma abordagem de **tutoria guiada** onde:

| Claude (Tutor) | Você (Aprendiz) |
|----------------|-----------------|
| Cria estrutura de arquivos | Implementa lógica de negócio |
| Define assinaturas de métodos | Escreve o corpo dos métodos |
| Prepara contexto e imports | Toma decisões de design |
| Faz code review | Corrige e refatora |
| Explica conceitos quando necessário | Pergunta quando tem dúvidas |

---

## Fases do Projeto

### Fase 1: Fundamentos (Classes e Objetos)
**Objetivo:** Dominar a criação de classes, atributos e métodos

| Entregável | Quem Implementa | Conceitos |
|------------|-----------------|-----------|
| Classe `Cliente` | Você | `__init__`, atributos, métodos básicos |
| Classe `Prato` | Você | Encapsulamento, propriedades |
| Classe `Restaurante` | Você | Composição, estado |

**Critério de conclusão:** Todas as classes instanciam corretamente e métodos retornam valores esperados.

---

### Fase 2: Estruturas de Dados
**Objetivo:** Usar dicionários e listas de forma efetiva

| Entregável | Quem Implementa | Conceitos |
|------------|-----------------|-----------|
| Sistema de inventário | Você | Dicionários, CRUD |
| Sistema de receitas | Você | frozenset, lookup |
| Histórico de ações | Você | Listas, append, iteração |

**Critério de conclusão:** Sistema de cozinha funcional — selecionar ingredientes, validar receita, consumir inventário.

---

### Fase 3: Sistemas de Jogo
**Objetivo:** Integrar componentes em fluxos de gameplay

| Entregável | Quem Implementa | Conceitos |
|------------|-----------------|-----------|
| Sistema de diálogos | Você | Árvores de decisão, recursão |
| Loop da noite | Você | While loops, condicionais |
| Passagem de tempo | Você | Manipulação de strings/tempo |

**Critério de conclusão:** Uma noite completa jogável — cliente chega, conversa, come, vai embora.

---

### Fase 4: Dados e Persistência
**Objetivo:** Trabalhar com arquivos JSON

| Entregável | Quem Implementa | Conceitos |
|------------|-----------------|-----------|
| Carregar clientes.json | Você | json.load, file handling |
| Carregar pratos.json | Você | Tratamento de erros |
| Estruturar dados | Colaborativo | Design de schemas |

**Critério de conclusão:** Jogo carrega todos os dados de arquivos externos.

---

### Fase 5: Integração e Polimento
**Objetivo:** Jogo completo e jogável

| Entregável | Quem Implementa | Conceitos |
|------------|-----------------|-----------|
| Loop principal (main.py) | Você | Orquestração de sistemas |
| Noite 5 (revelação) | Colaborativo | Lógica condicional complexa |
| Polimento de UX | Colaborativo | Formatação, clear screen |

**Critério de conclusão:** Jogo jogável do início ao fim, com todos os 4 clientes + revelação final.

---

## Padrão de Cada Sessão

```
1. CONTEXTO (Claude)
   └─ Explico o que vamos construir e por quê

2. PREPARAÇÃO (Claude)
   └─ Crio arquivo com estrutura, imports, assinaturas de métodos
   └─ Adiciono comentários explicativos e TODOs

3. IMPLEMENTAÇÃO (Você)
   └─ Escreve o corpo dos métodos (5-15 linhas cada)
   └─ Testa localmente

4. REVISÃO (Claude)
   └─ Analiso seu código
   └─ Sugiro melhorias ou alternativas
   └─ Explico conceitos relacionados

5. COMMIT (Você)
   └─ Faz commit das alterações
   └─ Mensagem descritiva em português

6. PRÓXIMO (Claude)
   └─ Apresento o próximo desafio
```

---

## Registro de Progresso

### Fase 1: Fundamentos
- [ ] `Cliente.__init__()` — inicialização com atributos
- [ ] `Cliente.apresentar()` — retorna descrição formatada
- [ ] `Cliente.reagir()` — responde a ações do jogador
- [ ] `Prato.__init__()` — inicialização
- [ ] `Prato.preparar()` — retorna narrativa
- [ ] `Restaurante.__init__()` — estado inicial do jogo
- [ ] `Restaurante.avancar_tempo()` — manipula horário

### Fase 2: Estruturas de Dados
- [ ] Inventário como dicionário
- [ ] Sistema de receitas com frozenset
- [ ] Validação de ingredientes
- [ ] Consumo de ingredientes

### Fase 3: Sistemas de Jogo
- [ ] Árvore de diálogos
- [ ] Escolhas com input()
- [ ] Loop while da noite
- [ ] Condição de fim da noite

### Fase 4: Dados e Persistência
- [ ] Estrutura de clientes.json
- [ ] Estrutura de pratos.json
- [ ] Função carregar_dados()
- [ ] Tratamento de FileNotFoundError

### Fase 5: Integração
- [ ] main.py funcional
- [ ] 4 noites jogáveis
- [ ] Noite 5 com revelação
- [ ] Testes manuais completos

---

## Conceitos-Chave a Dominar

### Python Básico
- [x] Variáveis e tipos
- [ ] Funções com parâmetros e retorno
- [ ] Condicionais (if/elif/else)
- [ ] Loops (for, while)
- [ ] Tratamento de exceções (try/except)

### Orientação a Objetos
- [ ] Classes e instâncias
- [ ] Atributos de instância
- [ ] Métodos
- [ ] `__init__` e `self`
- [ ] Composição (objetos dentro de objetos)

### Estruturas de Dados
- [ ] Listas: criar, adicionar, iterar, filtrar
- [ ] Dicionários: criar, acessar, iterar, verificar chaves
- [ ] Sets e frozensets
- [ ] List/dict comprehensions

### Arquivos
- [ ] Abrir e ler arquivos (with open)
- [ ] JSON: load e dump
- [ ] Tratamento de erros de arquivo

### Boas Práticas
- [ ] Nomes descritivos (snake_case)
- [ ] Funções pequenas e focadas
- [ ] Comentários úteis (não óbvios)
- [ ] Git: commits frequentes e descritivos

---

## Dicas para Maximizar Aprendizado

1. **Tente antes de perguntar** — Gaste 5-10 minutos tentando resolver sozinho
2. **Leia os erros** — Mensagens de erro são pistas valiosas
3. **Teste incrementalmente** — Rode o código a cada poucas linhas
4. **Verbalize seu raciocínio** — Me explique o que você está tentando fazer
5. **Não copie cegamente** — Entenda cada linha antes de usar
6. **Refatore depois de funcionar** — Primeiro faça funcionar, depois faça bonito

---

## Recursos Complementares

- [Python Docs - Classes](https://docs.python.org/3/tutorial/classes.html)
- [Real Python - OOP](https://realpython.com/python3-object-oriented-programming/)
- [Python Docs - JSON](https://docs.python.org/3/library/json.html)

---

## Status Atual da Sessão

### Sessão 1 (07/01/2026)
**Status:** Pausada — aguardando implementação

**O que foi feito:**
- [x] Criada estrutura do projeto
- [x] Documentação inicial (README, DESIGN, APRENDIZAGEM)
- [x] Esqueleto da classe `Cliente` preparado

**Próxima tarefa:**
Implementar os 5 métodos da classe `Cliente` em `models/cliente.py`:

| Método | Linhas | Status |
|--------|--------|--------|
| `__init__` | ~8 | Pendente |
| `apresentar()` | ~5-8 | Pendente |
| `reagir(acao)` | ~10-15 | Pendente |
| `aumentar_confianca(qtd)` | ~2-3 | Pendente |
| `pode_revelar_segredo()` | 1 | Pendente |

**Como retomar:**
```bash
cd /Users/iurileao/Documents/Projects/midnight-kitchen
python models/cliente.py  # Para testar após implementar
```

**Dica:** Comece pelo `__init__`, depois `pode_revelar_segredo()` (mais fácil),
e deixe `reagir()` por último (mais complexo).

---

*Última atualização: 07/01/2026*

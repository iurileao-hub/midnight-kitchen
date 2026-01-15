"""
Abertura — Tela Título e Introdução do Midnight Kitchen.

A primeira impressão do jogador. Define o tom e expectativas.
"""


class Abertura:
    """Textos e sequências da abertura do jogo."""

    # Texto que aparece após o logo
    TAGLINE = '"O que você quer comer? Se eu tiver os ingredientes, eu faço."'

    SUBTITULO = "Uma história de culpa, memória e perdão."

    # Inspiração (aparece no onboarding ou créditos)
    INSPIRACAO = """Este jogo se passa 10 anos antes dos eventos
de "Midnight Diner" (深夜食堂 Shinya Shokudō).

Conta a história de como Master se tornou
o homem sábio e sereno que conhecemos na série."""

    # Introdução atmosférica (novo jogo)
    INTRODUCAO = """Tóquio, 2:00 da manhã.

Um beco silencioso no bairro de Shinjuku.
Uma cortina de noren balança suavemente.

Atrás dela, um pequeno restaurante.
Apenas seis lugares no balcão.
Um homem trabalha sozinho na cozinha.

Ele tem uma cicatriz no rosto.
Nunca fala sobre ela.

Há dez anos, algo aconteceu.
Algo que ele tenta esquecer toda noite.

Mas esta semana... será diferente."""

    # Introdução curta (para quem pula o tutorial)
    INTRODUCAO_CURTA = """Uma semana no Midnight Kitchen.

Seis clientes. Seis noites. Seis histórias.
E uma verdade que você carrega há dez anos."""

    # Texto de transição para o jogo
    TRANSICAO_INICIO = """A primeira noite começa.

O relógio marca quase duas da manhã.
A cortina de noren balança.

Alguém está chegando."""


class TextosMenu:
    """Textos para o menu principal."""

    OPCAO_CONTINUAR = "Continuar"
    OPCAO_NOVO_JOGO = "Novo Jogo"
    OPCAO_SAIR = "Sair"

    # Quando há save
    DESCRICAO_SAVE = "Noite {noite}, {memorias} {palavra_memoria}"

    # Confirmação de novo jogo quando há save
    CONFIRMAR_NOVO = """Você tem um jogo em andamento (Noite {noite}).

Começar um novo jogo irá apagar seu progresso.

Tem certeza?"""

    OPCAO_SIM = "Sim, começar do zero"
    OPCAO_NAO = "Não, voltar ao menu"

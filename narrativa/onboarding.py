"""
Onboarding — Tutorial e Introdução às Mecânicas.

Apresenta o jogo para novos jogadores de forma
não intrusiva e pulável.
"""


class Onboarding:
    """Textos e sequência do tutorial/onboarding."""

    # Pergunta inicial
    PERGUNTA_TUTORIAL = "Primeira vez no Midnight Kitchen?"

    OPCAO_SIM = "Sim, quero conhecer o jogo"
    OPCAO_NAO = "Não, já sei como funciona"

    # Seções do onboarding
    SECOES = [
        {
            "titulo": "Sobre o Jogo",
            "texto": """Este jogo é inspirado na série de TV "Midnight Diner"
(深夜食堂 Shinya Shokudō), criada por Yaro Abe.

Na série, Master é um homem enigmático que serve
clientes de madrugada, cada um com uma história.
A única coisa que se sabe sobre ele: uma cicatriz
no rosto, nunca explicada.

Este jogo conta a história de como essa cicatriz
surgiu — e como Master se tornou quem é.""",
        },
        {
            "titulo": "A Premissa",
            "texto": """Esta história se passa 10 anos antes da série.

Você é Master, antes de se tornar o homem sábio
e sereno que conhecemos. Ainda carrega feridas
que não cicatrizaram.

Uma semana. Seis clientes. Seis histórias.
E uma verdade que você tem evitado por dez anos.

Ao final, você entenderá a origem da cicatriz
— e do homem que ela criou.""",
        },
        {
            "titulo": "O Restaurante",
            "texto": """Você é dono de um pequeno restaurante que abre
apenas de madrugada, num beco de Shinjuku.

Seis lugares no balcão. Uma cozinha simples.
E clientes que chegam carregando mais do que fome.

Cada pessoa que entra pela cortina de noren
traz uma história. Algumas histórias precisam
ser ouvidas para serem curadas.""",
        },
        {
            "titulo": "A Conversa",
            "texto": """Seu trabalho é ouvir.

A cada momento, você terá opções do que dizer.
Algumas aproximam. Outras afastam.

Preste atenção no que os clientes dizem.
Às vezes, uma frase casual esconde
algo muito mais profundo.

A confiança deles cresce (ou diminui)
baseado em como você responde.""",
        },
        {
            "titulo": "O Tempo",
            "texto": """O relógio no canto da tela mostra a hora.

O tempo passa a cada interação.
Os clientes têm vidas — não podem ficar para sempre.

Se demorar demais para criar conexão,
eles irão embora. Gentilmente.
Mas irão embora.

Não é um cronômetro cruel. É a realidade.""",
        },
        {
            "titulo": "A Comida",
            "texto": """Às vezes, a palavra certa não é uma palavra.
É um prato.

Preste atenção nas histórias dos clientes.
Eles vão mencionar — direta ou indiretamente —
algo que os conecta a uma comida específica.

Quando você perceber qual é o prato certo,
prepare-o. Sirva-o. E deixe a comida
fazer o trabalho que palavras não conseguem.""",
        },
        {
            "titulo": "O Progresso",
            "texto": """São sete noites no total.
Seis clientes. E um dia de reflexão.

Seu progresso é salvo automaticamente
ao final de cada noite. Você pode parar
e continuar depois.

Cada noite que você consegue criar conexão
revela uma memória. Cada memória importa
para o final da história.""",
        },
        {
            "titulo": "Os Finais",
            "texto": """Suas escolhas importam.

O final que você recebe depende de quantas
conexões conseguiu criar. De quantas memórias
coletou. De quão bem você ouviu.

Não existe um jeito "certo" de jogar.
Mas existe um jeito atento.

Boa sorte, Master.""",
        },
    ]

    # Texto final do onboarding
    CONCLUSAO = """Você está pronto.

A primeira noite espera.
A cortina de noren balança.

Alguém está chegando."""


class DicasContextuais:
    """Dicas que aparecem durante o jogo (opcional)."""

    PRIMEIRA_ESCOLHA = "Dica: Observe os detalhes. Eles importam."
    CONFIANCA_BAIXA = "Dica: Às vezes, o silêncio diz mais que palavras."
    PRATO_REVELADO = "Dica: Você percebeu algo. Talvez seja hora de cozinhar."
    TEMPO_PASSANDO = "Dica: O tempo passa. Não há pressa, mas há limite."

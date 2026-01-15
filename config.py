"""
Configurações globais do Midnight Kitchen v2.0.

Centraliza constantes, configurações de tempo, cores,
e parâmetros de gameplay.
"""

from pathlib import Path

# ============================================================
# PATHS
# ============================================================

ROOT_DIR = Path(__file__).parent
DADOS_DIR = ROOT_DIR / "dados"
SAVES_DIR = ROOT_DIR / "saves"
CLIENTES_DIR = DADOS_DIR / "clientes"
DIALOGOS_DIR = DADOS_DIR / "dialogos"

# ============================================================
# GAMEPLAY
# ============================================================

TOTAL_NOITES = 7          # 6 clientes + 1 reflexão
MAX_FALHAS_FINAL_BOM = 1  # Máximo de falhas para final bom

# Sistema de confiança
CONFIANCA_INICIAL = 20
CONFIANCA_FECHADO = (0, 20)
CONFIANCA_CAUTELOSO = (21, 40)
CONFIANCA_CURIOSO = (41, 60)
CONFIANCA_ABERTO = (61, 80)
CONFIANCA_VULNERAVEL = (81, 100)

# ============================================================
# SISTEMA DE TEMPO
# ============================================================

# Tempo avança por tipo de interação (minutos de jogo)
TEMPO_POR_INTERACAO = {
    "dialogo_curto": (3, 7),      # Resposta curta
    "dialogo_medio": (5, 12),     # Conversa normal
    "dialogo_longo": (10, 18),    # Revelação profunda
    "silencio": (2, 5),           # Pausa silenciosa
    "cozinha": (8, 15),           # Preparar prato
    "servir": (3, 5),             # Servir prato
}

# Duração máxima antes do cliente ir embora (minutos de jogo)
DURACAO_MAXIMA_NOITE = 150  # 2h30 de "tempo de jogo" (padrão)

# Duração específica por cliente (None = usa padrão)
# Primeira noite mais generosa para o jogador se ambientar
DURACAO_POR_CLIENTE = {
    "yuki": 200,      # Primeira noite: mais tempo para aprender
    "tanaka": 160,    # Segunda noite: um pouco mais
    "ryo": 150,       # Normal
    "midori": 150,    # Normal
    "sachiko": 150,   # Normal
    "hiroto": 180,    # Final: mais tempo para a revelação
}

# Horários de chegada de cada cliente
HORARIOS_CLIENTES = {
    "yuki": (1, 47),      # 1:47
    "tanaka": (2, 23),    # 2:23
    "ryo": (3, 15),       # 3:15
    "midori": (0, 30),    # 0:30
    "sachiko": (23, 58),  # 23:58 (quase meia-noite)
    "hiroto": (2, 0),     # 2:00 (hora do incêndio)
}

# ============================================================
# UI / VISUAL
# ============================================================

# Largura padrão dos painéis
LARGURA_PAINEL = 70

# Velocidade do efeito de digitação (segundos entre caracteres)
VELOCIDADE_DIGITACAO = 0.02
VELOCIDADE_DIGITACAO_RAPIDA = 0.01
VELOCIDADE_DIGITACAO_DRAMATICA = 0.04

# Pausa entre parágrafos (segundos)
PAUSA_PARAGRAFO = 0.5
PAUSA_DRAMATICA = 1.5

# ============================================================
# CORES (usando nomes do rich)
# ============================================================

CORES = {
    # Tema principal
    "primaria": "dark_orange",
    "secundaria": "grey70",
    "fundo": "grey11",

    # Texto
    "texto": "grey85",
    "texto_sutil": "grey50",
    "destaque": "wheat1",

    # Estados emocionais
    "fechado": "grey50",
    "cauteloso": "dark_khaki",
    "curioso": "khaki1",
    "aberto": "pale_green1",
    "vulneravel": "light_coral",

    # UI
    "borda": "grey35",
    "borda_ativa": "dark_orange",
    "menu_item": "grey70",
    "menu_selecionado": "wheat1",

    # Tempo
    "relogio": "grey50",
    "relogio_urgente": "indian_red",

    # Especiais
    "pensamento": "italic grey62",
    "memoria": "light_steel_blue",
    "erro": "red1",
    "sucesso": "green3",
}

# ============================================================
# SAVE
# ============================================================

SAVE_FILENAME = "save.json"
SAVE_VERSION = 1

# ============================================================
# DEBUG
# ============================================================

DEBUG_MODE = False
SKIP_ANIMACOES = False  # Para testes rápidos

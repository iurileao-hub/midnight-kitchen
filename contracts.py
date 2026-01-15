"""
Contratos e Tipos — Midnight Kitchen v2.0

Define interfaces e tipos compartilhados entre módulos.
Isso garante que todos os componentes "falem a mesma língua".
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Callable
from datetime import datetime


# ============================================================
# ENUMS
# ============================================================

class EstadoEmocional(Enum):
    """Estados emocionais dos clientes."""
    FECHADO = "fechado"
    CAUTELOSO = "cauteloso"
    CURIOSO = "curioso"
    ABERTO = "aberto"
    VULNERAVEL = "vulneravel"


class TipoInteracao(Enum):
    """Tipos de interação que afetam o tempo."""
    DIALOGO_CURTO = "dialogo_curto"
    DIALOGO_MEDIO = "dialogo_medio"
    DIALOGO_LONGO = "dialogo_longo"
    SILENCIO = "silencio"
    COZINHA = "cozinha"
    SERVIR = "servir"


class TipoCena(Enum):
    """Tipos de cena no jogo."""
    TITULO = "titulo"
    MENU = "menu"
    ONBOARDING = "onboarding"
    NOITE = "noite"
    DIALOGO = "dialogo"
    COZINHA = "cozinha"
    TRANSICAO = "transicao"
    REFLEXAO = "reflexao"
    FINAL = "final"


class ResultadoNoite(Enum):
    """Resultado possível de uma noite."""
    SUCESSO = "sucesso"           # Memória revelada
    FALHA_TEMPO = "falha_tempo"   # Cliente foi embora por tempo
    FALHA_CONFIANCA = "falha_confianca"  # Confiança muito baixa
    PARCIAL = "parcial"           # Alguma conexão, mas sem revelação


# ============================================================
# DATA CLASSES - DADOS
# ============================================================

@dataclass
class DadosCliente:
    """Dados estáticos de um cliente (carregado do JSON)."""
    id: str
    nome: str
    idade: int
    profissao: str
    descricao_chegada: str
    genero_masculino: bool
    prato_favorito: str
    memoria: str
    hora_chegada: tuple[int, int]
    maneirismos: list[str] = field(default_factory=list)
    pistas: list[str] = field(default_factory=list)


@dataclass
class NoDialogo:
    """Um nó na árvore de diálogo."""
    id: str
    texto: str  # O que o cliente diz
    opcoes: list["OpcaoDialogo"] = field(default_factory=list)
    confianca_minima: int = 0  # Só aparece se confiança >= este valor
    e_pista: bool = False      # Se este texto contém uma pista
    e_revelacao: bool = False  # Se este é o momento de revelação


@dataclass
class OpcaoDialogo:
    """Uma opção de resposta do jogador."""
    texto: str                    # O que Master diz
    dica: str = ""               # Dica sutil para o jogador (ex: "[observador]")
    impacto_confianca: int = 0   # Quanto afeta a confiança
    tipo_interacao: TipoInteracao = TipoInteracao.DIALOGO_MEDIO
    proximo_no: Optional[str] = None  # ID do próximo nó
    requer_pista: Optional[str] = None  # Só aparece se jogador captou pista


@dataclass
class DadosPrato:
    """Dados de um prato."""
    nome: str
    descricao: str
    narrativa_preparo: str
    tempo_preparo: int  # Minutos de jogo


# ============================================================
# DATA CLASSES - ESTADO
# ============================================================

@dataclass
class EstadoTempo:
    """Estado atual do sistema de tempo."""
    hora: int
    minuto: int
    minutos_passados: int = 0

    def formatar(self) -> str:
        """Retorna hora formatada (ex: '2:15')."""
        return f"{self.hora}:{self.minuto:02d}"

    def avancar(self, minutos: int) -> None:
        """Avança o tempo."""
        self.minutos_passados += minutos
        total_minutos = self.hora * 60 + self.minuto + minutos
        self.hora = (total_minutos // 60) % 24
        self.minuto = total_minutos % 60


@dataclass
class EstadoCliente:
    """Estado dinâmico de um cliente durante a noite."""
    dados: DadosCliente
    confianca: int = 20
    prato_descoberto: bool = False
    memoria_revelada: bool = False
    pistas_captadas: list[str] = field(default_factory=list)
    no_dialogo_atual: Optional[str] = None

    @property
    def estado_emocional(self) -> EstadoEmocional:
        """Retorna o estado emocional baseado na confiança."""
        if self.confianca <= 20:
            return EstadoEmocional.FECHADO
        elif self.confianca <= 40:
            return EstadoEmocional.CAUTELOSO
        elif self.confianca <= 60:
            return EstadoEmocional.CURIOSO
        elif self.confianca <= 80:
            return EstadoEmocional.ABERTO
        else:
            return EstadoEmocional.VULNERAVEL


@dataclass
class EstadoJogo:
    """Estado global do jogo."""
    noite_atual: int = 0
    memorias: list[tuple[str, str]] = field(default_factory=list)
    tem_envelope: bool = False
    resultados_noites: list[ResultadoNoite] = field(default_factory=list)

    def contar_falhas(self) -> int:
        """Conta quantas noites falharam."""
        falhas = [ResultadoNoite.FALHA_TEMPO, ResultadoNoite.FALHA_CONFIANCA]
        return sum(1 for r in self.resultados_noites if r in falhas)

    def pode_final_bom(self) -> bool:
        """Verifica se final bom é possível."""
        return self.contar_falhas() <= 1


@dataclass
class SaveData:
    """Dados de save do jogo."""
    version: int = 1
    noite_atual: int = 0
    memorias: list[tuple[str, str]] = field(default_factory=list)
    tem_envelope: bool = False
    resultados_noites: list[str] = field(default_factory=list)
    timestamp: str = ""

    def to_dict(self) -> dict:
        """Converte para dicionário (para JSON)."""
        return {
            "version": self.version,
            "noite_atual": self.noite_atual,
            "memorias": self.memorias,
            "tem_envelope": self.tem_envelope,
            "resultados_noites": self.resultados_noites,
            "timestamp": self.timestamp or datetime.now().isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "SaveData":
        """Cria instância a partir de dicionário."""
        return cls(
            version=data.get("version", 1),
            noite_atual=data.get("noite_atual", 0),
            memorias=data.get("memorias", []),
            tem_envelope=data.get("tem_envelope", False),
            resultados_noites=data.get("resultados_noites", []),
            timestamp=data.get("timestamp", ""),
        )


# ============================================================
# PROTOCOLOS / INTERFACES
# ============================================================

@dataclass
class RenderContext:
    """Contexto passado para funções de renderização."""
    largura: int = 70
    tempo: Optional[EstadoTempo] = None
    noite: int = 0
    estado_cliente: Optional[EstadoCliente] = None


# Tipo para callbacks de renderização
RenderCallback = Callable[[str, RenderContext], None]

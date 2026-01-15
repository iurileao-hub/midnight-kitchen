"""
Sistema de Cozinha v2 — Midnight Kitchen.

Gerencia a preparação de pratos, narrativas de cozinha,
e a conexão emocional entre prato e cliente.
"""

import json
from pathlib import Path
from dataclasses import dataclass
from typing import Optional

from config import DADOS_DIR
from contracts import TipoInteracao


@dataclass
class Prato:
    """Representa um prato do cardápio."""
    id: str
    nome: str
    nome_japones: str
    descricao: str
    tempo_preparo: int
    cliente_ideal: Optional[str]
    narrativa_preparo: str
    narrativa_servir: str
    reacao_correta: str
    reacao_errada: str


@dataclass
class ResultadoPrato:
    """Resultado de servir um prato."""
    sucesso: bool
    narrativa_preparo: str
    narrativa_servir: str
    reacao: str
    memoria_revelada: Optional[str] = None


class SistemaCozinha:
    """
    Sistema de cozinha do Midnight Kitchen v2.

    Gerencia o cardápio, preparação de pratos,
    e as reações dos clientes.
    """

    def __init__(self):
        self._pratos: dict[str, Prato] = {}
        self._carregar_pratos()

    def _carregar_pratos(self) -> None:
        """Carrega os pratos do arquivo JSON."""
        pratos_path = DADOS_DIR / "pratos.json"

        try:
            with open(pratos_path, "r", encoding="utf-8") as f:
                dados = json.load(f)

            for id_prato, info in dados.get("pratos", {}).items():
                self._pratos[id_prato] = Prato(
                    id=id_prato,
                    nome=info.get("nome", ""),
                    nome_japones=info.get("nome_japones", ""),
                    descricao=info.get("descricao", ""),
                    tempo_preparo=info.get("tempo_preparo", 10),
                    cliente_ideal=info.get("cliente_ideal"),
                    narrativa_preparo=info.get("narrativa_preparo", ""),
                    narrativa_servir=info.get("narrativa_servir", ""),
                    reacao_correta=info.get("reacao_correta", ""),
                    reacao_errada=info.get("reacao_errada", info.get("reacao_generica", "")),
                )

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Erro ao carregar pratos: {e}")

    def listar_pratos(self) -> list[tuple[str, str, str]]:
        """
        Lista todos os pratos disponíveis.

        Returns:
            Lista de tuplas (id, nome, descricao)
        """
        return [
            (p.id, p.nome, p.descricao)
            for p in self._pratos.values()
        ]

    def obter_prato(self, prato_id: str) -> Optional[Prato]:
        """Retorna um prato pelo ID."""
        return self._pratos.get(prato_id)

    def preparar_prato(self, prato_id: str) -> Optional[str]:
        """
        Retorna a narrativa de preparação de um prato.

        Returns:
            Texto narrativo da preparação.
        """
        prato = self._pratos.get(prato_id)
        if prato:
            return prato.narrativa_preparo
        return None

    def servir_prato(
        self,
        prato_id: str,
        cliente_id: str
    ) -> ResultadoPrato:
        """
        Serve um prato para um cliente.

        Args:
            prato_id: ID do prato a servir
            cliente_id: ID do cliente

        Returns:
            ResultadoPrato com narrativas e resultado
        """
        prato = self._pratos.get(prato_id)
        if not prato:
            return ResultadoPrato(
                sucesso=False,
                narrativa_preparo="",
                narrativa_servir="",
                reacao="Prato não encontrado.",
            )

        # Verifica se é o prato ideal
        sucesso = prato.cliente_ideal == cliente_id

        if sucesso:
            reacao = prato.reacao_correta
            # Extrai memória do texto de reação (para o sistema de jogo)
            memoria = f"Revelou sua história através de {prato.nome}"
        else:
            reacao = prato.reacao_errada
            memoria = None

        return ResultadoPrato(
            sucesso=sucesso,
            narrativa_preparo=prato.narrativa_preparo,
            narrativa_servir=prato.narrativa_servir,
            reacao=reacao,
            memoria_revelada=memoria,
        )

    def obter_tempo_preparo(self, prato_id: str) -> int:
        """Retorna o tempo de preparo em minutos de jogo."""
        prato = self._pratos.get(prato_id)
        return prato.tempo_preparo if prato else 10


# Teste rápido
if __name__ == "__main__":
    print("=== TESTE SISTEMA COZINHA V2 ===\n")

    cozinha = SistemaCozinha()

    print("Cardápio:")
    for id_prato, nome, desc in cozinha.listar_pratos():
        print(f"  • {nome}: {desc[:50]}...")

    print("\n--- Preparando Tamago Gohan ---")
    narrativa = cozinha.preparar_prato("tamago_gohan")
    if narrativa:
        print(narrativa[:200] + "...")

    print("\n--- Servindo para Yuki ---")
    resultado = cozinha.servir_prato("tamago_gohan", "yuki")
    print(f"Sucesso: {resultado.sucesso}")
    print(f"Reação: {resultado.reacao[:150]}...")

    print("\n--- Servindo prato errado ---")
    resultado = cozinha.servir_prato("onigiri", "yuki")
    print(f"Sucesso: {resultado.sucesso}")
    print(f"Reação: {resultado.reacao[:100]}...")

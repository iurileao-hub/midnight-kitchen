"""
Sistema de Save — Midnight Kitchen.

Salva automaticamente o progresso ao final de cada noite.
Permite continuar de onde parou em sessões futuras.
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Optional

from config import SAVES_DIR, SAVE_FILENAME, SAVE_VERSION
from contracts import SaveData, ResultadoNoite


class SistemaSave:
    """
    Gerencia a persistência do jogo.

    Save automático entre noites, permitindo que o jogador
    continue sua jornada em múltiplas sessões.
    """

    def __init__(self, diretorio: Optional[Path] = None):
        """
        Inicializa o sistema de save.

        Args:
            diretorio: Pasta onde salvar (padrão: saves/)
        """
        self.diretorio = diretorio or SAVES_DIR
        self.arquivo = self.diretorio / SAVE_FILENAME

        # Garante que o diretório existe
        self.diretorio.mkdir(parents=True, exist_ok=True)

    def existe_save(self) -> bool:
        """Verifica se existe um save válido."""
        if not self.arquivo.exists():
            return False

        try:
            save = self.carregar()
            return save is not None and save.noite_atual > 0
        except Exception:
            return False

    def carregar(self) -> Optional[SaveData]:
        """
        Carrega o save do disco.

        Returns:
            SaveData se existir, None caso contrário.
        """
        if not self.arquivo.exists():
            return None

        try:
            with open(self.arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)

            # Verifica versão
            if dados.get("version", 0) != SAVE_VERSION:
                # Versão incompatível - poderia fazer migração
                return None

            return SaveData.from_dict(dados)

        except (json.JSONDecodeError, KeyError, TypeError):
            return None

    def salvar(self, save_data: SaveData) -> bool:
        """
        Salva o progresso no disco.

        Args:
            save_data: Dados a salvar

        Returns:
            True se salvou com sucesso.
        """
        try:
            # Atualiza timestamp
            save_data.timestamp = datetime.now().isoformat()

            with open(self.arquivo, "w", encoding="utf-8") as f:
                json.dump(save_data.to_dict(), f, indent=2, ensure_ascii=False)

            return True

        except Exception as e:
            print(f"Erro ao salvar: {e}")
            return False

    def criar_save_de_jogo(
        self,
        noite_atual: int,
        memorias: list[tuple[str, str]],
        tem_envelope: bool,
        resultados: list[ResultadoNoite],
    ) -> SaveData:
        """
        Cria um SaveData a partir do estado atual do jogo.
        """
        return SaveData(
            version=SAVE_VERSION,
            noite_atual=noite_atual,
            memorias=memorias,
            tem_envelope=tem_envelope,
            resultados_noites=[r.value for r in resultados],
            timestamp=datetime.now().isoformat(),
        )

    def apagar_save(self) -> bool:
        """
        Apaga o save existente.

        Usado quando o jogador quer começar do zero.
        """
        try:
            if self.arquivo.exists():
                self.arquivo.unlink()
            return True
        except Exception:
            return False

    def obter_resumo(self) -> Optional[dict]:
        """
        Retorna um resumo do save para exibir no menu.

        Útil para mostrar "Continuar (Noite 3, 4 memórias)"
        """
        save = self.carregar()
        if not save:
            return None

        # Conta sucessos e falhas
        sucessos = sum(1 for r in save.resultados_noites if r == "sucesso")
        falhas = len(save.resultados_noites) - sucessos

        # Formata data
        try:
            data = datetime.fromisoformat(save.timestamp)
            data_formatada = data.strftime("%d/%m/%Y %H:%M")
        except Exception:
            data_formatada = "Data desconhecida"

        return {
            "noite": save.noite_atual,
            "memorias": len(save.memorias),
            "sucessos": sucessos,
            "falhas": falhas,
            "tem_envelope": save.tem_envelope,
            "data": data_formatada,
        }


# Teste rápido
if __name__ == "__main__":
    print("=== TESTE SISTEMA DE SAVE ===\n")

    sistema = SistemaSave()

    # Verifica se existe save
    print(f"Save existe? {sistema.existe_save()}")

    # Cria um save de teste
    save = sistema.criar_save_de_jogo(
        noite_atual=3,
        memorias=[("Yuki", "Fotos do incêndio"), ("Tanaka", "Culpa pelo acidente")],
        tem_envelope=True,
        resultados=[ResultadoNoite.SUCESSO, ResultadoNoite.SUCESSO, ResultadoNoite.FALHA_TEMPO],
    )

    # Salva
    print(f"\nSalvando... {sistema.salvar(save)}")

    # Carrega de volta
    carregado = sistema.carregar()
    if carregado:
        print(f"\nCarregado:")
        print(f"  Noite: {carregado.noite_atual}")
        print(f"  Memórias: {carregado.memorias}")
        print(f"  Envelope: {carregado.tem_envelope}")
        print(f"  Resultados: {carregado.resultados_noites}")

    # Resumo
    resumo = sistema.obter_resumo()
    if resumo:
        print(f"\nResumo para menu:")
        print(f"  Noite {resumo['noite']}, {resumo['memorias']} memórias")
        print(f"  Sucessos: {resumo['sucessos']}, Falhas: {resumo['falhas']}")
        print(f"  Salvo em: {resumo['data']}")

    # Limpa o save de teste
    sistema.apagar_save()
    print(f"\nSave apagado. Existe? {sistema.existe_save()}")

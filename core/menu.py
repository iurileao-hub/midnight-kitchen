"""
Menu — Menu Principal do Midnight Kitchen.

Gerencia o fluxo de início: título, continuar/novo,
onboarding, e transição para o jogo.
"""

from typing import Optional, Callable
from enum import Enum, auto

from ui.renderer import Renderer
from ui.ascii_art import AsciiArt
from core.save import SistemaSave
from narrativa.abertura import Abertura, TextosMenu
from narrativa.onboarding import Onboarding


class AcaoMenu(Enum):
    """Ações possíveis do menu."""
    CONTINUAR = auto()
    NOVO_JOGO = auto()
    SAIR = auto()


class Menu:
    """
    Menu principal do jogo.

    Gerencia o fluxo completo de início,
    desde a tela de título até começar o jogo.
    """

    def __init__(self, renderer: Renderer):
        self.renderer = renderer
        self.save = SistemaSave()

    def executar(self) -> AcaoMenu:
        """
        Executa o fluxo completo do menu.

        Returns:
            AcaoMenu indicando o que fazer (CONTINUAR, NOVO_JOGO, SAIR)
        """
        # Tela de título
        self._mostrar_titulo()

        # Menu principal
        acao = self._mostrar_menu_principal()

        if acao == AcaoMenu.SAIR:
            return acao

        if acao == AcaoMenu.NOVO_JOGO:
            # Verifica se precisa confirmar
            if self.save.existe_save():
                if not self._confirmar_novo_jogo():
                    return self.executar()  # Volta ao menu

            # Apaga save antigo
            self.save.apagar_save()

            # Onboarding
            self._executar_onboarding()

            # Introdução
            self._mostrar_introducao()

        elif acao == AcaoMenu.CONTINUAR:
            # Mostra resumo e transição rápida
            self._mostrar_retorno()

        return acao

    def _mostrar_titulo(self) -> None:
        """Mostra a tela de título."""
        self.renderer.limpar()
        self.renderer.mostrar_logo()
        self.renderer.espaco()
        self.renderer.console.print(
            f"[destaque]{Abertura.TAGLINE}[/destaque]",
            justify="center"
        )
        self.renderer.console.print(
            f"\n[sutil]{Abertura.SUBTITULO}[/sutil]",
            justify="center"
        )
        self.renderer.espaco(2)

    def _mostrar_menu_principal(self) -> AcaoMenu:
        """Mostra o menu principal e retorna a escolha."""
        opcoes = []

        # Verifica se há save
        if self.save.existe_save():
            resumo = self.save.obter_resumo()
            if resumo:
                # Formata descrição do save
                noite = resumo["noite"]
                memorias = resumo["memorias"]
                palavra = "memória" if memorias == 1 else "memórias"
                desc = f"Noite {noite}, {memorias} {palavra}"

                opcoes.append((TextosMenu.OPCAO_CONTINUAR, desc))
            else:
                opcoes.append((TextosMenu.OPCAO_CONTINUAR, ""))

        opcoes.append((TextosMenu.OPCAO_NOVO_JOGO, ""))
        opcoes.append((TextosMenu.OPCAO_SAIR, ""))

        escolha = self.renderer.mostrar_menu("", opcoes, permitir_cancelar=False)

        # Mapeia escolha para ação
        tem_save = self.save.existe_save()
        if tem_save:
            acoes = [AcaoMenu.CONTINUAR, AcaoMenu.NOVO_JOGO, AcaoMenu.SAIR]
        else:
            acoes = [AcaoMenu.NOVO_JOGO, AcaoMenu.SAIR]

        return acoes[escolha - 1]

    def _confirmar_novo_jogo(self) -> bool:
        """
        Confirma se o jogador quer começar novo jogo.

        Returns:
            True se confirmou, False se cancelou.
        """
        resumo = self.save.obter_resumo()
        noite = resumo["noite"] if resumo else "?"

        self.renderer.limpar()
        texto = TextosMenu.CONFIRMAR_NOVO.format(noite=noite)
        self.renderer.console.print(f"\n{texto}\n")

        opcoes = [
            (TextosMenu.OPCAO_SIM, ""),
            (TextosMenu.OPCAO_NAO, ""),
        ]
        escolha = self.renderer.mostrar_menu("", opcoes, permitir_cancelar=False)

        return escolha == 1

    def _executar_onboarding(self) -> None:
        """Executa a sequência de onboarding."""
        self.renderer.limpar()

        # Pergunta se quer tutorial
        self.renderer.mostrar_titulo(Onboarding.PERGUNTA_TUTORIAL)

        opcoes = [
            (Onboarding.OPCAO_SIM, "recomendado"),
            (Onboarding.OPCAO_NAO, ""),
        ]
        escolha = self.renderer.mostrar_menu("", opcoes, permitir_cancelar=False)

        if escolha == 2:
            # Pula tutorial - mostra introdução curta
            self.renderer.transicao()
            self.renderer.mostrar_narrativa(
                Abertura.INTRODUCAO_CURTA,
                titulo="Midnight Kitchen",
                digitar=False,
            )
            self.renderer.pausar()
            return

        # Executa tutorial completo
        for secao in Onboarding.SECOES:
            self.renderer.transicao()
            self.renderer.mostrar_narrativa(
                secao["texto"],
                titulo=secao["titulo"],
                digitar=True,
            )
            self.renderer.pausar()

        # Conclusão
        self.renderer.transicao()
        self.renderer.mostrar_narrativa(
            Onboarding.CONCLUSAO,
            titulo="Pronto",
            digitar=True,
        )
        self.renderer.pausar()

    def _mostrar_introducao(self) -> None:
        """Mostra a introdução completa para novo jogo."""
        self.renderer.transicao()

        # Introdução atmosférica
        self.renderer.mostrar_narrativa(
            Abertura.INTRODUCAO,
            titulo="Prólogo",
            digitar=True,
        )
        self.renderer.pausar()

        # Transição para o jogo
        self.renderer.transicao()
        self.renderer.mostrar_narrativa(
            Abertura.TRANSICAO_INICIO,
            digitar=True,
        )
        self.renderer.pausar()

    def _mostrar_retorno(self) -> None:
        """Mostra mensagem de retorno para jogo salvo."""
        resumo = self.save.obter_resumo()

        self.renderer.transicao()

        if resumo:
            texto = f"""Bem-vindo de volta.

Noite {resumo['noite']} espera.
{resumo['memorias']} {'memória coletada' if resumo['memorias'] == 1 else 'memórias coletadas'}.

A cortina de noren balança."""

            self.renderer.mostrar_narrativa(texto, titulo="Retorno", digitar=True)
        else:
            self.renderer.mostrar_narrativa(
                Abertura.TRANSICAO_INICIO,
                digitar=True,
            )

        self.renderer.pausar()


# Teste
if __name__ == "__main__":
    print("=== TESTE MENU ===\n")

    renderer = Renderer()
    menu = Menu(renderer)

    acao = menu.executar()
    print(f"\nAção escolhida: {acao}")

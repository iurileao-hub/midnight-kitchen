#!/usr/bin/env python3
"""
Midnight Kitchen v2.0 — Ponto de Entrada Principal.

Uma história de culpa, memória e perdão.
Dez anos antes de Midnight Diner.
"""

from typing import Optional

from ui.renderer import Renderer
from core.game import Game
from core.menu import Menu, AcaoMenu
from core.noite import Noite, ResultadoNoiteCompleto
from sistemas.reflexao import SistemaReflexao
from contracts import ResultadoNoite


# Ordem dos clientes por noite
CLIENTES = ["yuki", "tanaka", "ryo", "midori", "sachiko", "hiroto"]


def executar_jogo():
    """
    Loop principal do Midnight Kitchen.

    Coordena menu, noites, e sistema de save.
    """
    renderer = Renderer()
    game = Game()

    # Menu inicial
    menu = Menu(renderer)
    acao = menu.executar()

    if acao == AcaoMenu.SAIR:
        mostrar_despedida(renderer)
        return

    # Carrega save se estiver continuando
    if acao == AcaoMenu.CONTINUAR:
        game.carregar()
        noite_inicial = game.noite_atual
    else:
        noite_inicial = 0

    # Loop das noites
    for i, cliente_id in enumerate(CLIENTES):
        noite_num = i + 1

        # Pula noites já completadas
        if noite_num <= noite_inicial:
            continue

        # Executa a noite
        resultado = executar_noite(game, renderer, cliente_id)

        # Processa resultado
        if resultado.resultado == ResultadoNoite.SUCESSO:
            game.registrar_sucesso(resultado.cliente_nome, resultado.memoria or "")
        elif resultado.resultado == ResultadoNoite.FALHA_TEMPO:
            game.registrar_falha(ResultadoNoite.FALHA_TEMPO)
        else:
            game.registrar_falha(resultado.resultado)

        # Salva progresso
        game.salvar()

        # Transição entre noites
        if noite_num < len(CLIENTES):
            mostrar_transicao(renderer, noite_num)

    # Dia 7 - Reflexão (inclui final e créditos)
    if game.noite_atual >= len(CLIENTES):
        executar_reflexao(game, renderer)
    else:
        # Se saiu antes de completar todas as noites, mostra despedida simples
        mostrar_despedida(renderer)


def executar_noite(
    game: Game,
    renderer: Renderer,
    cliente_id: str
) -> ResultadoNoiteCompleto:
    """Executa uma noite com um cliente."""
    noite = Noite(game, renderer, cliente_id)

    if not noite.iniciar():
        # Fallback se cliente não carregar
        renderer.mostrar_erro(f"Erro ao carregar cliente: {cliente_id}")
        return ResultadoNoiteCompleto(
            resultado=ResultadoNoite.FALHA_CONFIANCA,
            cliente_nome=cliente_id,
        )

    return noite.executar()


def mostrar_transicao(renderer: Renderer, noite_atual: int):
    """Mostra transição entre noites."""
    renderer.transicao()

    textos = [
        "O sol nasce e se põe. Outra noite começa.",
        "As horas passam. O restaurante espera.",
        "Mais uma noite. Mais uma história.",
        "O neon de Shinjuku pulsa. A cortina balança.",
        "A madrugada chama. Alguém vem chegando.",
    ]

    texto = textos[min(noite_atual - 1, len(textos) - 1)]

    renderer.mostrar_narrativa(
        texto,
        titulo=f"Noite {noite_atual + 1}",
        digitar=True,
    )
    renderer.pausar()


def executar_reflexao(game: Game, renderer: Renderer):
    """Executa o Dia 7 - Reflexão completa."""
    reflexao = SistemaReflexao(renderer)

    reflexao.executar(
        memorias=game.memorias,
        tem_envelope=game.tem_envelope,
        tipo_final=game.determinar_final(),
    )


def mostrar_despedida(renderer: Renderer):
    """Mostra a despedida final."""
    renderer.transicao()
    renderer.console.print("\n")
    renderer.console.print("[titulo]Obrigado por jogar Midnight Kitchen.[/titulo]", justify="center")
    renderer.console.print("[sutil]深夜キッチン[/sutil]", justify="center")
    renderer.console.print("\n")


# ============================================================
# PONTO DE ENTRADA
# ============================================================

if __name__ == "__main__":
    try:
        executar_jogo()
    except KeyboardInterrupt:
        print("\n\nO restaurante fecha por hoje...")
        print("Volte quando quiser.\n")

#!/usr/bin/env python3
"""
Script de teste parametrizado para um cliente específico.
Uso: python test_cliente.py <cliente_id> <prato_correto_index>
"""

import pexpect
import sys
import time
import re
import json
from pathlib import Path

# Configurações
TIMEOUT = 15
PROJECT_DIR = Path(__file__).parent.parent

# Mapeamento de clientes para noites e pratos corretos
CLIENTES = {
    "yuki": {"noite": 1, "prato_index": 1, "prato_nome": "Tamago Gohan"},
    "tanaka": {"noite": 2, "prato_index": 2, "prato_nome": "Katsudon"},
    "ryo": {"noite": 3, "prato_index": 3, "prato_nome": "Curry Udon"},
    "midori": {"noite": 4, "prato_index": 5, "prato_nome": "Missoshiru"},
    "sachiko": {"noite": 5, "prato_index": 6, "prato_nome": "Nikujaga"},
    "hiroto": {"noite": 6, "prato_index": 7, "prato_nome": "Omurice"},
}


def strip_ansi(text):
    """Remove códigos ANSI."""
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)


def extrair_contexto(text):
    """Extrai contexto limpo."""
    if not text:
        return ""
    clean = strip_ansi(text)
    lines = [l.strip() for l in clean.split('\n') if l.strip()]
    return '\n'.join(lines[-15:])


def testar_cliente(cliente_id: str) -> dict:
    """
    Testa um cliente específico do jogo.

    Returns:
        Dicionário com resultados do teste
    """
    if cliente_id not in CLIENTES:
        return {"erro": f"Cliente '{cliente_id}' não encontrado"}

    config = CLIENTES[cliente_id]
    resultado = {
        "cliente": cliente_id,
        "noite": config["noite"],
        "prato_esperado": config["prato_nome"],
        "sucesso": False,
        "interacoes": 0,
        "bugs": [],
        "observacoes": [],
        "tempo_teste": 0,
    }

    inicio = time.time()

    # Limpa save anterior
    save_file = PROJECT_DIR / "saves" / "save.json"
    if save_file.exists():
        save_file.unlink()

    # Inicia o jogo
    import os
    env = os.environ.copy()
    env["COLUMNS"] = "100"
    env["LINES"] = "40"

    child = pexpect.spawn(
        'python3 main.py',
        encoding='utf-8',
        timeout=TIMEOUT,
        cwd=str(PROJECT_DIR),
        env=env
    )

    try:
        # Menu inicial
        child.expect("Escolha:", timeout=20)
        child.sendline("1")  # Novo Jogo

        # Tutorial
        child.expect("Escolha:", timeout=20)
        child.sendline("2")  # Pular tutorial

        # Introdução
        child.expect("ENTER", timeout=20)
        child.sendline("")

        # Pula noites até chegar na noite desejada
        noite_atual = 1
        while noite_atual <= config["noite"]:
            interacoes_noite = 0
            max_interacoes = 60
            noite_sucesso = False

            while interacoes_noite < max_interacoes:
                try:
                    index = child.expect([
                        "Escolha:",
                        "ENTER para continuar",
                        "Obrigado por jogar",
                        f"Noite {noite_atual + 1}",
                        "O sol nasce",
                        "As horas passam",
                        "Mais uma noite",
                        "O neon de Shinjuku",
                        "madrugada chama",
                        pexpect.TIMEOUT,
                        pexpect.EOF
                    ], timeout=TIMEOUT)

                    contexto = extrair_contexto(child.before)

                    if index == 0:  # Menu de escolha
                        interacoes_noite += 1
                        resultado["interacoes"] += 1
                        ctx_lower = contexto.lower()

                        # Lógica de escolha de prato
                        if noite_atual == config["noite"]:
                            # Estamos na noite do cliente alvo
                            if any(p in ctx_lower for p in ["tamago", "katsudon", "ochazuke", "missoshiru", "nikujaga", "omurice", "onigiri", "gyudon", "yakitori", "curry"]):
                                # Menu de pratos - escolhe o prato correto
                                child.sendline(str(config["prato_index"]))
                                resultado["observacoes"].append(f"Escolheu prato {config['prato_nome']} (opção {config['prato_index']})")
                            else:
                                child.sendline("1")
                        else:
                            # Noites anteriores - faz rapidamente
                            if any(p in ctx_lower for p in ["tamago", "katsudon", "ochazuke"]):
                                child.sendline("1")  # Qualquer prato
                            else:
                                child.sendline("1")

                    elif index == 1:  # ENTER
                        child.sendline("")

                    elif index == 2:  # Fim do jogo
                        break

                    elif index in [3, 4, 5, 6, 7, 8]:  # Transição de noite
                        noite_sucesso = True
                        if noite_atual == config["noite"]:
                            # Completou a noite do cliente alvo!
                            if "momento passou" in contexto.lower() or "vazias" in contexto.lower():
                                resultado["bugs"].append("Prato errado servido - cliente não satisfeito")
                            else:
                                resultado["sucesso"] = True
                                resultado["observacoes"].append("Cliente satisfeito!")
                        noite_atual += 1
                        child.sendline("")
                        break

                    elif index == 9:  # Timeout
                        child.sendline("")

                    elif index == 10:  # EOF
                        break

                except Exception as e:
                    resultado["bugs"].append(f"Erro: {str(e)}")
                    break

            if not noite_sucesso and noite_atual <= config["noite"]:
                resultado["bugs"].append(f"Noite {noite_atual} não completou normalmente")
                break

    except pexpect.TIMEOUT:
        resultado["bugs"].append("Timeout global")
    except Exception as e:
        resultado["bugs"].append(f"Erro fatal: {str(e)}")
    finally:
        child.close()

    resultado["tempo_teste"] = round(time.time() - inicio, 2)
    return resultado


def main():
    if len(sys.argv) < 2:
        print("Uso: python test_cliente.py <cliente_id>")
        print(f"Clientes disponíveis: {', '.join(CLIENTES.keys())}")
        sys.exit(1)

    cliente_id = sys.argv[1].lower()
    print(f"\n{'='*50}")
    print(f"TESTE: {cliente_id.upper()}")
    print(f"{'='*50}\n")

    resultado = testar_cliente(cliente_id)

    # Output em JSON para fácil parsing
    print("\n" + "="*50)
    print("RESULTADO:")
    print("="*50)
    print(json.dumps(resultado, indent=2, ensure_ascii=False))

    return 0 if resultado["sucesso"] else 1


if __name__ == "__main__":
    sys.exit(main())

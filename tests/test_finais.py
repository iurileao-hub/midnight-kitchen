#!/usr/bin/env python3
"""
Script de teste para os diferentes finais do jogo.

Finais:
- perfeito: 0 falhas, 6 memorias, envelope
- bom: max 1 falha, envelope
- neutro: max 2 falhas
- ruim: 3+ falhas
"""

import pexpect
import sys
import time
import re
import json
from pathlib import Path

TIMEOUT = 15
PROJECT_DIR = Path(__file__).parent.parent

# Clientes em ordem e seus pratos corretos
CLIENTES_ORDEM = ["yuki", "tanaka", "ryo", "midori", "sachiko", "hiroto"]
PRATOS_CORRETOS = {
    "yuki": 1,      # Tamago Gohan
    "tanaka": 2,    # Katsudon
    "ryo": 3,       # Curry Udon (ou 4 para Ochazuke)
    "midori": 5,    # Missoshiru (era 4, que e Ochazuke!)
    "sachiko": 6,   # Nikujaga
    "hiroto": 7,    # Omurice
}

# Configuracao de cada final
FINAIS_CONFIG = {
    "perfeito": {
        "descricao": "0 falhas - todos os pratos corretos",
        "falhar_clientes": [],
    },
    "bom": {
        "descricao": "1 falha - falha em Tanaka",
        "falhar_clientes": ["tanaka"],
    },
    "neutro": {
        "descricao": "2 falhas - falha em Tanaka e Ryo",
        "falhar_clientes": ["tanaka", "ryo"],
    },
    "ruim": {
        "descricao": "3+ falhas - falha em Tanaka, Ryo e Midori",
        "falhar_clientes": ["tanaka", "ryo", "midori"],
    },
}


def strip_ansi(text):
    """Remove codigos ANSI."""
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)


def extrair_contexto(text):
    """Extrai contexto limpo."""
    if not text:
        return ""
    clean = strip_ansi(text)
    lines = [l.strip() for l in clean.split('\n') if l.strip()]
    return '\n'.join(lines[-20:])


def testar_final(tipo_final: str) -> dict:
    """
    Testa um tipo de final especifico.

    Usa abordagem simplificada: detecta cliente pelo nome no dialogo
    e escolhe o prato correto ou errado conforme configuracao.
    """
    if tipo_final not in FINAIS_CONFIG:
        return {"erro": f"Final '{tipo_final}' nao reconhecido"}

    config = FINAIS_CONFIG[tipo_final]
    falhar_clientes = set(config["falhar_clientes"])

    resultado = {
        "tipo_final": tipo_final,
        "descricao": config["descricao"],
        "final_obtido": None,
        "sucesso": False,
        "clientes_atendidos": [],
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
    env["COLUMNS"] = "120"
    env["LINES"] = "50"

    child = pexpect.spawn(
        'python3 main.py',
        encoding='utf-8',
        timeout=TIMEOUT,
        cwd=str(PROJECT_DIR),
        env=env
    )

    # Rastreia cliente atual baseado em padroes do dialogo
    cliente_atual = None
    cliente_idx = 0
    prato_servido_nesta_noite = False

    try:
        # Menu inicial
        child.expect("Escolha:", timeout=30)
        child.sendline("1")  # Novo Jogo

        # Tutorial
        child.expect("Escolha:", timeout=20)
        child.sendline("2")  # Pular tutorial

        # Introducao
        child.expect("ENTER", timeout=20)
        child.sendline("")

        # Loop principal - processa ate encontrar o final
        max_interacoes = 500
        interacoes = 0

        while interacoes < max_interacoes:
            interacoes += 1

            try:
                index = child.expect([
                    "Escolha:",                    # 0 - Menu de opcoes
                    "ENTER para continuar",       # 1 - Pausas
                    "ENTER",                      # 2 - Outras pausas
                    "FINAL: REDEN",               # 3 - Final perfeito
                    "FINAL: AMANHECER",           # 4 - Final bom
                    "FINAL: PERGUNTAS",           # 5 - Final neutro
                    "FINAL: CINZAS",              # 6 - Final ruim
                    "Obrigado por jogar",         # 7 - Creditos
                    pexpect.TIMEOUT,              # 8 - Timeout
                    pexpect.EOF                   # 9 - Fim
                ], timeout=TIMEOUT)

                contexto = extrair_contexto(child.before)
                ctx_lower = contexto.lower()

                # Detecta qual cliente esta presente pelo nome
                for nome in CLIENTES_ORDEM:
                    if nome in ctx_lower or nome.capitalize() in contexto:
                        if cliente_atual != nome:
                            cliente_atual = nome
                            prato_servido_nesta_noite = False

                if index == 0:  # Menu de escolha
                    # Detecta menu de pratos
                    is_menu_prato = any(p in ctx_lower for p in [
                        "tamago", "katsudon", "ochazuke", "missoshiru",
                        "nikujaga", "omurice", "onigiri", "gyudon", "yakitori", "curry"
                    ])

                    if is_menu_prato and cliente_atual and not prato_servido_nesta_noite:
                        # Decide prato
                        deve_falhar = cliente_atual in falhar_clientes
                        prato = 1 if deve_falhar else PRATOS_CORRETOS.get(cliente_atual, 1)
                        status = "ERRADO" if deve_falhar else "CERTO"

                        child.sendline(str(prato))
                        prato_servido_nesta_noite = True
                        resultado["clientes_atendidos"].append(f"{cliente_atual}: {status}")
                        resultado["observacoes"].append(f"{cliente_atual.capitalize()}: prato {prato} [{status}]")
                    else:
                        child.sendline("1")

                elif index in [1, 2]:  # ENTER
                    # Detecta transicao de noite
                    if any(t in ctx_lower for t in ["sol nasce", "horas passam", "outra noite", "madrugada"]):
                        cliente_idx += 1
                        if cliente_idx < len(CLIENTES_ORDEM):
                            cliente_atual = CLIENTES_ORDEM[cliente_idx]
                            prato_servido_nesta_noite = False
                    child.sendline("")

                elif index == 3:  # Final perfeito
                    resultado["final_obtido"] = "perfeito"
                    resultado["observacoes"].append("Final: REDENCAO (perfeito)")
                    child.sendline("")

                elif index == 4:  # Final bom
                    resultado["final_obtido"] = "bom"
                    resultado["observacoes"].append("Final: AMANHECER (bom)")
                    child.sendline("")

                elif index == 5:  # Final neutro
                    resultado["final_obtido"] = "neutro"
                    resultado["observacoes"].append("Final: PERGUNTAS SEM RESPOSTA (neutro)")
                    child.sendline("")

                elif index == 6:  # Final ruim
                    resultado["final_obtido"] = "ruim"
                    resultado["observacoes"].append("Final: CINZAS (ruim)")
                    child.sendline("")

                elif index == 7:  # Creditos
                    resultado["observacoes"].append("Creditos finais")
                    break

                elif index == 8:  # Timeout
                    child.sendline("")

                elif index == 9:  # EOF
                    break

                # Se ja encontrou o final, continua ate os creditos
                if resultado["final_obtido"] and index not in [7, 9]:
                    continue

            except Exception as e:
                resultado["bugs"].append(f"Erro: {str(e)}")
                break

        # Verifica sucesso
        if resultado["final_obtido"] == tipo_final:
            resultado["sucesso"] = True
        elif resultado["final_obtido"] is not None:
            resultado["observacoes"].append(
                f"DIVERGENCIA: esperado {tipo_final}, obtido {resultado['final_obtido']}"
            )

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
        print("Uso: python test_finais.py <tipo_final>")
        print("Tipos disponiveis: perfeito, bom, neutro, ruim")
        sys.exit(1)

    tipo_final = sys.argv[1].lower()
    print(f"\n{'='*60}")
    print(f"TESTE FINAL: {tipo_final.upper()}")
    print(f"{'='*60}\n")

    resultado = testar_final(tipo_final)

    print("\n" + "="*60)
    print("RESULTADO:")
    print("="*60)
    print(json.dumps(resultado, indent=2, ensure_ascii=False))

    return 0 if resultado["sucesso"] else 1


if __name__ == "__main__":
    sys.exit(main())

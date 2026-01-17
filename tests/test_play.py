#!/usr/bin/env python3
"""
Script de teste automatizado para Midnight Kitchen.
Joga a primeira noite (Yuki) para validar o fluxo do jogo.
"""

import pexpect
import sys
import time
import re

# Configurações
TIMEOUT = 20
LOG_FILE = "test_play_log.txt"

def log(msg):
    """Log com timestamp."""
    timestamp = time.strftime("%H:%M:%S")
    print(f"[{timestamp}] {msg}")

def strip_ansi(text):
    """Remove códigos ANSI do texto."""
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

def extrair_contexto(text, chars=300):
    """Extrai contexto limpo do texto."""
    if not text:
        return ""
    clean = strip_ansi(text)
    # Remove linhas vazias extras
    lines = [l.strip() for l in clean.split('\n') if l.strip()]
    return '\n'.join(lines[-10:])  # Últimas 10 linhas

def jogar_primeira_noite():
    """Executa a primeira noite do jogo automaticamente."""

    log("Iniciando Midnight Kitchen...")

    # Spawn do processo - herda ambiente mas adiciona configurações
    import os
    env = os.environ.copy()
    env["COLUMNS"] = "100"
    env["LINES"] = "40"

    child = pexpect.spawn(
        'python3 main.py',
        encoding='utf-8',
        timeout=TIMEOUT,
        cwd='/Users/iurileao/Documents/Projects/midnight-kitchen',
        env=env
    )

    # Log para arquivo
    logfile = open(LOG_FILE, 'w')
    child.logfile_read = logfile

    try:
        # === MENU INICIAL ===
        log("Aguardando menu inicial...")
        child.expect("Escolha:", timeout=20)
        log("Menu detectado. Escolhendo 'Novo Jogo' (1)...")
        child.sendline("1")

        # === TUTORIAL ===
        log("Aguardando pergunta do tutorial...")
        child.expect("Escolha:", timeout=20)
        contexto = extrair_contexto(child.before)
        log(f"Tutorial:\n{contexto}")
        log("Pulando tutorial (2)...")
        child.sendline("2")

        # === INTRODUÇÃO CURTA ===
        log("Aguardando introdução...")
        child.expect("ENTER", timeout=20)
        contexto = extrair_contexto(child.before)
        log(f"Introdução:\n{contexto}")
        log("Continuando...")
        child.sendline("")

        # === NOITE 1 - YUKI ===
        log("\n" + "="*50)
        log("=== NOITE 1: YUKI ===")
        log("="*50 + "\n")

        # Loop de interação
        interacoes = 0
        max_interacoes = 50  # Limite de segurança

        while interacoes < max_interacoes:
            try:
                # Espera por prompt de escolha ou ENTER
                index = child.expect([
                    "Escolha:",
                    "ENTER para continuar",
                    "Obrigado por jogar",
                    "Noite 2",
                    pexpect.TIMEOUT,
                    pexpect.EOF
                ], timeout=20)

                contexto = extrair_contexto(child.before)

                if index == 0:
                    # Menu de escolha
                    interacoes += 1
                    log(f"\n[Interação {interacoes}]")
                    log(f"Contexto:\n{contexto[-400:]}")

                    # Analisa o contexto para fazer escolhas inteligentes
                    ctx_lower = contexto.lower()

                    # Detecta menu de pratos
                    if "tamago" in ctx_lower or "katsudon" in ctx_lower or "cardápio" in ctx_lower:
                        log("  → Menu de pratos detectado. Escolhendo Tamago Gohan (1)...")
                        child.sendline("1")
                    # Detecta opção de cozinha vs conversa
                    elif "preparar" in ctx_lower and "conversar" in ctx_lower:
                        log("  → Opção cozinha/conversa. Escolhendo conversar (1)...")
                        child.sendline("1")
                    else:
                        log("  → Escolhendo opção 1...")
                        child.sendline("1")

                elif index == 1:
                    # Prompt de ENTER
                    if contexto:
                        log(f"\nNarrativa:\n{contexto[-300:]}")
                    log("Continuando...")
                    child.sendline("")

                elif index == 2:
                    # Fim do jogo
                    log("\n=== JOGO FINALIZADO ===")
                    break

                elif index == 3:
                    # Chegou na noite 2 - sucesso!
                    log("\n" + "="*50)
                    log("=== NOITE 1 COMPLETADA COM SUCESSO! ===")
                    log("="*50)
                    log(f"Contexto final:\n{contexto}")
                    break

                elif index == 4:
                    # Timeout
                    log("Timeout - tentando continuar...")
                    child.sendline("")

                elif index == 5:
                    # EOF
                    log("Processo encerrado.")
                    break

            except Exception as e:
                log(f"Erro durante interação: {e}")
                break

        # Captura output final
        log("\n=== OUTPUT FINAL ===")
        try:
            child.expect(pexpect.EOF, timeout=5)
        except:
            pass

        if child.before:
            log(extrair_contexto(child.before))

    except pexpect.TIMEOUT:
        log("TIMEOUT - O jogo não respondeu a tempo")
        if child.before:
            log(f"Último output:\n{extrair_contexto(child.before)}")

    except Exception as e:
        log(f"ERRO: {e}")
        import traceback
        traceback.print_exc()

    finally:
        child.close()
        logfile.close()
        log(f"\nLog completo salvo em: {LOG_FILE}")

if __name__ == "__main__":
    jogar_primeira_noite()

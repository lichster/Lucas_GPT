"""
Agente GPT Pessoal - Main CLI
--------------------------------
Este arquivo serve como ponto de entrada para executar o agente via linha de comando.
Estruturado para:
- Receber input do usuário.
- Processar via prompts especializados.
- Retornar outputs estruturados.
- Facilitar integração futura com APIs reais (OpenAI, LangChain, etc).
"""

import sys
import logging
from pathlib import Path

# ======================================
# CONFIGURAÇÃO DE LOGGING
# ======================================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger("AgenteGPT")

# ======================================
# PROMPTS SIMULADOS (em produção, importar de /src/prompts/)
# ======================================
PROMPTS = {
    "system": "Você é um colega digital proativo. Questione, organize, proponha e execute. Evite respostas genéricas.",
    "organizacao": "Transforme as informações abaixo em uma lista estruturada de tarefas.",
    "decisao": "Analise os cenários apresentados. Liste prós, contras e riscos de cada opção.",
    "pessoal": "Crie uma reflexão crítica baseada na situação abaixo. Faça provocações para crescimento pessoal."
}

# ======================================
# ENGINE MOCK (em produção -> integração com API GPT)
# ======================================
def process_input(user_input: str, mode: str = "organizacao") -> str:
    """
    Simula o processamento de um input do usuário.
    Em produção, este método chamaria a API GPT com o prompt adequado.
    """
    logger.debug(f"Processando input no modo '{mode}'")

    if mode not in PROMPTS:
        logger.warning(f"Modo '{mode}' não encontrado. Usando 'system' como fallback.")
        mode = "system"

    prompt = PROMPTS[mode]

    # Saída simulada (em integração real, viria da API)
    simulated_output = f"[PROMPT SELECIONADO: {mode}]\nUsuário disse: {user_input}\nResposta simulada baseada no prompt: {prompt}"
    return simulated_output


# ======================================
# CLI LOOP
# ======================================
def cli_loop():
    """
    Loop interativo de CLI.
    """
    logger.info("🚀 Agente GPT Pessoal iniciado (modo CLI). Digite 'exit' para sair.")
    logger.info("Modos disponíveis: organizacao, decisao, pessoal")

    while True:
        try:
            user_input = input("\nVocê: ").strip()
            if user_input.lower() in ["exit", "quit", "sair"]:
                logger.info("Encerrando agente. Até logo!")
                break

            mode = "organizacao"  # default
            if user_input.startswith("/"):
                parts = user_input.split(maxsplit=1)
                cmd = parts[0][1:]
                if cmd in PROMPTS:
                    mode = cmd
                    user_input = parts[1] if len(parts) > 1 else ""

            response = process_input(user_input, mode=mode)
            print(f"\n🤖 AgenteGPT:\n{response}")

        except KeyboardInterrupt:
            logger.info("Encerrando agente (Ctrl+C).")
            break
        except Exception as e:
            logger.error(f"Erro inesperado: {e}", exc_info=True)


# ======================================
# ENTRYPOINT
# ======================================
if __name__ == "__main__":
    cli_loop()

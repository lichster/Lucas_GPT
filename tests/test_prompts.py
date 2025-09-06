"""
Testes automatizados para validação dos prompts do Agente GPT Pessoal.

Objetivos:
- Garantir consistência estrutural dos prompts.
- Validar padrões de escrita (clareza, objetividade, ausência de jargões).
- Verificar que cada prompt cumpre seu papel sem ambiguidade.
- Criar base para integração futura com chamadas reais à API GPT.
"""

import re
import pytest

# ===============================================================
# MOCK DE PROMPTS – em produção, estes seriam importados de /src/prompts/
# ===============================================================
PROMPTS = {
    "system": "Você é um colega digital proativo. Questione, organize, proponha e execute. Evite respostas genéricas.",
    "organizacao": "Transforme as informações abaixo em uma lista estruturada de tarefas. Use ordem lógica e explique rapidamente cada item.",
    "decisao": "Analise os cenários apresentados. Liste prós, contras e riscos de cada opção. Sugira uma recomendação final com justificativa.",
    "pessoal": "Crie uma reflexão crítica baseada na situação abaixo. Faça provocações que incentivem crescimento pessoal e profissional."
}


# ===============================================================
# TESTES DE ESTRUTURA
# ===============================================================

def test_prompts_existem():
    """Todos os prompts essenciais devem estar definidos."""
    required = ["system", "organizacao", "decisao", "pessoal"]
    for key in required:
        assert key in PROMPTS, f"Prompt {key} não está definido."


def test_prompts_nao_vazios():
    """Nenhum prompt pode ser vazio."""
    for name, text in PROMPTS.items():
        assert text.strip() != "", f"Prompt {name} está vazio."


def test_prompts_terminam_com_ponto():
    """Por consistência, todos os prompts devem terminar com ponto final."""
    for name, text in PROMPTS.items():
        assert text.strip()[-1] in [".", "?"], f"Prompt {name} deve terminar com ponto final."


# ===============================================================
# TESTES DE QUALIDADE TEXTUAL
# ===============================================================

def test_prompts_nao_usam_ingles():
    """Prompts devem estar em português, não em inglês."""
    forbidden_words = ["task", "decision", "personal", "system", "analyze"]
    for name, text in PROMPTS.items():
        for word in forbidden_words:
            assert word.lower() not in text.lower(), f"Prompt {name} contém palavra em inglês proibida: {word}"


def test_prompts_contem_verbo_de_acao():
    """Cada prompt deve conter ao menos um verbo de ação claro (ex: organize, analise, crie)."""
    action_verbs = ["organize", "analise", "crie", "transforme", "liste", "sugira", "faça"]
    for name, text in PROMPTS.items():
        assert any(v in text.lower() for v in action_verbs), f"Prompt {name} não contém verbo de ação."


# ===============================================================
# TESTES FUTUROS (PLACEHOLDER)
# ===============================================================

@pytest.mark.skip(reason="Integração futura com API GPT.")
def test_resposta_modelo():
    """
    Teste placeholder para integração futura.
    Aqui será feita chamada real à API GPT para verificar se
    a saída respeita as instruções do prompt.
    """
    pass

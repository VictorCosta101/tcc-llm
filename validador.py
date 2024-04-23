def validador(llm_response, repostas):
    
    acertos = 0
    for chave, valor_resposta in repostas.items():
        valor_fornecido = llm_response.get(chave)
        if valor_fornecido == valor_resposta:
            acertos += 1
    
    return acertos        
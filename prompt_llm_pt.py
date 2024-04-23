def generate_llm_prompt(extracted_text):
    q = f'''
            Responda em português.
            Você é um agente de processamento de texto trabalhando com um documento de contrato de locação.
            Extraia valores especificados do texto tokenizado de origem.
            Retorne a resposta como um objeto JSON com os seguintes campos:
            - "Categoria_da_sesmaria" <string>
            - "Sesmeiros" <string>
            - "Capitania" <string>
            - "Estado_atual" <string>
            - "Historico_da_terra <string>
            - "Data_de_peticao" <string>
            - "Localidade" <string>
            - "Marcos_geograficos" <string>
            - "Ribeira" <string>
            - "Confrotantes" <string>
            - "Area" <float>
            - "Tipo_de_area" <string>
            - "Largura" <string>
            - "Comprimento" <string>

            Instrução:
            Não infira nenhum dado com base no treinamento anterior, use estritamente apenas o texto de origem fornecido abaixo como entrada.
            Responda todos os campos, se você não encontrar a informação no texto, retorne o campo com "NA"
            Classifique "Categoria_da_sesmaria" selecionando uma das seguintes opções ["individual"], ["coletiva"]
            Classifique "Capitania" selecionando uma das seguintes opções ["Alagoas"], ["Bahia"], ["Ceará"], ["Colonia do Sacramento"], ["Espírito Santo"], ["Goias"], ["Itamaracá"], ["Maranhão"], ["Mato Grosso do Sul"], ["Minas Gerais"], ["NA"], ["Pará"], ["Paraíba"], ["Pernambuco"], ["Pernambuco/Alagoas"], ["Pernambuco/Piauí"], ["Piauí"], ["Rio de Janeiro"], ["Rio Grande do Norte"], ["Rio Grande do Sul"], ["Rio Negro"], ["Santa Catarina"], ["São Paulo"], ["São Paulo/Rio de Janeiro"], ["Sergipe"]
            Classifique "Estado_atual" selecionando uma das seguintes opções ["Alagoas"], ["Bahia"], ["Ceará"], ["Colonia do Sacramento"], ["Espírito Santo"], ["Goias"], ["Itamaracá"], ["Maranhão"], ["Mato Grosso do Sul"], ["Minas Gerais"], ["NA"], ["Pará"], ["Paraíba"], ["Pernambuco"], ["Pernambuco/Alagoas"], ["Pernambuco/Piauí"], ["Piauí"], ["Rio de Janeiro"], ["Rio Grande do Norte"], ["Rio Grande do Sul"], ["Rio Negro"], ["Santa Catarina"], ["São Paulo"], ["São Paulo/Rio de Janeiro"] , ["Sergipe"]
            Classifique "Historico_da_terra" selecionando uma das seguintes opções ["Comprada"], ["Devoluta nunca povoada"], ["Devoluta por abandono"], ["Herdada"], ["NA"], ["Primordial"]
            Classifique "Tipo_de_area" selecionando uma das seguintes opções ["Léguas"], ["Braças"]. ["NA"]
            ========

            source text: "{extracted_text}"
            ========
    '''
        
    
    return q
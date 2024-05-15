def generate_llm_prompt(extracted_text):
    q = f'''
        source text: "{extracted_text}"
        role: you're a historian 
        Answer in portuguese.
        You are a text processing agent working with lease agreement document.
        Extract specified values from the source tokenized text.
        
        Return answer as JSON object with following fields:
        - "Categoria_da_sesmaria" <string>
        - "Sesmeiros" <string>
        - "Capitania" <string>
        - "Estado_atual" <string>
        - "Historico_da_terra" <string>
        - "Data_de_peticao" <string>
        - "Localidade" <string>
        - "Marcos_geograficos" <string>
        - "Ribeira" <string>
        - "Confrotantes" <string>
        - "Area" <float>
        - "Tipo_de_area" <string>
        - "Largura" <string>
        - "Comprimento" <string>

        Instruction:
        Do not infer any data based on previous training, strictly use only source text given as input.
        Answer All fields, if you don't find the information on text return filed with "NA"
        Classify "Categoria_da_sesmaria" by selecting one of the following options ["individual"], ["coletiva"]
        Classify "Capitania" by selecting one of the following options ["Alagoas"], ["Bahia"], ["Ceará"], ["Colonia do Sacramento"], ["Espírito Santo"], ["Goias"], ["Itamaracá"], ["Maranhão"], ["Mato Grosso do Sul"], ["Minas Gerais"], ["NA"], ["Pará"], ["Paraíba"], ["Pernambuco"], ["Pernambuco/Alagoas"], ["Pernambuco/Piauí"], ["Piauí"], ["Rio de Janeiro"], ["Rio Grande do Norte"], ["Rio Grande do Sul"], ["Rio Negro"], ["Santa Catarina"], ["São Paulo"], ["São Paulo/Rio de Janeiro"], ["Sergipe"]
        Classify "Estado_atual" by selecting one of the following options ["Alagoas"], ["Bahia"], ["Ceará"], ["Colonia do Sacramento"], ["Espírito Santo"], ["Goias"], ["Itamaracá"], ["Maranhão"], ["Mato Grosso do Sul"], ["Minas Gerais"], ["NA"], ["Pará"], ["Paraíba"], ["Pernambuco"], ["Pernambuco/Alagoas"], ["Pernambuco/Piauí"], ["Piauí"], ["Rio de Janeiro"], ["Rio Grande do Norte"], ["Rio Grande do Sul"], ["Rio Negro"], ["Santa Catarina"], ["São Paulo"], ["São Paulo/Rio de Janeiro"] , ["Sergipe"]
        Classify "Historico_da_terra" by selecting one of the following options ["Comprada"], ["Devoluta nunca povoada"], ["Devoluta por abandono"], ["Herdada"], ["NA"], ["Primordial"]
        Classify "Tipo_de_area" by selecting one of the following options ["Léguas"], ["Braças"]. ["NA"]
        
        '''
    
    return q
def generate_llm_prompt(extracted_text):
    q = f'''
You are a text processing agent working with lease agreement document.

Extract specified values from the source tokenized text.
Answer in portuguese.
Return answer as JSON object with following fields:
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
- "Largura" <float>
- "Comprimeinto" <float>

Instruções:
Do not infer any data based on previous training, strictly use only source text given below as input.
Answer All fields, if you don't find the information on text return filed with 'Null'
Classifique a "Categoria_da_sesmaria" como "petição individual" ou "petição coletiva" com base na informação extraída do texto.
Classifique a "Capitania" como "Alagoas", "Bahia", "Ceará", "Colonia do Sacramento", "Espírito Santo", "Goias", "Itamaracá", "Maranhão", "Mato Grosso do Sul", "Minas Gerais", "NA", "Pará", "Paraíba", "Pernambuco", "Pernambuco/Alagoas", "Pernambuco/Piauí", "Piauí", "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul", "Rio Negro", "Santa Catarina", "São Paulo", "São Paulo/Rio de Janeiro" ou "Sergipe"  com base na informação extraída do texto.
Classifique a "Estado_atual" como "Alagoas", "Bahia", "Ceará", "Colonia do Sacramento", "Espírito Santo", "Goias", "Itamaracá", "Maranhão", "Mato Grosso do Sul", "Minas Gerais", "NA", "Pará", "Paraíba", "Pernambuco", "Pernambuco/Alagoas", "Pernambuco/Piauí", "Piauí", "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul", "Rio Negro", "Santa Catarina", "São Paulo", "São Paulo/Rio de Janeiro" ou "Sergipe"  com base na informação extraída do texto.
Classifique a "Historico_da_terra" como "Comprada", "Devoluta nunca povoada", "Devoluta por abandono", "Herdada", "NA" ou "Primordial" com base na informação extraída do texto.
Classifique a "Tipo_de_area" como "Léguas", "Braças" ou "NA" com base na informação extraída do texto.
========
{extracted_text}
========
'''
    
    return q
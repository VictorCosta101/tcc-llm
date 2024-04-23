from llm import iniciar_llm
import json
from validador import validador

pdf_path = "/home/victor/Documentos/tcc/peal0002.pdf"

#resposta = iniciar_llm("/home/victor/Documentos/tcc/PE-AL0013.pdf")


gabarito_json = json.loads('''{
"Categoria_da_sesmaria": "individual",
"Sesmeiros": "Christovão de Mendonça",
"Capitania": "Pernambuco",
"Estado_atual": "Alagoas",
"Historico_da_terra": "Comprada",
"Data_de_peticao": "21/02/1702",
"Localidade": "Palmares",
"Marcos_geograficos": "Rio Jacuípe, Rio Quaraguassú, riacho João Mulato",
"Ribeira": "NA",
"Confrotantes": "NA",
"Area": 16,
"Tipo_de_area": "Léguas",
"Largura": 4,
"Comprimento": 4
}''')


temperatura = 0.5
delta = 0.05
acertos_anterior = 0

while True:
    print(f'''Taxa de acerto anterior : {acertos_anterior} || temperatura : {temperatura}''')
    resposta = iniciar_llm(pdf_path, temperatura)
    resposta_json = json.loads(resposta)
    acertos = validador(resposta_json, gabarito_json)
    print(f"Taxa de acerto: {acertos}")
    if acertos == 14:
        break
    if acertos > acertos_anterior: 
        temperatura += delta
        acertos_anterior = acertos
    else:
        break

print(f'''O melhor resultado com acertos {acertos_anterior} e temperatura {temperatura}''')

from llm import iniciar_llm
import json
from validador import validador
from gabaritos import gabarito_peal0002_json, gabarito_peal00013_json

documentos = [["/home/victor/Documentos/tcc/documentos/peal0002.pdf", gabarito_peal0002_json ], 
               ["/home/victor/Documentos/tcc/documentos/peal0013.pdf", gabarito_peal00013_json ]]

temperatura = 0.0
delta = 0.05
acertos_anterior = 0
contador = 0 
while True:
    print(f'''Taxa de acerto anterior : {acertos_anterior} || temperatura : {temperatura}''')

    print( f'''Teste {documentos[contador][1]['Categoria_da_sesmaria']}''')
    
    resposta = iniciar_llm(documentos[contador][0], temperatura)
    resposta_json = json.loads(resposta)
    acertos = validador(resposta_json, documentos[contador][1])
    print(f"Taxa de acerto: {acertos}")
    if acertos == 14:
        break
    if acertos > acertos_anterior: 
        temperatura += delta
        acertos_anterior = acertos
    else:
        contador +=1
        if contador == len(documentos):
            break
        print(f'''Indo para novo documento {documentos[contador][0]}''')
        

print(f'''O melhor resultado com acertos {acertos_anterior} e temperatura {temperatura}''')

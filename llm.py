from ollama import Client
import pdfplumber
from transformers import AutoTokenizer
from prompt_llm import generate_llm_prompt
import spacy
import time



# Carregar modelo de linguagem Spacy em português
try:
    nlp = spacy.load("pt_core_news_sm")
except OSError:
    print("Modelo não encontrado. Baixando...")
    spacy.cli.download("pt_core_news_sm")
    nlp = spacy.load("pt_core_news_sm")


# Lê o arquivo pdf 
def extract_text_with_whitespace(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as file:
        for page in file.pages:
            text += page.extract_text()
    return text

# Gera tokens para o texto do arquivo pdf lido
def tokenize_text(text):
    doc = nlp(text)
    tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
    return ' '.join(tokens)

def iniciar_llm(pdf_path, temp):
    print("Incidado o processo de leitura do pdf")
    inicio_leitura_pdf = time.time()
    extracted_text = extract_text_with_whitespace(pdf_path)
    print(f"O tamanho do documento é: { len(extracted_text) }")
    fim_leitura_pdf = time.time()
    print(f"Tempo de execução ollama: {fim_leitura_pdf - inicio_leitura_pdf} segundos")
    
    print("Incidado o processo de geração de tokens do pdf")
    inicio_token_pdf = time.time()
    tokenized_text = tokenize_text(extracted_text)
    fim_token_pdf = time.time()
    print(f"Tempo de execução ollama: {fim_token_pdf - inicio_token_pdf} segundos")

    
    print("Incidado o procesamento do pdf pela llm")
    # Create prompt
    q = generate_llm_prompt(tokenized_text)
    #print("prompt: "+ q)
    inicio = time.time()
    client = Client(host='https://d388-34-91-50-237.ngrok-free.app')
    response = client.generate(
        model='llama3', format='json', prompt=q, stream=False, options={'temperature': temp})
    fim = time.time()
    tempo = fim - inicio
    print(response['response'])
    print(f"Tempo de execução ollama: {tempo} segundos || minutos : {tempo / 60} ")
    return response['response']


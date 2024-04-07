from ollama import Client
import pdfplumber
from transformers import AutoTokenizer
from prompt_llm import generate_llm_prompt
import spacy
import time

pdf_path = "/home/victor/Documentos/tcc/peal0002.pdf"

# Carregar modelo de linguagem Spacy em português
nlp = spacy.load("pt_core_news_sm")



def extract_text_with_whitespace(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as file:
        for page in file.pages:
            text += page.extract_text()
    return text

def tokenize_text(text):
    doc = nlp(text)
    tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
    return ' '.join(tokens)


print("Incidado o processo de leitura do pdf")
inicio_leitura_pdf = time.time()
extracted_text = extract_text_with_whitespace(pdf_path)
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

inicio = time.time()

client = Client(host='http://localhost:11434')

response = client.generate(
    model='llama2', format='json', prompt=q
)

fim = time.time()

print(f"Tempo de execução ollama: {fim - inicio} segundos")

print(response['response'])

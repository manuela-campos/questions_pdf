import sys # Importa e utiliza ferramentas do sistema operacional
import os

# Direcionamento de caminhos e acesso a deretórios do projeto

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import streamlit as st 
from src.extract import extract_text_from_pdf
from src.gemini_api import ask_gemini

# Configuração da página
st.set_page_config(
    page_title="Chat do Gemini",  # Título da aba do navegador
    page_icon="🤖",                # Ícone que aparece na aba do navegador
    layout="wide",                 # Layout da página: "centered" ou "wide"
    initial_sidebar_state="expanded"  # Estado inicial da barra lateral: "expanded" ou "collapsed"
)

# Estilos CSS personalizados
st.markdown(
    """
    <style>
    .header {
        text-align: center;
        color: #4CAF50;  /* Cor do texto do cabeçalho */
        font-size: 2.5em; /* Tamanho da fonte do cabeçalho */
        margin-bottom: 20px; /* Espaçamento abaixo do cabeçalho */
    }
    .subheader {
        text-align: center;
        color: #555; /* Cor do texto do subtítulo */
        font-size: 1.5em; /* Tamanho da fonte do subtítulo */
        margin-bottom: 40px; /* Espaçamento abaixo do subtítulo */
    }
    .chat-container {
        background-color: #f0f0f0; /* Cor de fundo do chat */
        border-radius: 10px; /* Bordas arredondadas */
        padding: 20px; /* Espaçamento interno */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Sombra */
        margin: 20px; /* Margem ao redor do contêiner */
    }
    .question {
        color: #007BFF; /* Cor da pergunta */
        font-weight: bold; /* Negrito */
    }
    .response {
        color: #333; /* Cor da resposta */
        font-style: italic; /* Itálico */
    }
    .button {
        background-color: #4CAF50; /* Cor de fundo do botão */
        color: white; /* Cor do texto do botão */
        border: none; /* Sem borda */
        border-radius: 5px; /* Bordas arredondadas */
        padding: 10px 20px; /* Espaçamento interno do botão */
        cursor: pointer; /* Cursor de ponteiro ao passar o mouse */
    }
    .button:hover {
        background-color: #45a049; /* Cor do botão ao passar o mouse */
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Título da aplicação
st.markdown('<h1 class="header">Chat do Gemini</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subheader">Faça perguntas e obtenha respostas!</h2>', unsafe_allow_html=True)


st.markdown(
    """
    <style>
    .chat-container {
        background-color: #f0f0f0; /* Cor de fundo do chat */
        border-radius: 10px; /* Bordas arredondadas */
        padding: 20px; /* Espaçamento interno */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Sombra */
    }
    .question {
        color: #007BFF; /* Cor da pergunta */
        font-weight: bold; /* Negrito */
    }
    .response {
        color: #333; /* Cor da resposta */
        font-style: italic; /* Itálico */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Upload do arquivo PDF
uploaded_file = st.file_uploader("Faça upload do PDF", type = {"pdf"})

# Se um arquivo for carregado, extrai o texto e armazena na sessão
if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)
    st.session_state["context"] = text

# Campo de entrada para a pergunta do usuário
question = st.text_input("Digite uma pergunta")

# Se houver uma pergunta e com um contexto carregado, chama a API do Gemini
if question and "context" in st.session_state:
    response = ask_gemini(question, st.session_state["context"])   # Exibe a pergunta e a resposta com estilos personalizados
    st.markdown(
        f'<div class="chat-container">'
        f'<p class="question">Pergunta: {question}</p>'
        f'<p class="response">Resposta: {response}</p>'
        f'</div>',
        unsafe_allow_html=True
    )

# Exemplo de botão estilizado
if st.button("Enviar", key="send_button"):
    st.success("Pergunta enviada!")  # Mensagem de sucesso ao clicar no botão
    
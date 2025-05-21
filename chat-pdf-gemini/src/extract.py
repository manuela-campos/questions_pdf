from pypdf import PdfReader
def extract_text_from_pdf(pdf_file):
    """
    Função para extrair o texto de um PDF carregando Streamlit

    Parâmetros:
    pdf_file(UploadedFile)

    retorno:
    src: texto extraído do PDF

    """
    reader = PdfReader(pdf_file) #Cria um objeto para ler o PDF

    # Percorre todas as páginas e extrair informações
    text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

    return text # retorna o texto extraído

    
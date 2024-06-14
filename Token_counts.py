from langchain_community.document_loaders import PyMuPDFLoader
import tiktoken

# Load the PDF
def process_pdf(pdf):

    pdf_path = "attention.pdf"
    loader = PyMuPDFLoader(pdf_path)
    documents = loader.load()

    def count_words(text):
        return len(text.split())

    total_word_count = 0
    for doc in documents:
        total_word_count += count_words(doc.page_content)

    #print(f"Total number of words in the PDF: {total_word_count}")

    # Extract text from PDF
    text = ""
    for doc in documents:
        text += doc.page_content

    #encoding = tiktoken.get_encoding("cl100k_base")
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

    # Tokenize the text
    tokens = encoding.encode(text)

    # Count the tokens
    token_count = len(tokens)

    # Output the token count
    print(f"Total number of tokens: {token_count}")
    print(f"Total number of words in the PDF: {total_word_count}")
    print(text)

    return token_count 

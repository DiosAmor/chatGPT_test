from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter

pdf_reader = PdfReader("Draft P802.11ah_D10.0.pdf")

total_text = ""
for page in pdf_reader.pages:
    total_text += page.extract_text()

text_splitter = CharacterTextSplitter(
    separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len
)

chunks = text_splitter.split_text(total_text)
print(len(chunks))
print(chunks[0])
print(chunks[1000])

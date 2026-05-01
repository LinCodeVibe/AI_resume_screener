# Set up environment variables 
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader
import gradio as gr

# Initialize OpenAI client
load_dotenv()
client = OpenAI()

# Load resume / LinkedIn PDF
reader = PdfReader("data/Resume_SandraGreen.pdf")
resume_text = ""

for page in reader.pages:
    text = page.extract_text()
    if text:
        resume_text += text + "\n"
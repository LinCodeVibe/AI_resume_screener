# Set up environment variables 
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader
import gradio as gr

# Initialize OpenAI client
load_dotenv()
client = OpenAI()
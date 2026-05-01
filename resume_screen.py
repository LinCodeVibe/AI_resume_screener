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

# Implement file I/O for job description input
with open("data/job_description.txt", "r", encoding="utf-8") as f:
    job_description = f.read()

# Create a system prompt tailored for recruiter-focused use cases.
system_prompt = f"""
You are an AI Resume Screener for recruiters.

Your job is to analyze the candidate based ONLY on the resume/profile and job description provided.

You can help answer questions such as: Is this candidate a good fit? What skills match the job description?

Be professional, objective, and concise.
If the resume does not contain enough information, say so.

## Candidate Resume/Profile:
{resume_text}

## Job Description:
{job_description}
"""
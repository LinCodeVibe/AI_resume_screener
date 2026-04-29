# AI Resume Screener

An AI-powered recruiter assistant that analyzes a candidate’s resume to a job description and answers screening questions using LLMs.

---

## Features

- Load candidate resume (PDF / LinkedIn export)
- Analyze with job description
- Ask recruiter-style questions such as skills or fit score
- Interactive chat UI using Gradio

---

## How It Works

1. Extract text from resume PDF  
2. Load job description from `.txt` file  
3. Combine both into a structured prompt  
4. Send user questions + context to LLM  
5. Return intelligent screening responses  



---

## Installation & Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```
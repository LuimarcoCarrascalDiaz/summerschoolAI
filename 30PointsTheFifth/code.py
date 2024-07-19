from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai

# Authentication process
genai.configure(api_key="API_KEY")
model = genai.GenerativeModel('gemini-pro')

app = FastAPI()

class TextItem(BaseModel):
    text: str

@app.post("/summarize/")
async def summarize_text(text_item: TextItem):
    prompt = f"""
    Please summarize the following text in less than 100 words: {text_item.text}
"""
    response = model.generate_content(prompt)
    summary = response.text.strip()
    return {"summary": summary}

@app.post("/token_count/")
async def count_tokens(text_item: TextItem):
    # This is a simplified token count
    token_count = len(text_item.text.split())
    return {"token_count": token_count}

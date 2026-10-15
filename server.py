import os
import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai

# 1. Load environment variables
load_dotenv()

# 2. Initialize the AI Client
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# 3. Initialize FastAPI
app = FastAPI()

# Data models for validation
class Idea(BaseModel):
    title: str

class Topic(BaseModel):
    name: str

# Database connection helper
def get_db_connection():
    conn = sqlite3.connect("ideas.db")
    conn.row_factory = sqlite3.Row 
    return conn

# READ all ideas from the database
@app.get("/ideas")
def get_all_ideas():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM hackathon_ideas")
    rows = cursor.fetchall()
    conn.close()
    return {"ideas": [dict(row) for row in rows]}

# CREATE a manual idea
@app.post("/ideas")
def add_idea(idea: Idea):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO hackathon_ideas (title) VALUES (?)", (idea.title,))
    conn.commit()
    conn.close()
    return {"status": "success", "message": f"Successfully added '{idea.title}'"}

# GENERATE a new idea using Gemini and save it
@app.post("/generate")
def generate_ai_idea(topic: Topic):
    # 1. Prompt the AI using the user's topic
    prompt = f"Give me a 3-sentence hackathon pitch for an AI app about {topic.name}."
    
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )
    ai_pitch = response.text.strip()
    
    # 2. Save the AI's response directly to the database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO hackathon_ideas (title) VALUES (?)", (ai_pitch,))
    conn.commit()
    conn.close()
    
    # 3. Send the generated pitch back to the user
    return {"status": "success", "topic": topic.name, "pitch": ai_pitch}
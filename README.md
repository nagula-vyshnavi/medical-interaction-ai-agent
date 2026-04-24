# AI-First CRM HCP Module – Log Interaction System

## Overview
This project is an AI-first CRM module designed for Healthcare Professionals (HCPs). It allows field representatives to log interactions using either structured input or conversational text.

The system uses AI (LLM) to automatically extract insights such as HCP name, discussion topic, and sentiment.

# Medical Interaction AI Agent

AI-powered agent that analyzes medical 
interactions using FastAPI and Groq LLM.

## Features
- Analyzes doctor interactions
- Classifies sentiment
- Suggests follow-up actions
- Fetches HCP details

## Tech Stack
- FastAPI
- LangGraph
- Groq LLM
- Python

## How to Run

### Step 1 - Clone project
git clone YOUR_REPO_URL

### Step 2 - Install packages
pip install -r requirements.txt

### Step 3 - Add API key
Create .env file
Add: GROQ_API_KEY=your_key_here

### Step 4 - Start server
uvicorn main:app --reload --port 8000

### Step 5 - Test API
Open browser: http://127.0.0.1:8000/docs

## Sample Output
{
  "input": "Met Dr Rao, discussed diabetes medicine",
  "output": "AI response...",
  "sentiment": "Neutral",
  "followup": "Schedule follow-up...",
  "hcp": "Fetched HCP details"
}

## Developer
Nagula Vyshnavi
Email: nagulavyshnavi608@gmail.com

Live API: https://medical-interaction-ai-agent-1.onrender.com
API Docs: https://medical-interaction-ai-agent-1.onrender.com/docs

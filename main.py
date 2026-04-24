from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from agent import app_graph

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputModel(BaseModel):
    input_text: str

@app.post("/ai")
def ai_endpoint(data: InputModel):
    try:
        result = app_graph.invoke({
            "input": data.input_text,
            "output": ""
        })
        return result
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def home():
    return {"message": "API is running"}

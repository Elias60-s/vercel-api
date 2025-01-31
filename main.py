from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load JSON file at runtime
with open("q-vercel-python.json", "r") as file:
    student_marks = json.load(file)

@app.get("/api")
async def get_marks(name: list[str] = Query(...)):
    """Returns the marks of given student names."""
    marks = [student_marks.get(n, None) for n in name]
    return {"marks": marks}

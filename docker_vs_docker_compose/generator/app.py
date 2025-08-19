import random
from fastapi import FastAPI

app = FastAPI()

@app.get("/random_number")
def get_random_number():
    """Generates a random integer between 1 and 100."""
    return {"number": random.randint(1, 100)}
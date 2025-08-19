import requests
from fastapi import FastAPI

# The hostname "generator" is the name of the other service
# in our docker-compose.yml file.
GENERATOR_URL = "http://generator:8000/random_number"

app = FastAPI()

@app.get("/")
def read_root():
    """
    Returns hello world in JSON format as the result.
    It is an example of standalone API.
    """
    return {"Hello": "World"}


@app.get("/get_number_and_string")
def get_number_and_string():
    """
    Calls the generator service to get a random number and
    combines it with a string.
    """
    try:
        response = requests.get(GENERATOR_URL)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        random_number = data.get("number")
        
        if random_number is not None:
            return {"message": f"The random number is: {random_number}"}
        else:
            return {"error": "Could not retrieve number from generator service."}
            
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to connect to generator service: {e}"}
    
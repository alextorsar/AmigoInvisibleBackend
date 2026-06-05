from fastapi import FastAPI

app = FastAPI(
    title="Secret Santa API",
    description="Clean Architecture API for managing Secret Santa matches",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"message": "Secret Santa API is running"}

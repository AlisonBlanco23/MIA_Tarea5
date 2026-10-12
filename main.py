from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "hola desde aws"}

@app.get("/health")
def health():
    return {"status": "ok"}

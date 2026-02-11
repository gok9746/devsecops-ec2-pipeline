from fastapi import FastAPI

app = FastAPI(title="DevSecOps EC2 Pipeline Demo", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Hello from a secure CI/CD pipeline 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}

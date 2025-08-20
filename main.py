from fastapi import FastAPI

app = FastAPI()

# new path syntax
@app.get('/')
def root():
    return {'Hello': 'World'}
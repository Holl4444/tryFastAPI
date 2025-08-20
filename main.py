from fastapi import FastAPI

app = FastAPI()

items = []

# new path syntax
@app.get('/')
def root():
    return {'Hello': 'World'}

@app.post('/items')
# item = query parameter
def create_item(item: str):
    items.append(item)
    return item
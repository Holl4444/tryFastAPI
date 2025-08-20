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

@app.get('/items/{item_id}')
def get_item(item_id: int) -> str:
    item = items[item_id]
    return item

@app.get('/items')
def get_all_items() -> list[str]:
    return items
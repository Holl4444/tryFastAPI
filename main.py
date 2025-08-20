from fastapi import FastAPI, HTTPException

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
    if not item_id < 0 or item_id >= len(items):
        item = items[item_id]
        return item
    else:
        HTTPException(status_code=404, detail=f'Item {item_id} not found')

@app.get('/items')
def get_all_items() -> list[str]:
    return items
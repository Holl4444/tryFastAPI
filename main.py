from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str
    is_done: bool = False

items = []

# new path syntax
@app.get('/')
def root():
    return {'Hello': 'World'}

@app.post('/items')
# item = query parameter
def create_item(item: Item):
    items.append(item)
    return item



@app.get('/items/{item_id}', response_model=Item)
def get_item(item_id: int) -> Item:
    if not item_id < 0 or item_id >= len(items):
        item = items[item_id]
        return item
    else:
        HTTPException(status_code=404, detail=f'Item {item_id} not found')

@app.get('/items', response_model=list[Item])
# limit returned results
# adding type suggestion int allows fastapi to convert from url request string
# default limit is 10 - query parameter is alterable to any limit
def get_items(limit: int = 10) -> list[Item]:
    return items[0: limit]
**PYTHON VERV AND GENERAL SET UP**
Activate the virtual environment before installing packages.
python -m venv .venv
source .venv/Scripts/activate

Install dependencies with pip.
pip install fastapi
pip install uvicorn - server to test and run apps

- to get versions for req folder if freezing: pip show fastapi / uvicorn

Update requirements.txt with pip freeze > requirements.txt.
Make sure .venv/ is in .gitignore.

**CREATE APP**
import fastapi to main and create app (app = FastAPI())

**ADD ROOT PATH**
add root path (@app.get('/')) and function to define what is found there

**START SERVER**
*main being the file name + reload auto refreshes the server on change
in terminal type: uvicorn main:app --reload

** note server link is white not blue
check server working {"Hello: World"}

**ADD POST PATH**
Add post route (@app.post('*post_route*')) in our case adding item to todo list so:
@app.post('/items')
Add function to add the item to our item list

Either use Postman or open a new terminal in order to test the route receiving a request:
curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=apple'
curl http://127.0.0.1:8000/items/0

**ADD GET ITEM BY ID**
Add get specific item route (/items/{item_id}) syntax. Here it doesn't need an id establishing but USES LIST INDEX. Add function to return the item and test with:
curl http://127.0.0.1:8000/items/0
(May need to run curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=apple' again directly beforehand)

**ADD GET ALL ITEMS**
Add get entire list route ('/items') and test by adding a couple of items. Same prio as in JS where more specific routes need to come first.
test by adding a couple of things:

curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=apple'
curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=banana'

and running the get in a separate terminal or via Postman:
curl http://127.0.0.1:8000/items

Optionally add limit to the number of returned items with def get_items(limit: int = 1) -> list[str]:
    return items[0: limit]

**ERROR HANDLING**
import HTTPException from fastapi
add error handling in your code (ie/ out of bounds index error 404) using the syntax:
raise HTTPException(status_code=404, detail="Item not found") - detail optional
test an out of bounds index in the same way as previously in a separate terminal:
curl http://127.0.0.1:8000/items/5
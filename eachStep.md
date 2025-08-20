pixegami tutorial vid: https://www.youtube.com/watch?v=iWS9ogMPOI0

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

curl = command-line tool for making HTTP requests
-X POST = that this is a POST request (-X GET is get etc)
-H "Content-Type: application/json" = before adding a header (says 'sending JSON')

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

Optionally add limit to the number of returned items with def get_items(limit: int = 10) -> list[str]:
    return items[0: limit]
Hardcoded some list items to test default. To test limit parameter add it to url: curl http://127.0.0.1:8000/items?limit=3

**ERROR HANDLING**
import HTTPException from fastapi
add error handling in your code (ie/ out of bounds index error 404) using the syntax:
raise HTTPException(status_code=404, detail="Item not found") - detail optional
test an out of bounds index in the same way as previously in a separate terminal:
curl http://127.0.0.1:8000/items/5

**Data Structures: Pydantic Models**
import BaseModel: from pydantic import BaseModel - pydantic is already installed by default with fastapi
Extend BaseModel to become an Item class: 
    class Item(BaseModel):
        text: str = None
        is_done: bool = False

To make a field required, just delete the default. ie text: str = None -> text: str.
Test by removing text or changing field name.

Update app to use the model.
Update curl request to handle new JSON type (was str):
    curl -X POST -H "Content-Type: application/json" -d '{"text":"apple"}' 'http://127.0.0.1:8000/items'

-d '{"text":"apple"}' = data to send in request body

***Add return type***
Add "response_model=<model-type>" to the route, here using the class we made earlier:
@app.get("/items/{item_id}", response_model=Item)
Update /items route also with response_model = list[Item]

**FastAPI Docs**
Add /docs#/ to the url:
    127.0.0.1:8000/docs#/
Takes you to automated documentation where you can see all routes and schemas generated! Inspect them by clicking AND test paths without typing in CLI / using Postman. Clicking the small /openapi.json gives you a JSON file with all the info on your api

using /redoc instead gives a different layout?:
    127.0.0.1:8000/redoc


FASTAPI vs FLASK(open source community support)
-Async by default: handles more concurrent requests without config
-Easier to use
xLess adoption and support

Usecase: lightweight backend
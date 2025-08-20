Activate the virtual environment before installing packages.
python -m venv .venv
source .venv/Scripts/activate

Install dependencies with pip.
pip install fastapi
pip install uvicorn - server to test and run apps

- to get versions for req folder if freezing: pip show fastapi / uvicorn

Update requirements.txt with pip freeze > requirements.txt.
Make sure .venv/ is in .gitignore.

import fastapi to main and create app (app = FastAPI())

add root path (@app.get('/')) and function to define what is found there

*main being the file name + reload auto refreshes the server on change
in terminal type: uvicorn main:app --reload

** note server link is white not blue
check server working {"Hello: World"}

Add post route (@app.post('*post_route*')) in our case adding item to todo list so:
@app.post('/items')
Add function to add the item to our item list

Either use Postman or open a new terminal in order to test the route receiving a request:
curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=apple'
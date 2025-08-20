Activate the virtual environment before installing packages.
python -m venv .venv
source .venv/Scripts/activate

Install dependencies with pip.
pip install fastapi
pip install uvicorn - server to test and run apps

- to get versions for req folder if freezing: pip show fastapi / uvicorn

Update requirements.txt with pip freeze > requirements.txt.
Make sure .venv/ is in .gitignore.

import fastapi to main and create app

*main being the file name + reload auto refreshes the server on change
in terminal type: uvicorn main:app --reload
** note server link is white not blue
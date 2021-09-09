# flask-server
# Playground App for learning Flask
## May or may not be running on http://127.0.0.1:5000/
# 1) Install dependencies to virtual enviornment
python3 -m venv venv
. venv/bin/activate
## Potentially use this
virtualenv .env && source .env/bin/activate && pip install -r requirements.txt

# 2) Run Flask App. Must be reran if new routes are added.
flask run
## If you would like to make the server availible to your network, use:
flask run --host=0.0.0.0

## To enable dev features, set the FLASK_ENV enviornment variable to development:
export FLASK_ENV=development

#Importing Flask
from flask import Flask

# Creating an app
app = Flask(__name__)

# 3. Define index route
@app.route('/')
def hello_world():
    return 'Hello world'

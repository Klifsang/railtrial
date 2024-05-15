from flask import Flask
from models.myname import myname

app = Flask(__name__)

@app.route('/')
def hello_world():
    my_name = myname()
    return {'message':f'Hello, {my_name}!'}

if __name__ == '__main__':
    app.run()
from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/greet/<string:city>/')
def index(city: str):
    name = request.args.get('name')
    surname = request.args.get('surname')

    return f'<p>Hello {name} {surname} from {city}!</p>'
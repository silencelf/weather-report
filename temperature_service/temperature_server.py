import random
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_temperature():
    temp_c = random.randint(-10, 33)
    return { 'temp_c': temp_c }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
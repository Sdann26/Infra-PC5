"""Main application file"""
from flask import Flask
app = Flask(__name__)

@app.route('/home')
def home():  
    return "Israel Danilo Blas Salas"; 

if __name__ == '__main__':
    app.run(host='http://af2c1894962354504a9bede9aef1a66d-1177657013.us-east-2.elb.amazonaws.com/')
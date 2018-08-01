# _*_ coding: utf-8 _*_
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world!'
    
@app.route('/main')
def main():
    return 'Main Page' 
    
if __name__ == '__main__':
    app.debug = True 
    app.run()


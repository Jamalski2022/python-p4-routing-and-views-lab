#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)  
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
  
    return '\n'.join(str(i) for i in range(parameter)) + '\n'

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
   
    n1 = float(num1)
    n2 = float(num2)
    
    if operation == '+':
        result = n1 + n2
    elif operation == '-':
        result = n1 - n2
    elif operation == '*':
        result = n1 * n2
    elif operation == 'div':
        result = n1 / n2
    elif operation == '%':
        result = n1 % n2
    
    
    if operation == 'div':
        return str(result)
    return str(int(result))
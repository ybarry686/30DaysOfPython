"""
RESTful API's:
    - Structure of an API:
        - An API endpoint is a URL which can help retrieve, create, update, or delete a resource
            - Ex: https://api.twitter.com/1.1/lists/members.json
        - GET: Used for object retrieval
        - POST: Used for object creation and object actions
        - PUT: Used for object update
        - DELETE: Used for object deletion
"""
from flask import Flask, Response
import json
import os
import sqlite3

app = Flask(__name__)

con = sqlite3.connect('30DaysOfPython.db')
cur = con.cursor()


@app.route('/api/v1.0/students', methods = ['GET'])
def students():
    student_list = [
        {
            'name':'Asabeneh',
            'country':'Finland',
            'city':'Helsinki',
            'skills':['HTML', 'CSS','JavaScript','Python']
        },
        {
            'name':'David',
            'country':'UK',
            'city':'London',
            'skills':['Python','MongoDB']
        },
        {
            'name':'John',
            'country':'Sweden',
            'city':'Stockholm',
            'skills':['Java','C#']
        }
    ]
    return Response(json.dumps(student_list), mimetype='application/json')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
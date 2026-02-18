"""
Python for Web:
    Flask:
        - A web development framework written in Python. 
        - Uses Jinja2 template engine
        - Can be usually sued alongside other modern font libraries like React 
"""
from flask import Flask, render_template, request, redirect, url_for
import os # imports operating system module
import jinja2

app =  Flask(__name__) # Create Flask we app using current module location

print("TEMPLATE FOLDER:", app.template_folder)
print("ROOT PATH:", app.root_path)

@app.route('/') # This decorator creates the 'home' route
def home():
    print("Home is Working!")
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days of Python Programming'
    return render_template('home.html', techs=techs, name = name, title = 'Home')

@app.route('/about') # Creates the 'about' route
def about():
    print("About is Working!")
    name = '30 Days of Python Programming'
    return render_template('about.html', name = name, title = 'About Us')

@app.route('/post', methods=['GET', 'POST']) # Creates the post route
def post():
    print("Post is Working!")
    name = 'Text Analyzer'
    if request.method == 'GET':
        return render_template('post.html', name = name, title = name)
    if request.method == 'POST':
        content = request.form['content']
        print(content)
        return redirect(url_for('result'))

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    """ For deployment we use the environ to make it work 
        for both production and development """
    
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
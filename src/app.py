from pydoc import render_doc
from flask import Flask, render_template, render_template_string


app = Flask(__name__)

@app.get('/')
def index():
    return  render_template_string('<h1>welcome to flask 🌶️</h1>')



if __name__ == '__main__':
    app.run(debug=True)


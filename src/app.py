from flask import Flask, jsonify, render_template,  render_template_string, request



app = Flask(__name__)

@app.get('/add')
def add():
    return {'name': 'aayush', 'data': {'data': [1, 2, 3]}}

@app.get('/')
def index():
    return  render_template_string('<h1>welcome to flask 🌶️</h1>')

@app.post('/name/<int:name>')
def postThis():
    return 'This is a post request'

@app.patch('/patch')
def patchThis():
    return 'This is a patch request'

@app.delete('/delete')
def deleteThis():
    return 'The post is deleted.'

@app.get('/template')
def show_template():
    return render_template('index.html', listValue = [0, 2, 4, 7, 8])


@app.route('/home') 
def home():       
        data = "hello world"
        return jsonify({'data': data}) 
  

@app.route('/home/<int:num>', methods = ['GET']) 
def disp(num): 
  
    return jsonify({'data': num**2}) 

if __name__ == '__main__':
    app.run(debug=True)
    app.logger.debug('logging the application')



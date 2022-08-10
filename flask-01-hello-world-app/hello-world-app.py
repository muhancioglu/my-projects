from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World from Flask"

@app.route('/second')
def second():
    return "bize her yer afyon"

@app.route('/third/subthird')
def third():
    return "this is the subpage of third page"

@app.route('/forth/<string:id>')
def forth(id):
    return f'ID no {id} '









if __name__=='__main__':
    app.run(debug=True, port=2000)
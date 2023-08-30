from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/temp/')
def temp():
    return render_template('index.html')

@app.route('/name/<name>/id/<number>')
def func_name(name,number):
    number_user=int(number)*100
    return f'<h1>Привет,</h1> <p><b>{name}</b> - <i>{number_user}</i></p>'


if __name__ == '__main__':
    app.run()
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # render_template assumes html files are inside a templates folder
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/blog')
def blog():
    return 'This is what I think about blogs'


@app.route('/blog/2020/dogs')
def blog_dog():
    return 'This is my dog'


@app.route('/<username>')
def user(username=None):
    return render_template('name.html', name=username)

from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


###################################################
# You can specify types in the path:
# string - (default) accepts any text without a slash
# int - accepts positive integers
# float - accepts positive floating point values
# path - like string but also accepts slashes
# uuid - accepts UUID strings
###################################################

# Use escape for user provided values to protect from injection attacks
@app.route("/<name>")
def hello_name(name):
    return f"Hello, {escape(name)}!"


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

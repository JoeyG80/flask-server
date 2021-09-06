from flask import Flask, render_template, request, make_response, redirect, url_for, abort, jsonify, session
from markupsafe import escape
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = os.urandom(16)

@app.route("/")
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return redirect(url_for('login'))


# Redirect for login
@app.route('/login', methods=['GET', 'POST'])
def login():
    # abort(401)
    # resp = make_response(render_template('page_not_found.html'), 404)
    # resp.headers['X-Something'] = 'A value'
    # return resp
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

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


@app.route('/api')
def api(name=None):
    return jsonify({
        "TEST": 'test',
        "HELLO": 'hello',
    })

# File uploading and saving to the server

# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save(f"/var/www/uploads/{secure_filename(uploaded_file.txt)}")


#Reading cookies:
# @app.route('/')
# def index():
#     username = request.cookies.get('username')

# Storing cookies:
# @app.route('/')
# def index():
#     resp = make_response(render_template(...))
#     resp.set_cookie('username', 'the username')
#     return resp


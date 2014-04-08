from flask import Flask, abort, redirect, url_for, render_template, session, escape, request

app = Flask(__name__)
@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
        <p><input type=text name=username>
        <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if its there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return username 

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return str(post_id)

@app.route('/redirect_test')
def redirect_test():
    return redirect(url_for('error'))

@app.route('/error')
def error():
    abort(404)
    this_is_never_executed()

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

#ほんとはあげちゃダメだよ
app.secret_key = '\x08Rv\xa4\r\xc4\x17\xf8\xbc:N\xcdV\x18\x84\xe2\xac&\xb0\xd4\x8b\x1c^4'

if __name__ == '__main__':
    app.run()

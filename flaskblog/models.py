from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin 

@login_manager.user_loader #We decorate the function so that the extension knows that this is the functio to get a user by id
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	#we have to inherit from the UserMixin class in order to activate the extension
	
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False )
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	posts = db.relationship('Post', backref='author',lazy=True) #defines when sqlachemy loads the data from the db. True means 
																#sqlalchemy will load the data as necessary in one go. Will use the
																#post attribute to get the posts posted by an indivudual user 

#backref 'author' creates a column author in the posts table
	def __repr__(self):
		return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable = False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f"Post('{self.title}','{self.date_posted}')"

class Constituencies(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	const = db.Column(db.String(100), nullable=False)
	county = db.Column(db.String(100),nullable=False)

	def __repr__(self):
		return f"Constituency('{self.Constituency}') "
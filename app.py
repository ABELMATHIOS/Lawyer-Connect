from flask import Flask

app = Flask(__name__)

#Adding the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'

#Creating Secret key
app.config['SECRET_KEY']="123"

db = SQLAlchemy(app)

#Flask login
login_manager =LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_u'



#-----------------------------------------Creating Database Models-----------------------------------

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Adds a primary key
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(200),unique=True,nullable=False)
    phone = db.Column(db.String(200),unique=True,nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __ref__(self):
        return f'Users {self.id}-{self.first_name}-{self.last_name}-{self.username}-{self.email}-{self.phone}-{self.date_added}'

 
class Lawyers(db.Model):
    l_id = db.Column(db.Integer, primary_key=True)
    l_first_name = db.Column(db.String(200), nullable=False)
    l_last_name = db.Column(db.String(200))
    l_email = db.Column(db.String(200), unique=True, nullable=False)
    l_username = db.Column(db.String(200), unique=True, nullable=False)
    l_phone = db.Column(db.String(200), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False) 
    l_specialty = db.Column(db.String(200))
    l_experience = db.Column(db.String(200))
    l_date_added = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def l_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_l_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __ref__(self):
        return f'Users {self.l_id}-{self.l_first_name}-{self.l_last_name}-{self.l_email}-{self.l_username}-{self.password}-{self.l_specialty}-{self.l_experience}-{self.l_date_added}'


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


#-------------Form Classes-----------------------

class LawyerForm(FlaskForm):  
    l_first_name = StringField("First Name")
    l_last_name = StringField("Last Name")
    l_email = EmailField("Email")
    l_username = StringField("Username")
    l_phone = StringField("Phone")
    l_password = PasswordField("Password")
    l_specialty = StringField("Specialty")
    l_experience = SelectField(u"Experience",choices=[('1-2yrs'), ('3-5yrs'), ('5+')])
    submit = SubmitField("Register")

class UserForm(FlaskForm):  
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    username = StringField("Username")
    email = EmailField("Email")
    phone = StringField("Phone")
    password = PasswordField("Password")
    submit = SubmitField("Register")


#------------Log in Forms-----------------------------------------
class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password',validators=[DataRequired()])   
    submit = SubmitField("Login")  


 

#----------------NAV-Bar Links routes --------------
#Home route
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    create_database()
    app.run(debug=True)   
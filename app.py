from flask import Flask, render_template, flash,url_for, session,request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField,SelectField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin,login_user, LoginManager,login_required,logout_user,current_user

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
def index():
    return render_template('index.html')

#About Us route
@app.route('/about')
def about():
    return render_template('about.html')

#Attorneys route
@app.route('/attorneys')
def attorneys():
    return render_template('attorneys.html')

#News route
@app.route('/news')
def news():
    return render_template('page-news-single.html')

#Contact Us route
@app.route('/contact')
def contact():
    return render_template('contact.html')

#404 Error route
@app.errorhandler(404)
def page_not_found(e):
    return render_template('page-404.html')

#---------------Signup/Registration app Route---------------------------
@app.route('/user-r', methods=['GET','POST'])
#Users Form Registration and Validation
def signup():
    u_form = UserForm()
    first_name =None
    last_name =None
    email =None
    username=None
    phone=None
    password=None
    if request.method == "POST":
        if u_form.validate_on_submit():
            with app.app_context():
                new_user = Users(
                first_name=u_form.first_name.data,
                last_name=u_form.last_name.data,
                email=u_form.email.data,
                username=u_form.username.data,
                phone=u_form.phone.data,
                password=u_form.password.data)
                db.session.add(new_user)
                db.session.commit()
                session['username'] = username
                flash("Registration Succesfull!")
                return redirect(url_for('dashboard_u'))
        else:
            flash('Sorry,There was a problem with the registration please try again.....') 
    return render_template("user-registration.html",u_form=u_form)
      

@app.route('/lawyer-r', methods=['GET','POST'])

#Lawyer Form Registration and validation
def lawyer_signup():
    form =  LawyerForm()
    l_first_name=None
    l_last_name=None
    l_email=None
    l_username=None
    l_phone=None
    l_password=None
    l_specialty=None
    l_experience=None
    if form.validate_on_submit():
        with app.app_context(): 
            new_lawyer = Lawyers(
            l_first_name=form.l_first_name.data,
            l_last_name=form.l_last_name.data,
            l_email=form.l_email.data,
            l_username=form.l_username.data,
            l_phone=form.l_phone.data,
            l_password=form.l_password.data,
            l_specialty=form.l_specialty.data,
            l_experience=form.l_experience.data)
            db.session.add(new_lawyer)
            db.session.commit()
            session['l_username'] = l_username
            flash("Lawyer added successfully!")
            return redirect(url_for('dashboard_l'))

    return render_template("lawyer-registration.html", form=form)




#-------------------------Login Routes---------------------------

@app.route('/login-u', methods=['GET','POST'])

def login_u():
    username = request.form.get("username")
    password = request.form.get("password")
    user=Users.query.filter_by(username=username).first()

    if user and user.check_password(password):
        session['username'] = username
        flash("validated Succesfully!!!")
        return redirect(url_for('dashboard_u'))
    else:
        flash('Wrong Password or Email. Try again...')
    return render_template('login-u.html')

    
@app.route('/login-l', methods=['GET','POST'])
def login_l():
    l_username = request.form.get("l_username")
    password = request.form.get("l_password")
    user=Lawyers.query.filter_by(l_username=l_username).first()

    if user and user.check_l_password(password):
        session['l_username'] = l_username
        flash("validated Succesfully!!!")
        return redirect(url_for('dashboard_l'))
    else:
        flash('Wrong Password or Email. Try again...')
        return render_template('login-l.html')


@app.route('/logout-u', methods=['GET','POST'])
def logout():
        session.clear()
        return redirect(url_for('index'))



#User Dashbaord
@app.route('/dashboard-u')

def dashboard_u():
    if session["username"]:
        return render_template('dashboard.html')
    else:
        return redirect(url_for("login_u"))


#Lawyer Dashboard
@app.route('/dashboard-l')
def dashboard_l():
    if session["l_username"]:
        return render_template('lawyer-dashboard.html')
    else:
        return redirect(url_for("login_l"))

#Admin route
@app.route('/admin')
def admin():
  reg_users=Users.query.all()
  reg_lawyers=Lawyers.query.all()
  return render_template('admin.html' , reg_users=reg_users,reg_lawyers=reg_lawyers)


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




#---------Creating the database-----------

def create_database():
    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    create_database()
    app.run(debug=True)   
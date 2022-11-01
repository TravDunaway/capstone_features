from flask import Flask, render_template, redirect, flash, request, url_for
import jinja2
from forms import LoginForm, SignupForm
from model import db, User, Signup, Login, connect_to_db

app = Flask(__name__)
app.secret_key = "Keep this secret"
app.jinja_env.undefined = jinja2.StrictUndefined

user_id = 1

@app.route("/")
def home():
    signup_form = SignupForm()
    login_form = LoginForm()
    login_form.update_signup(User.query.get(user_id).signups)
    return render_template("home.html", title = "login-signup", page = "home", signup_form = signup_form, login_form = login_form)

app.route("/add-signup", methods=["POST"])
def add_signup():
    signup_form = SignupForm()

    if signup_form.validate_on_submit():
        signup_name = signup_form.signup_name.data
        new_signup = Signup(signup_name, user_id)
        db.session.add(new_signup)
        db.session.commit()
        print("New signup has occured")
        return redirect(url_for("home"))
    else:
        print("New signup route didn't work")
        return redirect(url_for("home"))

@app.route("/add-login", methods=["POST"])
def add_login():
    login_form = LoginForm()
    login_form.update_signup(User.query.get(user_id).signups)

    if login_form.validate_on_submit():
        user_login_email = login_form.user_login_email.data
        user_login_password = login_form.user_login_password.data
        remember_me = login_form.remember_me.data
        
        signup_id = login_form.signup_selection.data

        new_login = Login(user_login_email, user_login_password, remember_me, signup_id) 
        db.session.add(new_login)
        db.session.commit()
        print("added login seemed to work correctly")
        return redirect(url_for("home"))
    else:
        ("added login did not work")
        return redirect(url_for("home"))

@app.route("/signups")
def signups():
    user = User.query.get(user_id)
    return render_template("signups.html", title = "signups", page = "signups", signups = user.signups)

@app.route("/logins")
def logins():
    user = User.query.get(user_id)
    logins = user.get_all_logins()
    return render_template("logins.html", title = "logins", page = "logins", logins = logins)

@app.route("/update-signup/<signup_id>", methods=["GET", "POST"])
def update_signup(signup_id):
    form = SignupForm()
    signup = signup.query.get(signup_id)
    if request.method == "POST":
        if form.validate_on_submit():
            signup.signup_name = form.signup_name.data
            db.session.add(signup)
            db.session.commit()
            return redirect(url_for("signups"))
        else:
            return redirect(url_for("home"))

    else:
        return render_template("update-signup.html", title = f"Update {signup.signup_name}", page = "signups", signup = signup, form = form)

@app.route("/update-login/<login_id>", methods=["GET", "POST"])
def update_login(login_id):
    form = LoginForm()
    form.update_signup(User.query.get(user_id).signups)
    login = Login.query.get(login_id)

    if request.method == "POST":
        if form.validate_on_submit():
            login.user_login_email = form.user_login_email.data
            if len(form.description.data) > 0:
                login.description = form.description.data
            login.remember_me = form.remember_me.data
            login.signup_id = form.signup_selection.data
            db.session.add(login)
            db.session.commit()
            return redirect(url_for("logins"))
        else:
            return redirect(url_for("home"))   
    else:
        return render_template("update-login.html", title = f"Update {login.user_login_email}", page = "logins", login = login, form = form)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug = True)

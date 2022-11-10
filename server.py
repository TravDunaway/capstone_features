
from flask import Flask, render_template, redirect, url_for, flash, abort, request
from forms import NewUser, OldUser
from model import db, User, connect_to_db
#
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash 
#^^


app = Flask(__name__)
app.secret_key = "Keep this secret"



user_id = 1

@app.route("/")
def home():
    newuser_form = NewUser()
    form = OldUser()
    return render_template("home.html", newuser_form = newuser_form, form = form)

@app.route("/where")
@login_required
def where():
    return render_template("where.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You logged out!")
    return redirect(url_for('home'))




@app.route("/register", methods=["GET","POST"])
def add_newuser():
    newuser_form = NewUser()

    if newuser_form.validate_on_submit() and newuser_form.check_email() and newuser_form.check_username():
        username = newuser_form.username.data
        password = newuser_form.password.data
        user_email = newuser_form.password.data
        newuser_info = User(username, password, user_email)
        db.session.add(newuser_info)
        db.session.commit()
        flash("Thanks for Registering")
        print(newuser_form.username.data)
        print(newuser_form.password.data)
        print(newuser_form.user_email.data)
        return redirect(url_for("where"))
    else:
        flash("Oops, lets try that again.")
        print("Your newuser_form didn't submit properly.")
        return redirect(url_for("home"))
    


@app.route("/login", methods=["GET", "POST"])
def login():
    form = OldUser()

    if form.validate_on_submit():
        user = User.query.filter_by(user_email=form.user_email.data).first()

        if user.check_password(form.password.data) and user is not None:

            login_user(user)
            flash('Logged in Successfully!')

            next = request.args.get('next')

            if next == None or not next[0] =='/':
                next = url_for('where')
            
    return render_template('home.html', form=form)
        
            

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug = True)













# app = Flask(__name__)
# app.secret_key = "Keep this secret"



# user_id = 1

# @app.route("/")
# def home():
#     newuser_form = NewUser()
#     form = OldUser()
#     return render_template("home.html", newuser_form = newuser_form, form = form)

# @app.route("/where")
# def where():
#     return render_template("where.html")

# @app.route("/add-newuser", methods=["GET","POST"])
# def add_newuser():
#     newuser_form = NewUser()

#     if newuser_form.validate_on_submit() and newuser_form.check_email() and newuser_form.check_username():
#         username = newuser_form.username.data
#         password = newuser_form.password.data
#         user_email = newuser_form.password.data
#         newuser_info = User(username, password, user_email)
#         db.session.add(newuser_info)
#         db.session.commit()
#         print(newuser_form.username.data)
#         print(newuser_form.password.data)
#         print(newuser_form.user_email.data)
#         return redirect(url_for("home"))
#     else:
#         print("Your newuser_form didn't submit properly.")
#         return redirect(url_for("home"))

# @app.route("/login", methods=["GET", "POST"])
# def login():
#     form = OldUser()

#     if form.validate_on_submit() and form.check_user_info():
#         print("Youve been directed to the where page.")
#         return redirect(url_for("where"))




# if __name__ == "__main__":
#     connect_to_db(app)
#     app.run(debug = True)




















































# @app.route("/")
# def home():
#     signup_form = SignupForm()
#     login_form = LoginForm()
#     login_form.update_signup(User.query.get(user_id).signups)
#     return render_template("home.html", title = "login-signup", page = "home", signup_form = signup_form, login_form = login_form)

# @app.route("/add-signup", methods=["POST"])
# def add_signup():
#     signup_form = SignupForm()

#     if signup_form.validate_on_submit():
#         signup_name = signup_form.user_signup_email.data

#         new_signup = Signup(signup_name, user_id)
#         db.session.add(new_signup)
#         db.session.commit()
#         print("New signup has occured")
#         return redirect(url_for("home"))
#     else:
#         print("New signup route didn't work")
#         return redirect(url_for("home"))

# @app.route("/add-login", methods=["POST"])
# def add_login():
#     login_form = LoginForm()
#     login_form.update_signup(User.query.get(user_id).signups)

#     if login_form.validate_on_submit():
#         user_login_email = login_form.user_login_email.data
#         user_login_password = login_form.user_login_password.data
#         remember_me = login_form.remember_me.data
        
#         signup_id = login_form.signup_selection.data

#         new_login = Login(user_login_email, user_login_password, remember_me, signup_id) 
#         db.session.add(new_login)
#         db.session.commit()
#         print("added login seemed to work correctly")
#         return redirect(url_for("home"))
#     else:
#         ("added login did not work")
#         return redirect(url_for("home"))

# @app.route("/signups")
# def signups():
#     user = User.query.get(user_id)
#     return render_template("signups.html", title = "signups", page = "signups", signups = user.signups)

# @app.route("/logins")
# def logins():
#     user = User.query.get(user_id)
#     logins = user.get_all_logins()
#     return render_template("logins.html", title = "logins", page = "logins", logins = logins)

# @app.route("/update-signup/<signup_id>", methods=["GET", "POST"])
# def update_signup(signup_id):
#     form = SignupForm()
#     signup = signup.query.get(signup_id)
#     if request.method == "POST":
#         if form.validate_on_submit():
#             signup.signup_name = form.signup_name.data
#             db.session.add(signup)
#             db.session.commit()
#             return redirect(url_for("signups"))
#         else:
#             return redirect(url_for("home"))

#     else:
#         return render_template("update-signup.html", title = f"Update {signup.signup_name}", page = "signups", signup = signup, form = form)

# @app.route("/update-login/<login_id>", methods=["GET", "POST"])
# def update_login(login_id):
#     form = LoginForm()
#     form.update_signup(User.query.get(user_id).signups)
#     login = Login.query.get(login_id)

#     if request.method == "POST":
#         if form.validate_on_submit():
#             login.user_login_email = form.user_login_email.data
#             if len(form.description.data) > 0:
#                 login.description = form.description.data
#             login.remember_me = form.remember_me.data
#             login.signup_id = form.signup_selection.data
#             db.session.add(login)
#             db.session.commit()
#             return redirect(url_for("logins"))
#         else:
#             return redirect(url_for("home"))   
#     else:
#         return render_template("update-login.html", title = f"Update {login.user_login_email}", page = "logins", login = login, form = form)


# if __name__ == "__main__":
#     connect_to_db(app)
#     app.run(debug = True)

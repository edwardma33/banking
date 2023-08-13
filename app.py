from flask import Flask, render_template, session, redirect, request, url_for
from db.sql import User

app = Flask(__name__)
app.config["SECRET_KEY"] = "asdvjkbdsalvbads"

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/dashboard')
def dashboard():
    if session["username"]:
        return render_template("dashboard.html", username=session["username"])
    else:
        print("No Username")
        return redirect(url_for("home"))

@app.route('/auth', methods=['POST'])
def auth():
    error = None
    username = request.form.get("username")
    password = request.form.get("password")

    if username is None or password is None:
        error = "Both fields must be filled out"
    else:
        user = User(username, password)

    if user.is_username_valid() == False:
        error = "Username either taken or too short. Try logging in or try a new username over 4 characters"
    
    if user.is_password_valid() == False:
        error = "Password must be 8 or more characters"

    if error is None:
        user.save()
        session["username"] = username
        return redirect(url_for("dashboard"))
    else:
        print(error)
        return redirect(url_for("home"))
    
@app.route('/logout')
def logout():
    session.pop("username")
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
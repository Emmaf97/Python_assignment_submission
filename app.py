from flask import Flask, render_template, request, redirect, url_for, flash,session
from flask_login import login_user,current_user, LoginManager, UserMixin, logout_user
import secrets
import json
import os

app = Flask(__name__)
# Generate a random secret key of 32 bytes


login_manager = LoginManager(app)

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
        

@app.route("/")
def index():
    # print("before user check is done")
    user_id = session.get('user_id')
    if user_id:
        user = load_user(user_id)
        return render_template('index.html', username=user.username)
    return render_template('index.html')

@app.route("/schedule")
def schedule():
    print("before user check is done")
    user_id = session.get('user_id')
    if user_id:
        print("schedule")
        user = load_user(user_id)
        return render_template('schedule.html', username=user.username)
    return render_template("schedule.html")

@app.route("/trainers")
def trainers():
    user_id = session.get('user_id')
    if user_id:
        user = load_user(user_id)
        return render_template('trainers.html', username=user.username)
    return render_template("trainers.html")

@app.route("/videos")
def videos():
    user_id = session.get('user_id')
    if user_id:
        user = load_user(user_id)
        return render_template('videos.html', username=user.username)
    return render_template("videos.html")

@app.route("/contact")
def contact():
    user_id = session.get('user_id')
    if user_id:
        user = load_user(user_id)
        return render_template('contact.html', username=user.username)
    return render_template("contact.html")

def load_user(user_id):
    json_file_path = os.path.join(app.static_folder, 'json', 'user.json')
    with open(json_file_path, 'r') as file:
        users = json.load(file)
        for user in users["users"]:
            if user["id"] == user_id:
                return User(user["id"], user["username"], user["password"])
    return None

login_manager.user_loader(load_user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form['username']
        password = request.form['password']
    
        # Authenticate user here (e.g., by checking credentials against the JSON file)
        user = authenticate_user(username, password)
    
        if user:
            login_user(user)
            session['user_id'] = user.id  # Store user ID in session
            flash('Logged in successfully.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password.', 'error')
            return redirect(url_for('login'))

    

def authenticate_user(username, password):
    json_file_path = os.path.join(app.static_folder, 'json', 'user.json')
    with open(json_file_path, 'r') as file:
        users_list = json.load(file)
        # print("Type of users_data:", type(users_list))
        # print("Value of users_data:", users_list)
        for users_list in users_list.values():
            for users in users_list:
                if users["username"] == username and users["password"] == password:
                    return User(users["id"], users["username"], users["password"])
    return None
    
@app.route('/logout', methods=['GET','POST'])
# @login_required          # had to remove the @login_required it was causing and error
def logout():
    if current_user.is_authenticated:
        print("Current user session:", current_user.username)
    else:
        print("No user is currently logged in.")
    
    if request.method == "GET":
        logout_user()
        flash('Logged out successfully.', 'success')
        return redirect(url_for('login'))



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    # app.run()
    app.run(debug=True, port=8080)

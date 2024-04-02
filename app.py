from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)


@app.route("/")
def index():
    logged_in = request.args.get('logged_in', False)
    username = request.args.get('username', '')
    return render_template('index.html', logged_in=logged_in, username=username)                    # passing parameter queries to jinja elements to display content.

@app.route("/schedule")
def schedule():
    return render_template("schedule.html")

@app.route("/trainers")
def trainers():
    return render_template("trainers.html")

@app.route("/videos")
def videos():
    return render_template("videos.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

def load_users(file_path: str) -> dict:                                                                    
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        json_file_path = os.path.join(app.static_folder, 'json', 'user.json')                       #I was having trouble with the path configuration so I used os path to solve this issue and read the json file.
        user_list = load_users(json_file_path)
        user_name_field = request.form['username']
        user_password_field = request.form['password']
        
        for user in user_list["users"]:
            if user_name_field == user["username"] and user_password_field == user["password"]:    # if the inputs match json data redirects and passes variables as parameter queries.
                print("Correct credentials entered. User logged in")
                return redirect(url_for('index', logged_in=True, username=user["username"]))
        
        print("Incorrect username or password")
        return render_template("login.html")
    
                                                                                                   # If the request method is GET, render the login form
    return render_template("login.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    # app.run()
    app.run(debug=True, port=8080)

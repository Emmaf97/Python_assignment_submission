from flask import Flask, render_template, url_for
import json
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

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
    json_file_path = os.path.join(app.static_folder, 'json', 'user.json')
    user_list = load_users(json_file_path)
    print(user_list)
    return render_template("login.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")




if __name__ == "__main__":
    # app.run()
    app.run(debug=True, port=8080)

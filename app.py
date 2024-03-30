from flask import Flask, render_template, url_for

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")


if __name__ == "__main__":
    # app.run()
    app.run(debug=True, port=8080)

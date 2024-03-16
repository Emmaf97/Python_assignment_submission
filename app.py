from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/schedule")
def canyon():
    return render_template("schedule.html")


@app.route("/trainers")
def javelina():
    return render_template("trainers.html")


@app.route("/videos")
def weekend():
    return render_template("videos.html")


# @app.route("/festival")
# def festival():
#     return render_template("festival.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=8080)

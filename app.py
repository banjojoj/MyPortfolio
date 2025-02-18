from flask import Flask, render_template

# define flask app
app = Flask(__name__)


# home route
@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

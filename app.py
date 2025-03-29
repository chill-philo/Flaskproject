from flask import Flask,render_template
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/About")
def About():
    return "<p>About</p>"

if __name__ == "__main__":
    app.run()
def Home():
   my_title = "Home"
   context = {"my_title": my_title}
   return render_template("home.html", context=context)

@app.route("/Gallery")
def Gallery():
    return "<p>Gallery!<p>"
@app.route("/Contact Us")
def Contact_Us():
    return "<p>Contact Us!<p>"


if __name__ == "__main__":
    app.run()


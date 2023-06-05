from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        "Autor" : "Jacek", 
        "post": "post nr 1",
        "kontent": " siema"
    }
]

@app.route("/home")
@app.route("/")
def index():
    return render_template("home.html", post = posts , title = "Home")

@app.route("/about")
def about():
    return render_template("about.html", title = "About")
    

if __name__ == "__main__":
    app.run(debug=True)

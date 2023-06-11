from flask import Flask, render_template, flash
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "2190cj7jf0sda90902j8"

posts = [
    {
        "Autor" : "Jacek", 
        "post": "post nr 1",
        "kontent": " siema"
    }
]

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html", post = posts , title = "Home")

@app.route("/about")
def about():
    return render_template("about.html", title = "About")

@app.route("/register", methods =["POST","GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created {form.username.data}!", "succes")
    return render_template("register.html", title="Register",  form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login",  form = form)
    
    

if __name__ == "__main__":
    app.run(debug=True)

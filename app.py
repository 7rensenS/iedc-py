from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return "you are in home"

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
   return render_template("contact.html")

@app.route("/webpage")
def webpg():
   return render_template("webpg.html")

if(__name__=="__main__"):
    app.run(debug=True)



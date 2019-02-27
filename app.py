from flask import Flask  

app=Flask(__name__)

@app.route("/")
def index():
    return "<h1>hello you are in...</h1>"\

@app.route("/home")
def home():
    return "you are in home"

@app.route("/about")
def about():
    return "you are in about"

@app.route("/contact")
def contact():
    return "you are in contact"

if(__name__=="__main__"):
    app.run(debug=True)



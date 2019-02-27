from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def webpg():
   return render_template("webpg.html")

if(__name__=="__main__"):
    app.run(debug=True)



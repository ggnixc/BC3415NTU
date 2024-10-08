from flask import Flask, render_template, request
import google.generativeai as palm

api = "AIzaSyCaQcgKn95ZO6AR1t2PXzk9UydTkt4sWZQ"
palm.configure(api_key=api)
model = {"model": "models/chat-bison-001"}

app = Flask(__name__, template_folder = ".") #template folder = "." sets the search for the template folder to current folder

@app.route("/", methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/financial_FAQ", methods=["GET","POST"])
def financial_FAQ():
    return render_template("financial_FAQ.html")

@app.route("/makersuite", methods=["GET","POST"])
def makersuite():
    q = request.form.get("q")
    r = palm.chat(messages=q, **model)
    return render_template("makersuite.html", r=r.last)

@app.route("/sg_joke", methods=["GET","POST"])
def sg_joke():
    return render_template("sg_joke.html")

if __name__ == "__main__":
    app.run()

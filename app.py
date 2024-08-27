from flask import Flask,render_template,request
import google.generativeai as palm
import os
import random
import wikipedia

api = os.getenv("MAKERSUITE_API_TOKEN")
palm.configure(api_key=api)
model = {"model": "models/chat-bison-001"}

# List of Singaporean jokes
# Extended list of Singaporean jokes
jokes = [
    "The only thing faster than Singapore's MRT during peak hours is the way we 'chope' seats with a tissue packet.",
    "Why did the chicken cross the road in Singapore? To get to the other side before the ERP charges kick in!",
    "In Singapore, the quickest way to lose friends is to say, 'Let's split the bill equally!'",
    "Why don't Singaporeans play hide and seek? Good luck hiding in a country where everything is so efficient!",
    "In Singapore, the best way to avoid a parking fine is to simply not drive.",
    "Why did the kopitiam uncle refuse to serve kopi? Because the coffee was already 'gao' enough!",
    "What did one HDB block say to the other? 'You lift me up!'",
    "Why did the durian go to the gym? To get stronger spikes!",
    "What do Singaporeans say when they don’t want to take sides? 'Anything, lah!'",
    "Why do Singaporeans never get lost? Because there’s a hawker centre on every corner!"
]

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/financial_QA",methods=["GET","POST"])
def financial_QA():
    return(render_template("financial_QA.html"))

@app.route("/makersuite",methods=["GET","POST"])
def makersuite():
    q = request.form.get("q")
    try:
        r = palm.generate_text(**model, prompt=q)
    except Exception:
        r = wikipedia.summary(q, sentences=5)
        return (render_template("makersuite.html", r=r))

    return(render_template("makersuite.html",r=r.result))

@app.route("/prediction",methods=["GET","POST"])
def prediction():
    return(render_template("prediction.html"))

@app.route("/joke", methods=["GET", "POST"])
def joke():
    if request.method == "POST":
        selected_joke = random.choice(jokes)
    else:
        selected_joke = random.choice(jokes)
    return render_template("joke.html", r=selected_joke)

if __name__ == "__main__":
    app.run()
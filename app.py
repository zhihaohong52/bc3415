from flask import Flask,render_template,request
import google.generativeai as palm
import os
import random

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
    "Why do Singaporeans never get lost? Because there’s a hawker centre on every corner!",
    "Why don't Singaporeans ever play Monopoly? Because they've already mastered the art of property investment.",
    "Why was the Singaporean computer cold? It left its 'Windows' open!",
    "Why don't Singaporeans ever tell secrets? Because they don't want to 'leak' information like Orchard Road during a flood.",
    "Why was the MRT so crowded? Because everyone wanted to 'Stand Clear of the Closing Doors!'",
    "Why did the Singaporean bring a ladder to work? To reach the top of the CPF ladder!",
    "Why did the chili crab cross the road? To join its friends at the seafood restaurant!",
    "Why did the hawker centre stall close early? Because they ran out of 'shiok' food!",
    "Why are Singaporean roads so smart? Because they have ERP gantries to keep them in check!",
    "Why do Singaporeans love air conditioning? Because it's the only way to escape the 'lah' in the hot weather!",
    "Why don’t Singaporeans use GPS? Because they already know where the best makan places are!",
    "Why was the Singaporean so punctual? Because he didn’t want to miss the 'chope' time!",
    "Why don't Singaporeans use calendars? Because every day is National Day when you’re this proud!",
    "Why did the Singaporean cross the road? To get to the other side... before the ERP charges kicked in again!",
    "Why did the Singaporean office worker bring a pillow to work? To 'chope' their seat for the next meeting!",
    "Why was the Singaporean baker so successful? Because he kneaded the dough!",
    "Why was the MRT so clean? Because even germs have to pay an ERP charge!",
    "Why do Singaporeans never play hide and seek? Because no one can hide from the efficient government!",
    "Why did the chicken rice vendor become a millionaire? Because he knew how to 'rice' to the occasion!",
    "Why was the kopi so strong? Because it had 'gao' power!",
    "Why do Singaporeans love to queue? Because the longer the queue, the better the food!",
    "Why don’t Singaporeans play poker? Because they already know how to 'chope' their cards!"
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
    r = palm.chat(prompt=q, **model)
    return(render_template("makersuite.html",r=r.last))

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
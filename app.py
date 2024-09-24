from flask import Flask,render_template,request
import google.generativeai as genai
import os
import random
import wikipedia

api = os.getenv("MAKERSUITE_API_TOKEN")
genai.configure(api_key=api)

config = genai.GenerationConfig(temperature=0.5)

model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello, you are a wikipedia chatbot who can provide one-paragraph summaries of various topics. Do not ask questions, just provide information."}
    ]
)

jokes = ["The only thing faster than Singapore's MRT during peak hours is the way we chope seats with a tissue packet." ,
         "Jay Powell has signalled he is ready to cut US interest rates in September, as he warned that 'downside risks' to the labour market had increased."]

chat2 = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello, please tell me jokes about Singapore or financial news."},
        {"role": "model", "parts": "Sure, I can do that. Give me a moment to think of some jokes."},
        {"role": "user", "parts": f"Some examples of jokes are: {jokes}"},
    ]
)

choice = ["Singapore", "financial news"]

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
        response = chat.send_message(q)
        r = response.text
    except Exception as e:
        print(e)
        r = wikipedia.summary(q, sentences=5)
    return (render_template("makersuite.html", r=r))

@app.route("/joke", methods=["GET", "POST"])
def joke():
    response = chat2.send_message("Give me a joke about " + random.choice(choice))
    return render_template("joke.html", r=response.text)

if __name__ == "__main__":
    app.run()
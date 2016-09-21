from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso"

@app.route("/Gryffindor")
def Gryffindor():
    return "Where dwell the brave at heart"

@app.route("/Hufflepuff")
def Hufflepuff():
    return "Where they are just and loyal"

if __name__=="__main__":
    app.run()

    

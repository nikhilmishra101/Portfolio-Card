from flask import Flask,render_template
from jinja2 import escape

app = Flask(__name__) #__name__ is the name of the current directory

@app.route('/')
def home():
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)

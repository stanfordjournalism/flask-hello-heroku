from flask import Flask
from flask import render_template
from random import randrange
from datetime import datetime

app = Flask(__name__)



@app.route("/hello/")
def hellofoo():
    return """
        <h1>
            Hello <em style="color:hotpink">world!</em>
        </h1>"""

@app.route("/")
def homepage():
    w = randrange(4, 20) * 50
    h = randrange(4, 20) * 40
    t = datetime.now().isoformat()

    return render_template('homepage.html',
            width=w, height=h, current_time=t)



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

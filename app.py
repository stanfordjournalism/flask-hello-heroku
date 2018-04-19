from flask import Flask
from flask import render_template
from random import randrange
from datetime import datetime

myapp = Flask(__name__)



@myapp.route("/hello/")
def hellofoo():
    return """
        <h1>
            Hello <em style="color:hotpink">world!</em>
        </h1>"""

@myapp.route("/")
def homepage():
    w = randrange(4, 20) * 50
    h = randrange(4, 20) * 40
    t = datetime.now().isoformat()

    return render_template('homepage.html',
            width=w, height=h, current_time=t)



if __name__ == '__main__':
    myapp.run(debug=True, use_reloader=True)

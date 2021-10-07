from flask import Flask, render_template
from werkzeug.utils import redirect
app = Flask(__name__)
import random

random_num = 0

@app.route('/')
def index():
    return render_template('index.html', number=random_num)

@app.route('/gen_num')
def generate_number():
    global random_num
    random_number = random.randint(1,100)
    random_num = random_number
    print("*"*50)
    print(random_num)
    print("*"*50)
    return redirect('/')

@app.route('/guess/<int:guess>')
def greet(guess):
    if guess == random_num:
        response_msg = "Finally Correct!"
        return render_template('gify.html', guess=guess, message=response_msg)
    else:
        if guess > random_num:
            response_msg = "Your guess is too high"
        elif guess < random_num:
            response_msg = "Your guess is too low"
        return render_template('incorrect.html', message = response_msg)

# THIS WILL LET US RUN OUR SERVER WITHOUT COMMANDS. 
if __name__ == "__main__":
    app.run(debug=True)


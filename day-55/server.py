from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)
print(random_number)


@app.route("/")
def index():
    return "<main><h1>Guess a number between 0 and 9</h1>\
        <img src='https://media.giphy.com/media/hvLwZ5wmarjnNKEJqq/giphy-downsized-large.gif' width='500' /></main>"


@app.route("/<int:number>")
def user_guess(number):
    print(number)

    if number < random_number:
        return "<div>\
            <h1 style='color: orange'>Too low.</h1>\
                 <img src='https://media.giphy.com/media/l3vRbgCJxtSXS9jFe/giphy.gif' width='500' />\
            </div>"
    elif number > random_number:
        return "<div>\
            <h1 style='color: red'>Too high!</h1>\
                 <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width='500' />\
            </div>"

    return "<div>\
        <h1 style='color: green'>Correct!</h1>\
                <img src='https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif' width='500' />\
        </div>"


if __name__ == "__main__":
    app.run(debug=True)

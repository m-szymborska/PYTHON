import random
from flask import Flask

my_number=random.randint(0,9)
print(my_number)

app = Flask(__name__)

@app.route("/")
def guess():
    return "<h1>Guess a number between 0 and 9</h1>"

@app.route("/<int:numb>")
def answer(numb):
    if numb < my_number:
        return ("<h1 style='color: blue'>To low</h1>")
    elif numb > my_number:
        return ("To hight")
    else:
        return ("Yes, it this number!!")


if __name__ == "__main__":
    app.run(debug=True)
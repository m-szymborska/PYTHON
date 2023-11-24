from flask import Flask
app = Flask(__name__)

def make_underline(func):
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper

def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def make_ephasis(func):
    def wrapper():
        return f"<em>{func()}</em>"
    return wrapper


@app.route("/")
@make_bold
@make_ephasis
@make_underline
def hello_world():
    return ('<h1 style="text-align: center">Hello, World</h1><p>'
            'This is paragrapf</p>'
            '<img src="https://www.dolina-noteci.pl/data/include/cms/Blog-DN/nowonarodzone_koty.jpg"'
            'width=200>'
            '<img src="https://media.giphy.com/media/uWYjSbkIE2XIMIc7gh/giphy.gif">')


@app.route("/bye")
def bye():
    return "ByByBy"

@app.route("/username/<name>")
def geet(name):
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask
from flask import render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def foot():
    random_number = random.randint(1,10)
    year = datetime.datetime.now().year
    return render_template("index.html", yer=year)


@app.route('/guess/<name>')
def test(name):

    response = requests.get(url=f"https://api.genderize.io?name={name}")
    response.raise_for_status()
    data_gender = response.json()
    gender = data_gender["gender"]

    response1 = requests.get(url=f"https://api.agify.io?name={name}")
    response1.raise_for_status()
    data_age = response1.json()
    age = data_age["age"]

    return render_template("guess.html", nam=name, gen=gender, ag=age)

@app.route('/blog/<num>')
def blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_post = response.json()
    return render_template("blog.html", posts=all_post)
if __name__ == "__main__":
    app.run(debug=True)


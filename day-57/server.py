from flask import Flask, render_template
import requests
import datetime
from post import Post


response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
posts_data = response.json()

posts = []
for post in posts_data:
    posts.append(Post(post))


app = Flask(__name__)


@app.route("/")
def index():
    year_today = datetime.date.today().year
    return render_template("index.html", year_today=year_today)


@app.route("/blogs")
def blogs():
    return render_template("blogs.html", posts=posts)


@app.route("/blog/<post_id>")
def single_blog(post_id):
    requested_post = [post for post in posts if str(post.id) == str(post_id)][0]
    print(requested_post)
    return render_template("single-blog.html", post=requested_post)


@app.route("/guess/")
@app.route("/guess/<name>")
def guess(name):
    genderize_response = requests.get(
        f"https://api.genderize.io?name={name}", timeout=130
    )
    genderize_data = genderize_response.json()
    gender = genderize_data["gender"]

    agify_response = requests.get(f"https://api.agify.io?name={name}", timeout=130)
    agify_data = agify_response.json()
    age = agify_data["age"]

    return render_template("guess.html", name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)

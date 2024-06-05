from flask import Flask, render_template, url_for

app = Flask(__name__)

dummy_blog_data = [
    {
        "title": "My First Blog Post",
        "author": "John Doe",
        "slug": "my-first-blog-post",
        "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac justo nec urna tincidunt aliquam.",
        "posted_on": "06-06-2024"
    },
    {
        "title": "Python Tips and Tricks",
        "author": "Jane Smith",
        "slug": "python-tips-and-tricks",
        "body": "In this post, we'll explore some useful Python tricks for better code efficiency.",
        "posted_on": "10-05-2023"
    },
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html", posts=dummy_blog_data)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

if __name__ == '__main__':
    app.run(debug=True)

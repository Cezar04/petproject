from flask import Flask, render_template, url_for, flash, redirect, request
from forms import registration_form, login_form, post_form
import data_manager



app = Flask(__name__)

app.config['SECRET_KEY'] = 'haker'


posts = [
    {"author":"Gigel",
    "title": "blog post 1",
    "content":"First post content",
    "date_posted": "marite 200001"},
    {"author":"Gina gaina",
    "title": "blog post 2",
    "content":"First post content",
    "date_posted": "marite 202"}
]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    form = registration_form()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = login_form()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "1234":
            flash('You are logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash("Login failed, check username and password", 'danger')

    return render_template("login.html", title="Login", form=form)


@app.route('/post/new', methods=["GET", "POST"])
def new_post():
    form = post_form()
    if form.validate_on_submit():
        # post = posts(title=form.title.data, author=form.content.data, content=form.content.data)
        flash("Post Created", "success")
        return redirect(url_for("home"))
    return render_template("create_post.html", title="New Post", form=form)


if __name__ == "__main__":
    app.run(debug=True)

import json
from flask import Flask, render_template, request
from functions import load_data, get_all_posts_by_tag, search

all_posts, comments = load_data()

app = Flask(__name__)


@app.route("/")  # лента
def feed_page():
    return render_template("index.html", all_posts=all_posts)
    pass


@app.route("/posts/<int:post_id>")  # просмотр поста
def posts():
    return render_template("post.html")
    pass

@app.route("/tag/<tag>") # посты по тэгу
def page_tag(tag):
    tag = request.args.get("tag")
    posts_with_tags = get_all_posts_by_tag(tag)
    return render_template('tag.html', tag=tag, posts_with_tags=posts_with_tags)


@app.route("/search/<word>")  # поиск
def search(word):
    return render_template('search.html', all_posts=all_posts, posts_count=len(posts), posts=posts)


@app.route("/users/<username>")  # вывод по пользователю
def username_page(username):
    for post in posts:
        pass
        # if posts['poster_name'] ==

    return render_template('user-feed.html')

    # Выведите те посты у которых poster name соответствует username из запроса.
    # Используйте шаблон user-feed


app.run()

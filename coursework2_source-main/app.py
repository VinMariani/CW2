import json
from flask import Flask, render_template, request
from functions import load_data, get_all_posts_by_tag, search_for_posts, get_post_by_pk, user_page

all_posts, comments = load_data()

app = Flask(__name__)


@app.route("/")  # лента
def feed_page():
    return render_template("index.html", all_posts=all_posts)
    pass


@app.route("/posts/<int:post_pk>")  # просмотр поста по его номеру
def page_post(post_pk):
    post = get_post_by_pk(all_posts, post_pk)
    return render_template("post.html", post=post)


@app.route("/tag/<tag>")  # посты по тэгу
def page_tag(tag):
    posts = get_all_posts_by_tag(all_posts, tag)
    return render_template('tag.html', tag=tag, posts=posts)


@app.route("/search/")  # поиск поста
def page_search():
    word = request.args.get('word')
    if word:
        posts = search_for_posts(all_posts, word)
    else:
        posts = all_posts
    return render_template('search.html', posts=posts, posts_count=len(posts))


@app.route("/users/<username>")  # вывод по пользователю
def username_page(username):
    posts = user_page(all_posts, username)
    return render_template('user-feed.html', posts=posts, username=username)


app.run()

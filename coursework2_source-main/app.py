import json
from flask import Flask, render_template, request
from functions import load_data, add_comments_to_posts, tags

posts, comments, bookmarks = load_data()

app = Flask(__name__)

@app.route("/")                  #лента
def user_page():
    return render_template("index.html", posts=posts)

@app.route("/posts/<int:post_id>") #просмотр поста
def posts():
    pass

@app.route("/search/") #поиск
def search():
    post = request.args.get('content')
    with open('data/posts.json', encoding="utf-8") as f:
        user_post = json.load(f)
    posts = []
    count = len(posts)
    for post in posts:
        if post in posts['content']:
            posts.append(post['content'])
    return render_template('search.html', post=post, user_post=user_post, count=len(posts))
    # В нем должно отображаться 10 постов, если есть.
    # Поиск должен выполняться по вхождению ключевого слово в текст поста.
    # Регистрозависимость на ваше усмотрение. Найдите и используйте подходящий шаблон для вывода результатов.


@app.route("/users/<username>") #вывод по пользователю
def post():
    pass
    # Выведите те посты у которых poster name соответствует username из запроса.
    # Используйте шаблон user-feed


app.run()
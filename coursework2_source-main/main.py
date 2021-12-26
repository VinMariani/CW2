from flask import Flask, render_template, request, Response
from defs import load_data

posts, comments, bookmarks = load_data()

app = Flask(__name__)

@app.route("/")
def user_page():
    return render_template("index.html", posts=posts)

@app.route("posts/<postid")
def post():
    pass
    #Получите комментарии из файла `comments.json`, у которых соответствующий `postid`.
    #Выведите комментарии к посту.

@app.route("search/s=...")
def search():
    pass
    #В нем должно отображаться 10 постов, если есть.
    #Поиск должен выполняться по вхождению ключевого слово в текст поста.
    #Регистрозависимость на ваше усмотрение. Найдите и используйте подходящий шаблон для вывода результатов.


@app.route("/users/<username>")
def post():
    pass
    #Выведите те посты у которых poster name соответствует username из запроса.
    #Используйте шаблон user-feed

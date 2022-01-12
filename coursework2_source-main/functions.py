import json
import pprint


def load_data():
    '''читаем файлы json'''
    with open("data/posts.json", "r", encoding='utf-8') as fp:
        all_posts = json.load(fp)

    with open("data/comments.json", "r", encoding='utf-8') as fp:
        comments = json.load(fp)

    all_posts = combine_posts(comments, all_posts)

    return all_posts, comments


def combine_posts(comments, all_posts):
    '''добавляем комментарии и тэги к посту'''
    for i, post in enumerate(all_posts):
        pk = post.get("pk")
        post_comments = []
        for comment in comments:
            if comment.get("post_id") == pk:
                post_comments.append(comment)
        all_posts[i]["comments"] = post_comments  # добавляем комментарии к постам
        all_posts[i]["comments_count"] = len(post_comments)  # добавляем счетчик комментариев к постам
        all_posts[i]["content"] = tags_in_posts(all_posts[i]["content"])  # пост с тэгами

    return all_posts


def tags_in_posts(content):
    '''ищем тэги в тексте поста'''
    words = content.split(" ")
    for i, word in enumerate(words):
        if word.startswith("#"):
            tag = word.replace("#", "")
            link = f"<a href='/tag/{tag}'>{word}</a>"
            words[i] = link

    return " ".join(words)


def get_all_posts_by_tag(all_posts, tag):
    '''получаем все посты по тэгу'''
    results = []
    for post in all_posts:
        if f'#{tag}' in post['content']:
            results.append(post)
    return results


def search_for_posts(all_posts, word):
    '''поиск постов по слову'''
    posts = []
    for post in all_posts:
        if word in post['content']:
            posts.append(post)
    return posts


def get_post_by_pk(all_posts, pk):
    for post in all_posts:
        if post['pk'] == pk:
            return post


def user_page(all_posts, username):
    '''все посты пользователя'''
    posts = []
    for post in all_posts:
        if post['poster_name'] == username:
            posts.append(post)
    return posts

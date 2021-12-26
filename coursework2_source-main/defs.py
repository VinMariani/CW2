import json
from pprint import pprint


def load_data():
    with open("data/posts.json", "r", encoding='utf-8') as fp:
        posts = json.load(fp)

    with open("data/comments.json", "r", encoding='utf-8') as fp:
        comments = json.load(fp)

    posts = add_comments_to_posts(comments, posts)

    with open("data/bookmarks.json", "r", encoding='utf-8') as fp:
        bookmarks = json.load(fp)

    return posts, comments, bookmarks


def add_comments_to_posts(comments, posts):
    for i, post in enumerate(posts):
        pk = post.get("pk")
        post_comments = []
        for comment in comments:
            if comment.get("post_id") == pk:
                post_comments.append(comment)
        posts[i]["comment_count"] = len(post_comments)

        posts[i]['content'] = tags(posts[i]['content'])

    return posts


def tags(content):
    words = content.split(" ")
    for i, word in enumerate(words):
        if word.startswith("#"):
            tag = word.replace("#", "")
            link = f"<a href='/tag/{tag}'>{word}</a>"
            words[i] = link

    return " ".join(words)


pprint(tags("#еда #закат"))

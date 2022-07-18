from flask import render_template, request, Blueprint
from flaskblog.models import Post
from flaskblog.users.utils import get_picture

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    presigned_urls = {}
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc())
    
    for post in posts:
        if(post.userid not in presigned_urls.keys()):
            presigned_url = get_picture(post.author.image_file)
            presigned_urls[post.userid] = presigned_url

    post_paginate = posts.paginate(page=page, per_page=4)

    return render_template('home.html', posts=post_paginate, presigned_urls=presigned_urls)

@main.route('/about')
def about():
    return render_template('about.html', title='About')

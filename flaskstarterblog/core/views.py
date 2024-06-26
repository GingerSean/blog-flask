from flaskstarterblog.models import BlogPost
from flask import render_template , Blueprint, request

core = Blueprint( 'core'  ,  __name__)

@core.route('/')
def index():
        page = request.args.get('page' , 1 , type=int)
        blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page , per_page = 9)

        return render_template('index.html' , blog_posts=blog_posts)

@core.route('/about')
def about():
        return render_template('about.html')



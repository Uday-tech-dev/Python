from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def home():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('new.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        os.makedirs('templates', exist_ok=True)
        with open('templates/index.html', 'w') as f:
            f.write("""<!DOCTYPE html>
<html>
<head>
    <title>Daily Posts</title>
</head>
<body>
    <h1>Daily Posts</h1>
    <a href='/new'>Add New Post</a>
    <ul>
        {% for post in posts %}
        <li>
            <h2>{{ post.title }}</h2>
            <p>{{ post.content }}</p>
            <small>Posted on {{ post.date_posted.strftime('%Y-%m-%d %H:%M') }}</small>
        </li>
        {% endfor %}
    </ul>
</body>
</html>""")
        with open('templates/new.html', 'w') as f:
            f.write("""<!DOCTYPE html>
<html>
<head>
    <title>New Post</title>
</head>
<body>
    <h1>Create a New Post</h1>
    <form method='POST'>
        <label>Title:</label><br>
        <input type='text' name='title' required><br>
        <label>Content:</label><br>
        <textarea name='content' required></textarea><br>
        <button type='submit'>Post</button>
    </form>
    <a href='/'>Back to Home</a>
</body>
</html>""")
    app.run(debug=True)

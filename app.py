from flask import Flask, render_template, url_for
app = Flask(__name__)

app.config['SECRET_KEY'] = '210a117f56e7b716bf75c34703fd897f'

posts = [
    {
        'author': 'Dhoni Pramudito',
        'title': 'Your Flask App',
        'content': 'Is this your portfolio?',
        'date_posted': 'May 6, 2020'
    },
    {
        'author': 'Mac Win Lin',
        'title': 'Who cares?',
        'content': 'Make it legit my friend',
        'date_posted': 'May 7, 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
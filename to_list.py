from flask import Flask, render_template, request, redirect, url_for
# from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'patkar'
# app.config['MYSQL_HOST'] = 'list'   ## Also try to create a database

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Burhanuddin/Study/TyBscit/Sem5/AI practical/FlaskList/todo.db'


db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)

@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('list.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = Todo(text=request.form['todoitem'], complete=False)
    db.session.add(todo)
    db.session.commit()

    # return '<h1>{}</h1>'.format(request.form['todoitem'])
    return redirect(url_for('index'))

@app.route('/upload', methods=['POST','GET'])
def update():
    if request.method == 'POST':
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)


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
    incomplete = Todo.query.filter_by(complete=False).all()
    complete = Todo.query.filter_by(complete=True).all()
    return render_template('list.html', incomplete=incomplete, complete=complete )

@app.route('/add', methods=['POST'])
def add():  # create
    todo = Todo(text=request.form['todoitem'], complete=False)
    db.session.add(todo)
    db.session.commit()

    # return '<h1>{}</h1>'.format(request.form['todoitem'])
    return redirect(url_for('index'))

@app.route('/upload', methods=['POST','GET'])
def update(): # update
    complete = Todo.query.filter_by(complete=True).all()
    return render_template('upload.html', todos=complete)

@app.route('/delete/<id>')
def delete(id): # delete
    todo = Todo.query.filter_by(id=int(id)).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete/<id>')
def complete(id):
    # return f"<h1>{id}</h1>"
    todo = Todo.query.filter_by(id=int(id)).first()
    if todo.complete == True:
        todo.complete =False
    else:
        todo.complete = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_all')
def delete_all():
    todos = Todo.query.all()
    for todo in todos:
        db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('update'))

if __name__ == '__main__':
    app.run(debug=True)


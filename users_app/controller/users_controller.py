from flask import render_template, request, redirect
from users_app import app
from users_app.models.users import User


@app.route('/')
def index():
    users = User.muestra_usuarios()
    return render_template("index.html", users=users)

@app.route('/new')
def new():
    return render_template("new.html")

@app.route('/create', methods=['POST'])
def create():
    User.guardar(request.form)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id":id
    }

    User.borrar(data)
    return redirect('/')
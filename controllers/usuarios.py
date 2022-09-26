from flask import render_template,redirect,request
from models.usuario import User
from __init__ import app

@app.route('/create_user',methods=['POST'])
def create_user():
    # primero hacemos un diccionario de datos a partir de nuestro request.form proveniente de la plantilla
    # las claves en los datos tienen que alinearse exactamente con las variables en la cadena de consulta
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    # pasamos el diccionario de datos al metodo save de la clase Friend
    User.save(data)
    # no olvides redirigir despues de guardar en la base de datos
    return redirect('/show')

@app.route('/show')
def show():
    # llamar al método de clase get all para obtener todos los amigos
    users = User.get_all()
    return render_template('show.html',users=users)

@app.route('/user/<int:id>')
def user_info(id):
    data = {
        "id": id
    }
    user = User.get_user_by_id(data)
    return render_template('user_info.html',user=user)

@app.route('/user/<int:id>/edit')
def edit(id):
    data = {
        "id": id
    }
    actual_info = User.get_user_by_id(data)
    # if statement to get errors
    return render_template('user_edit.html',actual_info=actual_info)

@app.route('/editing/user/<int:id>',methods=['POST'])
def editing(id):
    data = {
        "id": id,
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email'],
    }
    User.edit_user_by_id(data)
    return render_template('edit_end.html',id=id)

@app.route('/user/<int:id>/delete')
def deleting(id):
    data = {
        "id": id
    }
    User.delete_user_by_id(data)
    return render_template('delete_end.html',id=id)
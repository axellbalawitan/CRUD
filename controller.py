from flask import Flask, render_template, redirect, request, session
from model import Users #from model.py we wil bring the value to controller.py it means from model import class Users
app = Flask(__name__)
app.secret_key = "crud"


@app.route('/users')
def users():
    user = Users.all_users()    #all_users from model.py
    return render_template("user.html",all_user = user)

@app.route('/add_user', methods=['POST']) # retrieving data from user.html
def add_user():

    data = {
        "name" : request.form["txt-name"],  
        "email" : request.form["txt-email"],
        "password" : request.form["txt-pword"]
    }
    Users.add_users(data) # if the route works,the (data) will go to model.py
    return redirect ('/users')

@app.route('/delete_user/<user_id>')
def delete_user(user_id):
    
    data = {
        "id" : user_id
    }
    Users.delete_users(data) # we need to call the delete_user from model.py
    return redirect('/users')

#code below is for update app.route should be two since it's for retrieval and for update

@app.route('/retrieve_user/<user_id>') 
def retrieve_user(user_id):
    data = {
        "id" : user_id
    }
    session['id'] = user_id
    user = Users.retrieve_user(data)  #We need to call retrieve_user from model.py
    return render_template('update.html', all_users = user)

@app.route('/update_user', methods=['POST']) # retrieving data from update.html
def update_user():

    data = {
        "id" : session['id'],
        "name" : request.form["txt-name"],  
        "email" : request.form["txt-email"],
        "password" : request.form["txt-pword"]
    }
    Users.update_users(data) # if the route works,the (data) will go to model.py
    return redirect ('/users')

if __name__ == "__main__":
    app.run(debug=True)
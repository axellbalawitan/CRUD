from flask import render_template,redirect,request, session
from flask_app.model.users import Users
from flask_app import app



@app.route('/users')
def users():
    user = Users.all_users()
    return render_template ("add_user.html", all_users = user)


@app.route('/add_user')
def add_user(): 
    return render_template("new_user.html")

@app.route('/new_user', methods=['POST'])
def new_user():
    if not Users.validate_user(request.form):
        return redirect ('/add_user')  #this is the validation part, if it doesn't have an error and meets the requirements in the static method, the code below will execute

    data = {
        "first_name" : request.form["txt-firstname"],  
        "last_name" : request.form["txt-lastname"],
        "email" : request.form["txt-email"]
        }
    Users.add_users(data)
    return redirect ('/users')


@app.route('/delete_user/<user_id>')
def delete_user(user_id):
    
    data = {
        "id" : user_id
    }
    Users.delete_users(data) 
    return redirect('/users')



@app.route('/edit_user/<user_id>') #this route retrieves data from users.py
def retrieve_user(user_id):
    data = {
        "id" : user_id
    }
    session['id'] = user_id
    user = Users.retrieve_user(data)  
    return render_template("update2.html", all_users = user)


@app.route('/update_user', methods=['POST'])
def update_user():

    data = {
        "id" : session['id'],
        "first_name" : request.form["txt-firstname"],  
        "last_name" : request.form["txt-lastname"],
        "email" : request.form["txt-email"]
    }
    Users.update_users(data)
    return redirect ('/users')


@app.route('/show_user/<user_id>') # this code shows that the ID that was called in showuser.html 
def show_user(user_id): #user ID in showuser.html will be transferred here
    data = {
        "id" : user_id # and then here
    }
    return render_template ("showuser.html", all_users = Users.show_user(data)) 
    # so the data here which is the id from above code it transaltes to User.show_user(id) meaning it will look for the id in Users.show_user
   



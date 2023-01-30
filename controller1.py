from flask import Flask, render_template,redirect,request, session
from model1 import Users
app = Flask(__name__)
app.secret_key = "crud"


@app.route('/users')
def users():
    user = Users.all_users()
    return render_template ("add_user.html", all_users = user)


@app.route('/add_user')
def add_user():
    return render_template("new_user.html")

@app.route('/new_user', methods=['POST'])
def new_user():

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



@app.route('/edit_user/<user_id>')
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


if __name__ == "__main__":
    app.run(debug=True)
#retrieving all the values in the database

from flask import Flask
from mysqlconnection import connectToMySQL # connecting mysqlconnection to model.py

class Users: #to fetch data from database
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at'] #all of these are the parameters

    @classmethod # relationship with attributes / method that allows you to fetch value from database table to backend and frontend
    def all_users(cls):
        query = "SELECT * FROM users;" #fetch from databese
        results = connectToMySQL("sample_db1").query_db(query) # use to connect to MySQL database called "sample_db1" and execute the query that was in line (query = "SELECT * FROM users;)
        posts = [] #all of the values that has been retrieve in the database should be put here
        for post in results: #insert it to the posts list using the append medthod below / We also need for loop so we can retrieve everything in the parameter
            posts.append(cls(post)) #append using the cls(post) method / cls is the parameter above/ in short, cls (post) is calling the parameter above
        return posts
        # the code above is the query for retrieving the value from the database

        #Next step is to bring to the backend ( you need to create another py for this, "controller.py")

    @classmethod # We will now be retrieving data from controller.py
    def add_users(cls, data):
        query = "INSERT INTO users (name, email, password, created_at, updated_at) VALUES( %(name)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL("sample_db1").query_db(query, data) # from the user.html the data that we fetch then will go to controller.py and then will go to the database
        
    @classmethod # This is the delete callmethod function
    def delete_users(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        print(query)
        return connectToMySQL("sample_db1").query_db(query, data)

    
    @classmethod # for retrieval in update function
    def retrieve_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        return connectToMySQL("sample_db1").query_db(query, data)
        if len(results) < 1 :
            return  False
        return cls(results[0])

    @classmethod # We will now be retrieving data from controller.py
    def update_users(cls, data):
        query = "UPDATE users SET name = %(name)s, email = %(email)s, password = %(password)s, updated_at = NOW() WHERE id = %(id)s ;"
        return connectToMySQL("sample_db1").query_db(query, data)

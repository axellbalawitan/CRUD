from flask import Flask
from flask_app.config.mysqlconnection1 import connectToMySQL

class Users:
    def __init__(self, data):
        self.id = data ['id']
        self.first_name = data ['first_name']
        self.last_name = data ['last_name']
        self.email = data ['email']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']

    @classmethod # relationship with attributes / method that allows you to fetch value from database table to backend and frontend
    def all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("add_userdb").query_db(query) 
        posts = []
        for post in results:
            posts.append(cls(post))
        return posts


    @classmethod 
    def add_users(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES( %(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
        print(query)
        return connectToMySQL("add_userdb").query_db(query, data)


    @classmethod # This is the delete callmethod function
    def delete_users(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        print(query)
        return connectToMySQL("add_userdb").query_db(query, data)

    @classmethod # for retrieval in update function
    def retrieve_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        return connectToMySQL("add_userdb").query_db(query, data)
        if len(results) < 1 :
            return  False
        return cls(results[0])

    
    @classmethod # We will now be retrieving data from controller.py
    def update_users(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s ;"
        return connectToMySQL("add_userdb").query_db(query, data)

    @classmethod
    def show_user(cls,data):
        query  = "SELECT * FROM users WHERE id = %(id)s"; #this query will look for the ID
        result = connectToMySQL("add_userdb").query_db(query,data)
        return cls(result[0])
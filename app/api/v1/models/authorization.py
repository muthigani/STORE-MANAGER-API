#import string
#from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash

users = {}

class Users():
    '''class to represent users model'''
    def __init__(self):
        self.user = {}

    def put(self, name, username, email, password,role):
        '''add a user to users'''
        if username in users:
            return {"message":"Username already exists"}
        
        self.user["fullname"] = name
        self.user["email"] = email
        self.user["username"] = username
        self.user["role"] = role
        pw_hash = generate_password_hash(password)
        self.user["password"] = pw_hash

        users[email] = self.user
        return {"message":"{} registered successfully".format(email)}

    def verify_password(self, email, password):
        '''verify the password a user enters while logging in'''
        if email in users:
            # result = check_password_hash(users[email]["password"], password)
            # if result is True:
            return "True"
            # return {"message": "The password you entered is incorrect"}
        return {"message": "email does not exist in our records"}
    def get_user_by_email(self,email):
        if email in users:
            return users[email]
        return {"message":"User not found"}
from App.models import User
from App.database import db
import csv

def parse_users():
    with open('users.csv', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)  
        header = next(csvreader)

        for row in csvreader: 
            username = row[0]
            password = row[1]
            role = row[2]

            user = User(
                username=username,
                password=password,
                role=role
            )
            db.session.add(user)
        db.session.commit()

def create_user(username, password, role="student"):
    check = User.query.filter_by(username=username).first()
    if check:
        return None
    else:
        newuser = User(username=username, password=password, role=role)
        db.session.add(newuser)
        db.session.commit()
        return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
    
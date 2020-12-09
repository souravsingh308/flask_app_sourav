from flask import Flask, request
import re
import mysql.connector as sql
from usernames import is_safe_username
import datetime

app = Flask(__name__)

mycursor = mydb.cursor()
@app.route('/signin', methods=['POST'])
def Signin():
    int_features = request.get_json()
    username = int_features["username"]
    email = int_features["email"]
    user_password = int_features["user_password"]
    current_date = int_features["current_date"]
    is_valid_username = is_safe_username(username)
    if is_valid_username == True:
        valid_password = is_valid_password(user_password)
    else:
        res = "please enter a valid username"
        return res
    if valid_password == True:
        valid_date = is_valid_date(current_date)
    else:
        res = "please enter a valid Password"
        return res
    is_valid_date(current_date)
    if valid_date == True:
        is_valid_email_2 = is_valid_email(email)
    else:
        res = "please enter a valid date. 'format YYYY-MM-DD'"
        return res
    if is_valid_email_2 == True:
        res = "you have successfully logged in"
        sql = "INSERT INTO flask_app.user (user_name, user_password, email_id, date_of_birth) VALUES (%s, %s, %s, %s)"
        val = (username, user_password, email, current_date)
        mycursor.execute(sql, val)
        mydb.commit()
        return res
    else:
        res = "please enter a valid email"
        return res


def is_valid_password(user_password):
    password = user_password
    while True:
        if (len(password) < 8):
            flag = -1
            break
        elif not re.search("[a-z]", password):
            flag = -1
            break
        elif not re.search("[A-Z]", password):
            flag = -1
            break
        elif not re.search("[0-9]", password):
            flag = -1
            break
        elif not re.search("[_@$]", password):
            flag = -1
            break
        else:
            flag = 0
            return True
            break

    if flag == -1:
        return False

def is_valid_date(current_date):
    date_string = current_date
    date_format = '%Y-%m-%d'
    try:
        date_obj = datetime.datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False

def is_valid_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        return True
    else:
        return False

if __name__ == "__main__":
    app.run(debug=True)

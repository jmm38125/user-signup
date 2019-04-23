from flask import Flask, request, redirect, render_template
import cgi


app = Flask(__name__)

app.config['DEBUG'] = True 


@app.route("/register", methods=['POST','GET'])
def register():
    username = cgi.escape(request.form['username_render'])
    password = cgi.escape(request.form['password_render'])
    password2 = cgi.escape(request.form['password2_render'])
    email = cgi.escape(request.form['email_render'])

    username_error = ""
    password_error = ""
    password2_error = ""
    email_error = ""

    if not username:
        username_error = "A username is required"
    elif len(username) < 3 or len(username) > 20:
        username_error = "Username must be at least 3 and less than 20 characters long"
    else:
        has_space = False
        for char in username:
            if char.isspace():
                has_space = True
            if  has_space:       
                username_error = "Username cannot contain any spaces"
    if not password:
        password_error = "A password is required" 
    elif len(password) < 3 or len(password) > 20:
        password_error = "Password must be at least 3 and less than 20 characters long"
    else:
        has_space = False
        for char in password:
            if char.isspace():
                has_space = True
            if  has_space:       
                password_error = "Password cannot contain any spaces"
    if password != password2:
        password2_error = "Passwords must match"
    if email:
        if len(email) < 3 or len(email) > 20:
            email_error = "Username must be at least 3 and less than 20 characters long"
        count1 = 0
        count2 = 0
        for char in email:
            if char is '@':
                count1 = count1 + 1
            elif char is '.':
                count2 = count2 + 1
        if count1 >  1 or count1 == 0 or count2 == 0:
            email_error = "That is not a valid email"
        else:
            has_space = False
            for char in email:
                if char.isspace():
                    has_space = True
                if  has_space:       
                    email_error = "Email cannot contain any spaces"
    if username_error or password_error or password2_error or email_error:
        return render_template('index.html', username_render = username, username_error_render = username_error,
        password_render = "", password_error_render = password_error, password2_render = "", password2_error_render = password2_error, email_render = email, email_error_render = email_error)
    return render_template('welcome.html', username_render = username)

@app.route("/")
def index():
    return render_template('index.html', username_render = "", username_error_render = "", password_render = "", password_error_render = "", password2_render = "", password2_error_render = "", email_render = "", email_error_render = "")


app.run()
from flask import Flask, request
app = Flask(__name__)

saved_logins = {
}

@app.route('/register/', methods=['POST'])
def register():
    request_data = request.get_json()
    user_login = request_data['login']
    user_password = request_data['password']

    if user_login in saved_logins:
        return 'This user already exists!', 400

    saved_logins[user_login] = user_password
    
    return "Successfully registered"

@app.route('/login/', methods=['POST'])
def logging_in():
    request_data = request.get_json()
    user_login = request_data['login']
    user_password = request_data['password']

    if user_login not in saved_logins:
        return 'This user does not exist!', 404

    if user_password == saved_logins.get(user_login, None):
        return 'You\'re succesfully signed in!', 200
    
    return 'Wrong password!', 400

if __name__ == '__main__':
    app.run()

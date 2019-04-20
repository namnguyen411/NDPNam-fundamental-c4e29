from flask import *
app = Flask(__name__)
@app.route('/')
def index():
        return "Hello"
@app.route('/user')
def user():
        return "User"
users = {
        "huy": {
                "name":"Nguyen Quang Huy",
                "age": 29, 
                },
        "tuananh": {
                "name":"Huynh Tuan Anh", 
                "age": 22, 
                }
}

@app.route('/user/<user_name>')
def user_name(user_name):
    
    return render_template('profile.html', user_name = user_name, users = users)

if __name__ == '__main__':
  app.run(debug=True)
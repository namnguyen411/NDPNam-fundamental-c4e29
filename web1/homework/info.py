import os
from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello C4E29"

@app.route('/about-me')
def about_me():
        return render_template('info.html', about_me = about_me) 

@app.route('/school')
def school():
    return redirect("http://techkids.vn", code=302)

if __name__ == '__main__':
  app.run(debug=True)
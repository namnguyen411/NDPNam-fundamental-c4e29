from flask import Flask, render_template, request, redirect
from bike_database import bike_collection
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello C4E29"



@app.route('/bike')
def current_bike():
        bike = bike_collection.find()
        return render_template('bike.html', bike = bike)

@app.route('/new_bike', methods=['GET', 'POST'])
def new_bike():
        if request.method == 'GET':
                return render_template('rental.html')
        elif request.method == 'POST':
                form = request.form 
                new_bike = {
                        "model" : form['model'],
                        "fee": form['fee'],
                        "link": form['link'],
                        "year": form['year']
                }
                print(new_bike)
                bike_collection.insert_one(new_bike)
                return redirect("/bike", code = 302)

if __name__ == '__main__':
  app.run(debug=True)
 
from flask import *
app = Flask(__name__)
@app.route('/')

@app.route('/bmi')
def index():
        return "Hello"
def bmi():
    return "BMI"
@app.route('/bmi/<int:weight>')
def weight(weight):
    return "Your weight: {} kg". format(weight)

@app.route('/bmi/<int:weight>/<int:height>')
def height(weight,height):
        height_meter = (height)/100
        bmi = (weight)/(height_meter**2)
        # index = []
        # index.append(weight)
        # index.append(height)
        # return render_template("bmi.html", bmi = bmi, index = index)
        if bmi < 16:
                return "Severely underweight"
        elif bmi < 18.5:
                return "Underweight" 
        elif bmi < 25:
                return "Normal"
        elif bmi < 30:
                return "Overweight"
        else:
                return "Obese"

if __name__ == '__main__':
  app.run(debug=True)
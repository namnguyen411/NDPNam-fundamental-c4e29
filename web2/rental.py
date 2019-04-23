from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello C4E29"


bike = [
{
        "model" : "Honda SH",
        "fee" : "500000",
        "link" : "https://imgwebikevn-8743.kxcdn.com/58C4wYg8eEPyCW_2YlmSIoIfA6c=/product/2018/08/04/wvn.05b65182a13dc02.48439864.jpg",
        "year": 2009
},
{
        "model" : "Honda Spacy",
        "fee" : "300000",
        "link" : "https://image.anninhthudo.vn/w700/uploaded/caominh/2011_09_05/spacy.jpg",
        "year" : 2005
}
]

@app.route('/bike')
def current_bike():
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
                bike.append(new_bike)
                return redirect("/bike", code = 302)

if __name__ == '__main__':
  app.run(debug=True)
 
from flask import Flask, render_template, request
import requests
import csv

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def homepage():
    return render_template("index.html")

@app.route("/index.html", methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route('/create.html', methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template('create.html')
    elif request.method == "POST":
        result = []
        user_csv = request.form.get("data-input").split('\n')
        reader = csv.DictReader(user_csv)
        
        for row in reader:
            result.append(dict(row))
        return render_template('data.html', result=result)


@app.route("/data.html", methods=["GET", "POST"])
def data():
    result = []
    user_csv = open("static/dataset-1.csv")
    reader = csv.DictReader(user_csv)

    for row in reader:
        result.append(dict(row))
    return render_template('data.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
import csv
import pandas as pd

app = Flask(__name__)

### THE DEFAULT HOMEPAGE ###

@app.route("/", methods=['GET', 'POST'])
def homepage():
    return render_template("index.html")

### REDIRECT WHEN HOME IS CLICKED ON NAV ###

@app.route("/index.html", methods=['GET', 'POST'])
def home():
    return render_template("index.html")

### CREATE CSV ###

@app.route('/create.html', methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template('create.html')
    elif request.method == "POST":
        try:
            result = []
            user_csv = request.form.get("data-input").split('\n')
            reader = csv.DictReader(user_csv)

            for row in reader:
                result.append(dict(row))
            return render_template('data.html', result=result)

        ### CREATING AN ERROR PAGE IF CSV DATA NOT ENTERED ###

        except:
            return render_template('error-404.html')

### A PAGE THAT EDITS THE DATASET ###

@app.route('/edit-data.html', methods= ["GET", "POST"])
def edit():
    ### OLD DATASET ###
    result = []
    user_csv = open("static/dataset-1.csv")
    reader = csv.DictReader(user_csv)

    for row in reader:
        result.append(dict(row))

    ### NEW DATASET WITH OLD TABLE HEADS IN COLUMN 1 ###
    df = pd.DataFrame(result)
    column_names = df.columns
    new_df = pd.DataFrame(data=column_names, columns=['Column Names'])
    new_df['Include'] = ""

    result = []
    edit_csv = open('static/edit-col.csv')
    reader = csv.DictReader(edit_csv)

    for row in reader:
        result.append(dict(row))
    return render_template('edit-data.html', result=result)

### MAIN DATAPAGE ###

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
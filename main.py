from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score >50:
        res = "Pass"
    else:
        res = "Fail"
    return render_template('result.html', result=res)

@app.route('/fail/<int:score>')
def fail(score):
    return f"The student has failed with a score of {score}"


@app.route('/results/<int:marks>')
def results(marks):
    res=""
    if marks < 50:
        res="fail"
    else:
        res="success"
    return redirect(url_for(res, score=marks))

#Result checker html page
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        Science=float(request.form['Science'])
        Maths = float(request.form['Maths'])
        C = float(request.form['C'])
        data_science = float(request.form['Data Science'])
        total_score = (Science + Maths + C + data_science)/4

    res = ""
    if total_score >=50:
        res="success"
    else:
        res="fail"
    
    return redirect(url_for(res, score=total_score))

if __name__ == "__main__":
    app.run(debug=True)
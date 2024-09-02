from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/check/<int:score>')
def check(score):
    res=""
    if score>=60:
        res="Pass"
    else:
        res="Fail"
    out={'Score': score, 'Result': res}
    return render_template('result.html', result=out)

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

    return redirect(url_for('check', score=total_score))

if __name__ == "__main__":
    app.run(debug=True)
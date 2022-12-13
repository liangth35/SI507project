from flask import Flask, render_template
import time
app = Flask(__name__)

course = 'SI 507'
semester = 'Fall 2020'
month="October"
day=31
@app.route('/')
def about():
    return render_template('index.html',course=course, semester=semester, month=month, day=day)

if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(host= '127.0.0.1', port=5001, debug=True)
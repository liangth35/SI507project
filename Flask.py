from flask import Flask, render_template, request
import time
app = Flask(__name__)

querytype = None
month="October"
day=31
@app.route('/')
def about():
    return render_template('index.html', querytype=querytype, month=month, day=day)

@app.route('/handle', methods=["POST"])
def handle():
    querytype = request.form["query"]
    return render_template('index.html', querytype=querytype, month=month, day=day)

if __name__ == '__main__':  
    print('starting Flask app', app.name)
    app.run(host= '127.0.0.1', port=5001, debug=True)
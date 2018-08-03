from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'whatdoyouwant'

@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else: 
        session['count'] = 0
    return render_template('index.html', **session)

@app.route('/track')
def addtwo():
    session['count'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
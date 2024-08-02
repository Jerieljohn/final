from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('hhh.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/view_events')
def view_events():
    return render_template('view_events.html')

@app.route('/manage_events')
def manage_events():
    return render_template('manage_events.html')

if __name__ == '__app__':
    app.run(debug=True)

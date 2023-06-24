from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/add_transaction')
def add_transaction():
    return render_template('add_transaction.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/view_transactions')
def view_transactions():
    return render_template('view_transactions.html')

if __name__ == '__main__':
    app.run()

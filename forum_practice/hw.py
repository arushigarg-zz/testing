from flask import *
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/welcome')
def profile():
    return render_template('welcome.html')
	
@app.route('/hello')
def hello():
    return render_template('hello.html')
	
@app.route('/log',methods=['GET','POST'])
def log():
        error = None
        if request.method == 'POST':
            if request.form['user'] != 'admin' or request.form['pass'] != 'pass':
                error = "Invalid Credentials entered !!"
            else:
                return redirect(url_for('hello'))	
        return render_template('log.html',error=error)		
if __name__ == "__main__":
    app.run(debug=True)	
	
	
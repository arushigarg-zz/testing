from flask import Flask, render_template

app = Flask(__name__)
#created a new instance of the Flask class

@app.route("/")
#mapthe URL / to the function home(). Now, when someone visits this URL, the function home() will execute.

def home():
    return render_template('home.html')
#render the home.html template just created from the templates/ folder to the browser.	

if __name__ == "__main__":
    app.run(debug=True)
#we use run() to run our app on a local server. We'll set the debug flag to true, so we can view any applicable error 
#messages if something goes wrong, and so that the local server automatically reloads after we've made changes to the code.
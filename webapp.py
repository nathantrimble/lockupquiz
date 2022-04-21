import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)
app.secret_key=os.environ["SECRET_KEY"];

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect('/') # url_for('renderMain') could be replaced with '/'

@app.route('/page1',methods=['GET','POST'])
def renderPage1():
    session["q1"]=request.form['q1']
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    session["q2"]=request.form['q2']
    return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    session["q3"]=request.form['q3']
    return render_template('page3.html')



if __name__=="__main__":
    app.run(debug=False)

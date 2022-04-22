import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)
app.secret_key=os.environ["SECRET_KEY"];

answers= ["HTML","JavaScript","CSS"]
correct1 = False
correct2 = False
correct3 = False

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

    if session['q1']==answers[0]:
        correct1 == True
    else:
        correct1 == False
    return render_template('page1.html', c1 = correct1)

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    session["q2"]=request.form['q2']

    if session['q2']==answers[1]:
        correct2 == True
    else:
        correct2 == False
    return render_template('page2.html', c2 = correct2)

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    session["q3"]=request.form['q3']
    if session['q3']==answers[2]:
        correct3 == True
    else:
        correct3 == False
    return render_template('page3.html', c3 = correct3)



if __name__=="__main__":
    app.run(debug=True)

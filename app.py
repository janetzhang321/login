#Janet Zhang
#Pd 6 SoftDev DW

from flask import Flask, render_template, request, url_for, session, redirect
from utils import register
import cgi

app= Flask(__name__)
app.secret_key = "g?\x01l\x1e\xf7\xb6\xdc\x0b:\x83\xf9O\x92\xeb\xcc\xd7\x02Z+\xd4uWM\x06'\x94\xbei\xf5\xeb\xda"


@app.route("/")
@app.route("/home/", methods = ['POST'])
def home() : 
	#python eqiv of toString, printing an object
	#User-Agent gives you the info the connection is coming from
    if request.method == 'POST':
		session.pop(user,None)
		print "name: " + request.form['button']
		return render_template('form.html', title="submit form")
    elif request.method == 'GET':
		return render_template('form.html', title="submit form")

@app.route('/getsession/')
def getsession() :
	if 'user' in session:
		return session['user']
	return 'not logged in'

@app.route('/dropsession/')
def dropsession() :
	session.pop('user',None)
	return 'Dropped!'


@app.route("/auth/", methods = ['GET'])
def auth() :
	if 'user' in session:
		#didn't know how to access form info form login page to auth so I hardcoded the output
		return render_template( 'auth.html', name=session['user'], output="successfully logged in" )
		
	else:
		return render_template( 'form.html', title="account" )

@app.route("/login/", methods = ['POST', 'GET'])
def login() :
	print "name from login: " + request.form['button']
	#register does not create session
	if request.form['button'] == "register":
		if register.addUser(request.form['user'],request.form['pass']) == "account created!":
			return render_template( 'form.html', title="account", output="account created!", name=request.form['user']  )
		else: 
			#register fails
			return render_template( 'form.html', title="account", output=register.addUser(request.form['user'],request.form['pass']) )
	#login creates session if correct
	elif request.form['button'] == "login":
		if register.login(request.form['user'],request.form['pass']) == "successfully logged in":
			#create a session
			session['user']=request.form['user']
			return redirect(url_for("auth"))
		else:
			#login fails
			return render_template( 'form.html', output=register.login(request.form['user'],request.form['pass']) )
		
	#regular login page
	return render_template( 'form.html', title="account" )


if __name__ == "__main__": 
	app.debug = True
	app.run()



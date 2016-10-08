#Janet Zhang
#Pd 6 SoftDev DW

from flask import Flask, render_template, request, url_for
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
			print "name: " + request.form['button']
			return render_template('form.html', title="submit form")
    elif request.method == 'GET':
      return render_template('form.html', title="submit form")




@app.route("/auth/", methods = ['POST'])
def auth() :
	print "name from auth: " + request.form['button']
	if request.form['button'] == "login":
		if register.login(request.form['user'],request.form['pass']) == "successfully logged in":
			print request.form['user']
			return render_template( 'auth.html', output=register.login(request.form['user'],request.form['pass']), name=request.form['user'] )
		else:
			return render_template( 'form.html', outputput=register.login(request.form['user'],request.form['pass']) )
	return render_template( 'form.html', title="account", output=register.addUser(request.form['user'],request.form['pass']) )


@app.route("/login/", methods = ['POST'])
def login() :
	print "name from login: " + request.form['button']
	print url_for("login")
	#the correct route of the function in your flask app
	print url_for("auth")

	if request.form['button'] == "register":
		print request.form['user']
		if register.addUser(request.form['user'],request.form['pass']) == "account created!":
			return render_template( 'auth.html', title="account", output="account created!", name=request.form['user']  )
		else: 
			return render_template( 'form.html', title="account", output=register.addUser(request.form['user'],request.form['pass']) )

	elif request.form['button'] == "login":
		if register.login(request.form['user'],request.form['pass']) == "successfully logged in":
			print request.form['user']
			return render_template( 'auth.html', output=register.login(request.form['user'],request.form['pass']), name=request.form['user'] )
		else:
			return render_template( 'form.html', output=register.login(request.form['user'],request.form['pass']) )
		
		
	return render_template( 'auth.html', title="account", output=register.login(request.form['user'],request.form['pass']), name=request.form['user'] )




if __name__ == "__main__": 
	app.debug = True
	app.run()



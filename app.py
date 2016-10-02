#Janet Zhang
#Pd 6 SoftDev DW

from flask import Flask, render_template, request
from utils import register
import cgi

app= Flask(__name__)

@app.route("/")
@app.route("/home/", methods = ['POST'])
def home() : 
	#python eqiv of toString, printing an object
	#User-Agent gives you the info the connection is coming from


	#print request.headers 
	#return render_template( 'form.html', foo="submit form")



    if request.method == 'POST':
        if request.form['button'] == 'login':
			print "login"
            #pass # do something
        elif request.form['button'] == 'register':
			print "register"
            #pass # do something else
        else:
			print "unknown"
            #pass # unknown
    elif request.method == 'GET':
        return render_template('form.html', foo="submit form")




@app.route("/auth/", methods = ['POST'])
def auth() :
	return render_template( 'form.html', foo="account", poo=register.addUser(request.form['user'],request.form['pass']) )


@app.route("/login/", methods = ['POST'])
def login() :
	return render_template( 'form.html', poo=register.login(request.form['user'],request.form['pass']) )




if __name__ == "__main__": 
	app.debug = True
	app.run()



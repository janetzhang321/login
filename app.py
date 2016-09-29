#Janet Zhang
#Pd 6 SoftDev DW

from flask import Flask, render_template, request

app= Flask(__name__)

@app.route("/")
@app.route("/login/")
def home() : 
	#python eqiv of toString, printing an object
	#User-Agent gives you the info the connection is coming from
	print request.headers 
	return render_template( 'form.html', foo="submit form")

@app.route("/authenticate/", methods = ['POST'])
def auth() :
	print request.headers 
	print request.form  
	print request.form['user']
	if request.form['user'] == "a" and request.form['pass'] == "a" : 
		return render_template( 'auth.html', poo="SUCCESS")
	else :
		return render_template( 'auth.html', poo="FAILURE")



if __name__ == "__main__": 
	app.debug = True
	app.run()



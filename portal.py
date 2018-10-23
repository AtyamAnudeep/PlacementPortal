from flask import Flask, render_template, request,redirect,url_for,flash
app = Flask(__name__)
app.secret_key = 'random string'

@app.route('/')
def student():
	return render_template('index.html')

@app.route('/login',methods=['POST', 'GET'])
def login():
	if request.method=='POST':
		result=request.form
		return render_template("login.html",result=result)

@app.route('/login/studentlogin',methods=['POST','GET'])
def studentlogin():
	if request.method=='POST':
		return render_template("studentlogin.html")

@app.route('/login/companylogin',methods=['POST','GET'])
def companylogin():
	if request.method=='POST':
		return render_template("companylogin.html")	

@app.route('/login/studentlogin/loggedIn',methods=['POST','GET'])
def studentlogged():
	if request.method=='POST':
		return render_template("SLoggedIn.html")

@app.route('/login/studentlogin/signing',methods=['POST','GET'])
def sSigning():
	if request.method=='POST':
		return render_template("sRegistration.html")	

@app.route('/login/companylogin/signing',methods=['POST','GET'])
def cSigning():
	if request.method=='POST':
		return render_template("cRegistration.html")

if __name__ == '__main__':
	app.run(debug=True)
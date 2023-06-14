from flask import Flask
app = Flask(__name__)


users = {
	"Agam": "manager",
	"Yuval": "manager",
	"Ido": "co-founder"
}	

@app.route("/")
def welcome():
	return "Hello, there! Welcome to my server\n"
	
@app.route("/<name>")
def authentication(name):
	if name not in users.keys():
		return "Hi %s, You are not allowed to use this server\n"%name
	return "Hi %s %s, You can do whatever you would like"%(users[name], name)



app.run(port=2017)

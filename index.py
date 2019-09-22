from flask import Flask,render_template,request
from pymongo import MongoClient

#commetnt

app=Flask(__name__)

client=MongoClient("mongodb+srv://Mayur:Mayur@123@cluster0-nv63c.mongodb.net/test?retryWrites=true&w=majority")
users=client["users"]
user_coll=["user_coll"]

person={
	"name":"mayur",
	"age":41
}
user_coll.insert_one(person)
@app.route("/")
def login():
	return render_template("login.html")

@app.route("/values",methods=["POST"])
def print():
	for value in request.form:
		data={}
		data[uname]=value
		password=request.form[value]
		print(data)
		return render_template("hello.html")
	
app.run()


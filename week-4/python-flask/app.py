from flask import render_template
from flask import Flask 
from flask import request
from flask import session
from flask import redirect

app=Flask(__name__) 
app.secret_key = b"69a2491c26617a5d867681ef213949901b11814b037789b8b311e0fb262d6414"

@app.route("/")
def index(): 
    return render_template("index.html")
    
@app.route("/signin", methods=["POST"])
def signin():
    account = request.form["account"]
    password = request.form["password"]

    if len(account) == 0 or len(password) == 0:
        return redirect("/error?message=請輸入帳號、密碼")
    else:
        if account == "test" and password == "test":
            session["status"] = "sign in"
            return redirect("/member")
        else:
            return redirect("/error?message=帳號、或密碼輸入錯誤")

@app.route("/member")
def member(): 
    if "status" not in session or session["status"] == "sign out":
        return redirect("/")
    return render_template("member.html")

@app.route("/error")
def error():
    message=request.args.get("message")
    return render_template("error.html", data=message)

@app.route("/signout")
def signout():
    session["status"] = "sign out"
    return redirect("/")

@app.route("/square", defaults={"number": None})
@app.route("/square/<int:number>")
def square(number):
    result = None
    if number is None:
        input_number=request.args.get("number")
        if len(input_number) == 0:
            result = "請輸入數字"
        else:
            result = pow(int(input_number), 2)        
    else:
        result = pow(number, 2)
    return render_template("square.html", data=result)

app.run(port=3000) 
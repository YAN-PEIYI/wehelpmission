from flask import render_template
from flask import Flask 
from flask import request
from flask import session
from flask import redirect
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost", 
  user="root",
  passwd="",
  database="website"
)

app=Flask(__name__) 
app.secret_key = b"69a2491c26617a5d867681ef213949901b11814b037789b8b311e0fb262d6414"

@app.route("/")
def index(): 
    return render_template("index.html")

@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    account = request.form["account"]
    password = request.form["password"]
    if len(name) == 0 or len(account) == 0 or len(password) == 0:
        return redirect("/error?message=姓名、帳號與密碼不可為空白，請再檢查一次&title=登入失敗&signout=重新登入")
    else:   
        mycursor = mydb.cursor()
        sql = "SELECT * FROM member WHERE username = %s"
        params = (account,)
        mycursor.execute(sql, params)
        myresult = mycursor.fetchall()

        if len(myresult) == 0:
            insert_sql = "INSERT INTO member(name, username, password, follower_count) VALUES(%s, %s, %s, %s)"
            insert_params = (name, account, password, 0)
            mycursor.execute(insert_sql, insert_params)
            mydb.commit()
            max_sql = "SELECT MAX(id) FROM member"
            mycursor.execute(max_sql)
            maxresult = mycursor.fetchall()
            session['member_id'] = maxresult[0][0]
            session["status"] = "sign in"
            session["name"] = name
            return redirect("/success?message=註冊成功&title=註冊成功&signin=進入會員頁")
        else:
            return redirect("/error?message=帳號已經被註冊&title=註冊失敗&signout=重新註冊")        
    
@app.route("/signin", methods=["POST"])
def signin():
    account = request.form["account"]
    password = request.form["password"]

    if len(account) == 0 or len(password) == 0:
        return redirect("/error?message=請輸入帳號、密碼&status=成功&title=登入失敗&signout=重新登入") 
    else:
        mycursor = mydb.cursor()
        sql = "SELECT * FROM member WHERE username = %s and password = %s"
        params = (account, password)
        mycursor.execute(sql, params)
        myresult = mycursor.fetchone()

        if len(myresult) > 0:
            session["status"] = "sign in"
            session['name'] = myresult[1]
            session['member_id'] = myresult[0]
            return redirect("/member")
        else:
            return redirect("/error?message=帳號或密碼輸入錯誤&title=登入失敗&signout=重新登入")

@app.route("/member")
def member(): 
    mycursor = mydb.cursor()
    sql = "SELECT member.username, message.content FROM member INNER JOIN message ON member.id=message.member_id ORDER BY message.time ASC"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    if "empty_sumit" in session:
        content = {
            "messages": myresult,
            "name": session['name'],
            "empty_sumit": session['empty_sumit']
        }
    else:
        content = {
            "messages": myresult,
            "name": session['name']
        }
    if "status" not in session or session["status"] == "sign out":
        return redirect("/")
    return render_template("member.html", data=content)

@app.route("/message", methods=["POST"])
def message():
    message = request.form["message"]
    
    if len(message) == 0:
        session["empty_sumit"] = "留言內容不可為空白，請重新輸入"
        return redirect("/member")
    else:  
        if "empty_sumit" in session:
            session.pop("empty_sumit")  
        mycursor = mydb.cursor()
        insert_sql = "INSERT INTO message(member_id, content) VALUES(%s, %s)"
        insert_params = ( session['member_id'],message)
        mycursor.execute(insert_sql, insert_params)
        mydb.commit()
        return redirect("/member")

@app.route("/error")
def error():
    message=request.args.get("message")
    title=request.args.get("title")
    signout=request.args.get("signout")
    tmp = {
        "message": message,
        "title": title,
        "signout": signout
    }
    return render_template("error.html", data=tmp)

@app.route("/success")
def success():
    message=request.args.get("message")
    title=request.args.get("title")
    signin=request.args.get("signin")
  
    tmp = {
        "message": message,
        "title": title,
        "signin": signin
    }
    return render_template("success.html", data=tmp)

@app.route("/signout")
def signout():
    session["status"] = "sign out"
    return redirect("/")

app.run(port=3000) 
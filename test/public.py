from flask import *
from database import*

public=Blueprint('public',__name__)

@public.route("/")
def home():
    return render_template('home.html')

@public.route("/login",methods=['get','post'])
def login():
    if 'submit' in request.form:
        uname=request.form['uname']
        psw=request.form['password']
        
        print("/////",uname,psw,"/////")

        qry="select * from login where username='%s' and password='%s'"%(uname,psw)
        res=select(qry)

        print(res)

        if res[0]['usertype']=='admin':
            return redirect(url_for('admin.admin_home'))
        
        if res[0]['usertype']=='user':
            return redirect(url_for('user.user_home'))

       


    return render_template('login.html')

@public.route("/reg",methods=['get','post'])
def reg():
    if 'submit' in request.form:
        name=request.form['name']
        fname=request.form['fname']
        uname=request.form['uname']
        psw=request.form['password']
        address=request.form['address']
        gender=request.form['gender']
        email=request.form['email']

        print("/////",name,fname,uname,psw,address,gender,email,"//////")

        logindata="insert into login values(null,'%s','%s','user')"%(uname,psw)
        b=insert(logindata)

        regdata="insert into registration values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(b,name,fname,uname,psw,address,gender,email)
        insert(regdata)

    return render_template('reg.html')
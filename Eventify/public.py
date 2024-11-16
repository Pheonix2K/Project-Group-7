from flask import *
from database import*

public = Blueprint('public',__name__)

@public.route("/")
def home():
    return render_template('home.html')

@public.route("/login",methods=['post','get'])
def login():
    if 'submit' in request.form:
        uname=request.form['uname']
        psw=request.form['password']

        x="select * from login where username='%s' and password='%s'"%(uname,psw)
        #res stores the dictionary inside the list at 0 index
        #and prints the dictionary with select query
        res=select(x)

        print("//////",res,"///////")

        session['log']=res[0]['Login_id']

        if res:
            #we are only checking the usertype inside the dictionary at the 0 index of list.
            if res[0]['Usertype']=='admin':
                return redirect(url_for('admin.admin'))
            
            if res[0]['Usertype']=='mod':
                qry="select * from moderator where Login_id='%s'"%(session['log'])
                res=select(qry)
                if res:
                    session['mod']=res[0]['Moderator_id']
                return redirect(url_for('mods.moderator'))#blueprint.function
            


    return render_template('login.html')

@public.route("/reg",methods=['post','get'])
def reg():
    if 'submit' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        uname=request.form['uname']
        psw=request.form['password']
        address=request.form['address']
        gender=request.form['gender']
        email=request.form['email']
        phone=request.form['phone']


        logindata="insert into login values(null,'%s','%s','user')"%(uname,psw)
        id=insert(logindata)

        regdata="insert into user values(null,'%s','%s','%s','%s','%s','%s','%s')"%(id,fname,lname,email,gender,phone,address)
        insert(regdata)

    return render_template('reg.html')